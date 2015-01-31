import re
from blessings import Terminal
from peewee import *

from Utils import logger
from Utils import get_answer

t = Terminal()
db = SqliteDatabase('emails.db')

class Comment(Model):
  email_address = CharField(null=True, default=None, unique=True)
  type_of_organization = CharField(null=True, default=None, unique=True)
  name = CharField(null=True, default=None, unique=True)
  text = TextField(null=True, default=None)

  class Meta:
    database = db

  @classmethod

  def __str__(self):
    return self.email_address + " (%s)" % self.comment
