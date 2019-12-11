from os.path import abspath, join

from .conf import get_setting

__title__ = 'tld.helpers'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'MPL-1.1 OR GPL-2.0-only OR LGPL-2.0-or-later'
__all__ = (
    'project_dir',
    'PROJECT_DIR',
)


def project_dir(base: str) -> str:
    """Project dir."""
    tld_names_local_path_parent = get_setting('NAMES_LOCAL_PATH_PARENT')
    return abspath(
        join(tld_names_local_path_parent, base).replace('\\', '/')
    )


PROJECT_DIR = project_dir
