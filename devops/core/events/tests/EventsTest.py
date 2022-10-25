import unittest
from devops.core.events import BaseEvent

class EventsTest(unittest.TestCase):

    def test_baseevent(self):
        self.be = BaseEvent.BaseEvent({},{})


if __name__ == '__main__':
    unittest.main()
