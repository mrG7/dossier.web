'''
dossier.web provides REST web services for Dossier Stack
========================================================

.. This software is released under an MIT/X11 open source license.
   Copyright 2012-2014 Diffeo, Inc.

.. autofunction:: dossier.web.WebBuilder
.. autofunction:: dossier.web.SearchEngine
.. autofunction:: dossier.web.Filter

Here are the available search engines by default:

.. autofunction:: dossier.web.engine_index_scan
.. autofunction:: dossier.web.engine_random

Here are the available filter predicates by default:

.. autofunction:: dossier.web.filter_already_labeled

Some useful utility functions.

.. autofunction:: dossier.web.streaming_sample

.. automodule:: dossier.web.routes
.. automodule:: dossier.web.folder
'''
from dossier.web.builder import WebBuilder, add_cli_arguments
from dossier.web.config import Config
from dossier.web.filters import already_labeled as filter_already_labeled
from dossier.web.filters import \
    nilsimsa_near_duplicates as filter_nilsimsa_near_duplicates
from dossier.web.folder import Folders
from dossier.web.interface import SearchEngine, Filter
from dossier.web.search_engines import random as engine_random
from dossier.web.search_engines import plain_index_scan as engine_index_scan
from dossier.web.search_engines import streaming_sample

__all__ = [
    'WebBuilder', 'add_cli_arguments',
    'Config',
    'Folders',
    'SearchEngine', 'Filter',
    'filter_already_labeled', 'filter_nilsimsa_near_duplicates',
    'engine_random', 'engine_index_scan',
    'streaming_sample',
]
