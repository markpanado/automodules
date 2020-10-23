# pylint: disable=E1101

import os
import importlib.util
import glob


class Modules:
    """Dynamic class to handle modules from ./modules
    """

    def __init__(self):
        pass


# Instance of dynamic class
MODULES = Modules()

# Load all modules from ./modules to MAIN
for path in glob.glob('modules/*.py'):
    module_name = os.path.basename(path)[:-3]
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    setattr(MODULES, module_name, module.Instance())

    # Bridge MAIN
    if 'bridge' in dir(getattr(MODULES, module_name)):
        getattr(getattr(MODULES, module_name), 'bridge')(MODULES)

if __name__ == '__main__':
    """Direct execution
    """

    MODULES.main.start()
