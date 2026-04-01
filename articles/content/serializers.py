from rest_framework import serializers
from .models import JobPosting, UserProfile

LOCKED_TEXT = "🔒 Premium Feature"

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        request = self.context.get('request')
        user = request.user if request else None

        # Default: mask fields
        is_premium = False

        if user and user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.membership == 'premium':
                    is_premium = True
            except UserProfile.DoesNotExist:
                pass

        if not is_premium:
            data['company_name'] = LOCKED_TEXT
            data['salary_range'] = LOCKED_TEXT
            data['application_link'] = LOCKED_TEXT

        return data