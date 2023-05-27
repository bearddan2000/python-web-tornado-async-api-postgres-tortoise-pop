# app/models.py
from tortoise.models import Model
from tortoise import fields

class Pop(Model):
    name = fields.TextField()
    color = fields.TextField()

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return "<Pop('%s', '%s')>" % (self.name, self.color)
