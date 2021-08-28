import peewee
from datetime import datetime

database = peewee.MySQLDatabase('pythondb', 
                                 host='localhost', 
                                 port=3306, 
                                 user='root', 
                                 passwd='root')


#users
# 
class User(peewee.Model):
    username = peewee.CharField(max_length=50, unique=True, index=True)
    email = peewee.CharField(max_length=60, null=False)
    active = peewee.BooleanField(default=False)
    created_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = database
        db_table = 'usersnew'

    #devuelve el nombre!
    def __str__(self):
        return self.username

if __name__ == '__main__':

    if User.table_exists():
        User.drop_table()

    User.create_table()

    user1 = User(username='user1', email='user1@example.com')
    print (user1)

