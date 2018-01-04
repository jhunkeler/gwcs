# Licensed under a 3-clause BSD style license - see LICENSE.rst
import os
from asdf import util
from asdf.extension import BuiltinExtension

# Make sure that all tag implementations are imported by the time we create
# the extension class so that _gwcs_types is populated correctly.
from .tags import *
from .gwcs_types import _gwcs_types


SCHEMA_PATH = os.path.abspath(
os.path.join(os.path.dirname(__file__), 'schemas'))


class GWCSExtension(BuiltinExtension):
    @property
    def types(self):
        return _gwcs_types #[LabelMapperType, RegionsSelectorType]

    @property
    def tag_mapping(self):
        return [('tag:stsci.edu:gwcs',
                 'http://stsci.edu/schemas/gwcs{tag_suffix}')]

    @property
    def url_mapping(self):
        return [('http://stsci.edu/schemas/gwcs/',
                 util.filepath_to_url(SCHEMA_PATH) +
                 '/{url_suffix}.yaml')]
