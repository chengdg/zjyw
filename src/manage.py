#!/usr/bin/env python
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append( ROOT )

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zjyw.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
