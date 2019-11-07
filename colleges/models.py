from django.db import models
from django.dispatch import receiver
from users.models import User


class Profile(models.Model):
	ROLES = (('DC', 'Director'), ('FC', 'Faculty'), ('MG', 'Management'), ('MS', 'Miscellaneous'))
    
	user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
	college = models.ForeignKey('colleges.College', on_delete=models.CASCADE, related_name='people',blank=True, null=True)
	role = models.CharField(choices=ROLES, max_length=2, default='MS')
	phone_no = models.CharField(max_length=13, blank=True, null=True)

	def __str__(self):
		return self.user.username
	


@receiver(models.signals.post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		profile = Profile(user=instance)
		profile.save()


class College(models.Model):

    Name = models.CharField(null=False, blank=False, max_length=100)
    Address = models.CharField(null=False, blank=False, max_length=100)

    # add more attributes

    def __str__(self):
        return self.Name
