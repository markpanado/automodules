class Instance:
    """Test module
    """

    def __init__(self):
        pass

    def bridge(self, modules):
        """
        Bridge modules
        """
        self.MODULES = modules

    def start(self):
        self.MODULES.sample.hello_world(caller=__file__)
