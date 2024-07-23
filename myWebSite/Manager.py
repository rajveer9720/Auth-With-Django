# from django.contrib.auth.base_user import BaseUserManager

# class UserManager(BaseUserManager):
#     def create_user(self, phone, password=None, **extra_FieldS):
#         if not phone:
#          raise ValueError("Phone number is required")
        
#         extra_FieldS['email'] = self.normalize_email (extra_FieldS['email'])
#         user =self.model(phone=phone, **extra_FieldS)
#         user.set_password(password)
#         user.save(using= self.db)
#         return user
    