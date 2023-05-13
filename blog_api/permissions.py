from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_staff:
            return True
        return obj.author == request.user
