# D5
D5
Users and Authors were created over to the next way. 
from django.contrib.auth.models import User
user_1 = User.objects.create_user('name')
user_2 = User.objects.create_user('name')

from newspaper.models import Author
author_1 =  Author.objects.create(user_id = 2)
author_2 =  Author.objects.create(user_id = 3)

I also took into account the introduction of authors and users through the site.

"likes" creation, the task of displaying the total number on the screen is not implemented. I didn't understand yet how to realize it.
When creating dislikes, the implementation is not correct, because only authors can dislike the post. When creating this function, if using the same algorithm as when creating likes, a conflict appears. The system says that you need to change the argument, because I am using identical data. If I change User to Author, the conflict disappears, the migration goes through.
