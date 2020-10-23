import pathlib


class Instance:
    """Change me for my purpose
    """

    def __init__(self):
        pass

    def bridge(self, modules):
        """
        Bridge modules
        """
        self.MODULES = modules

    def hello_world(self, caller):
        print('This is a sample module called from {called} by {caller}.'.format(
            called=__file__,
            caller=caller
        ))
