"""
test model
"""


from nose.tools import ok_
from circus.core.models import Model
from circus.tests import PROJ_PATH, pvpower_models
from circus.core import logging
import os
import sys

LOGGER = logging.getLogger(__name__)

sys.path.append(PROJ_PATH)


def test_circus_model():
    """
    Test Model
    """

    test_model_file = os.path.join(PROJ_PATH, 'models', 'default.json')
    circus_model_test1 = pvpower_models.PVPower(test_model_file)
    ok_(isinstance(circus_model_test1, Model))
    LOGGER.debug('base dir: %s', circus_model_test1.BASE_DIR)
