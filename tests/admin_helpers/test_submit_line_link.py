from django.contrib.admin.helpers import SubmitLineLink, SubmitLineObject
from django.test import SimpleTestCase


class TestSubmitLineLink(SimpleTestCase):
    def setUp(self):
        self.object = SubmitLineLink()

    def test_inherits_from_submit_line_object(self):
        self.assertIsInstance(self.object, SubmitLineObject)

    def test_p_class_is_empty_string(self):
        self.assertEqual(self.object.p_class, '')

    def test_a_href_is_empty_string(self):
        self.assertEqual(self.object.a_href, '')

    def test_a_class_is_empty_string(self):
        self.assertEqual(self.object.a_class, '')

    def test_a_value_is_empty_string(self):
        self.assertEqual(self.object.a_value, '')

    def test_get_html_returns_correct_html(self):
        self.object.p_class = 'my_p_class'
        self.object.a_href = 'my_a_href'
        self.object.a_class = 'my_a_class'
        self.object.a_value = 'my_a_value'

        self.assertEqual(self.object.get_html(), '<p class="my_p_class"><a href="my_a_href" class="my_a_class">'
                                                 'my_a_value</a></p>')
