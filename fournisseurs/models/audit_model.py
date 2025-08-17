# fournisseurs/models/audit_model.py
from django.db import models
from django.conf import settings

class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created_by"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated_by"
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        from allauth.account.signals import user_logged_in
        from django.contrib.auth import get_user_model
        User = get_user_model()

        # Récupérer l'utilisateur actuel
        user = kwargs.pop('user', None)
        
        if not user:
            # Essayer de récupérer l'utilisateur depuis la requête
            from django.core.exceptions import ImproperlyConfigured
            try:
                from crum import get_current_user
                user = get_current_user()
            except (ImportError, ImproperlyConfigured):
                pass

        # Si c'est une nouvelle instance et created_by n'est pas défini
        if not self.pk and not self.created_by:
            self.created_by = user if user and user.is_authenticated else None
        
        # Mettre à jour updated_by
        self.updated_by = user if user and user.is_authenticated else None
        
        super().save(*args, **kwargs)