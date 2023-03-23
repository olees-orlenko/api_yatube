from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsContentAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow content authors
    to edit and delete their own content
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or obj.author == request.user:
            return True
