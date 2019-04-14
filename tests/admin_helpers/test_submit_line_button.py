from django.contrib.admin.helpers import SubmitLineButton, SubmitLineObject
from django.test import SimpleTestCase


class TestSubmitLineButton(SimpleTestCase):
    def setUp(self):
        self.object = SubmitLineButton()

    def test_inherits_from_submit_line_object(self):
        self.assertIsInstance(self.object, SubmitLineObject)

    def test_value_is_empty_string(self):
        self.assertEqual(self.object.value, '')

    def test_name_is_empty_string(self):
        self.assertEqual(self.object.name, '')

    def test_onclick_is_empty_string(self):
        self.assertEqual(self.object.onclick, '')

    def test_is_highlighted_is_set_to_false(self):
        self.assertFalse(self.object.is_highlighted)

    def test_get_html_returns_correct_html(self):
        self.object.value = 'my_value'
        self.object.name = 'my_name'

        self.assertEqual(self.object.get_html(), '<input value="my_value" name="my_name" type="submit" />')

    def test_get_html_adds_class_default_if_is_highlighted_is_true(self):
        self.object.value = 'my_value'
        self.object.name = 'my_name'
        self.object.is_highlighted = True

        self.assertEqual(self.object.get_html(), '<input value="my_value" name="my_name" type="submit" '
                                                 'class="default" />')

    def test_get_html_adds_onclick_with_onclick_and_type_button_if_onclick_is_set(self):
        self.object.value = 'my_value'
        self.object.name = 'my_name'
        self.object.onclick = 'my_onclick'

        self.assertEqual(self.object.get_html(), '<input value="my_value" name="my_name" onclick="my_onclick" '
                                                 'type="button" />')
