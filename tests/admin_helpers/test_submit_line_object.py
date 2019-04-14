from django.contrib.admin.helpers import SubmitLineObject
from django.test import SimpleTestCase


class TestSubmitLineObject(SimpleTestCase):
    def setUp(self):
        self.object = SubmitLineObject()

    def test_get_html_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.object.get_html()
