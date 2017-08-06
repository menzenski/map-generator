#!/usr/bin/env python3

import map_generator


def test_version_number():
    version_number_from_package = map_generator.__version__
    print("version number from package = {}"
          .format(version_number_from_package))
    assert '0.0.1a1' == version_number_from_package
