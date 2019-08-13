import datetime
import mongoengine


class Cat(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    species = mongoengine.StringField(required=True)

    height = mongoengine.FloatField(required=True)
    name = mongoengine.StringField(required=True)
    is_angry = mongoengine.BooleanField(required=True)

    meta = {
        'db_alias': 'core4',
        'collection': 'cats4'
    }
