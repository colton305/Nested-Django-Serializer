
# Nested Django Serializer

An updated version of wadofstuff that is compatible with python3 and Django 4. Used to fully serialize Django model
foreign key and many-to-many relations.

## Installation

The package is available on pypi and can be installed via

`$ pip install nested-django-serializer`

To use the package in your Django project, simply add the following variable to your settings.py

```python
SERIALIZATION_MODULES = {
  'json': 'nested_django_serializer.django.serializers.json'
}
```

## Features

- relations - a list or dictionary of model related fields to be followed
  and serialized.
- extras - a list of non-model field properties or callables to be
  serialized.
- excludes - a list of fields to be excluded from serialization. The
  excludes list takes precedence over the fields argument.

### Relations
The Nested Django Serializer has the ability to fully serialize referenced Django models as opposed to the default 
behaviour of simply returning the primary key value. 

To override the default behaviour, supply the `relations` keyword argument to `serializers.serialize()` 

The argument should either be a list of relations to be serialized or a dictionary of key/value pairs where the keys are
relations to be serialized and the values are lists of arguments to be passed to the serializer when serializing that 
relation.

```python
serializers.serialize('json', Group.objects.all(), indent=4, relations=('permissions',))
[
    {
        "pk": 2,
        "model": "auth.group",
        "fields": {
            "name": "session",
            "permissions": [
                {
                    "pk": 19,
                    "model": "auth.permission",
                    "fields": {
                        "codename": "add_session",
                        "name": "Can add session",
                        "content_type": 7
                    }
                }
            ]
        }
    }
]
```

```python
serializers.serialize('json', Group.objects.all(), indent=4, 
                      relations={'permissions': {'fields': ('content_type', ), 'relations': ('content_type', )}})
[
    {
        "pk": 2,
        "model": "auth.group",
        "fields": {
            "name": "session",
            "permissions": [
                {
                    "pk": 19,
                    "model": "auth.permission",
                    "fields": {
                        "content_type": {
                            "pk": 7,
                            "model": "contenttypes.contenttype",
                            "fields": {
                                "model": "session",
                                "name": "session",
                                "app_label": "sessions"
                            }
                        }
                    }
                }
            ]
        }
    }
]

```
