from django.db import models
from ulid import ulid


class ULID_field(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 26)
        kwargs.setdefault("default", ulid)
        super().__init__(*args, **kwargs)
