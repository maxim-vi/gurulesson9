from pathlib import Path
import gurulesson9.tests_for_practice_form


def path(file_name):
    return str(
        Path( gurulesson9.tests_for_practice_form.__file__).parent.joinpath(f'testdir/{file_name}').absolute()
    )