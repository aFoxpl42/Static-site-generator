import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("div", "Hello", [HTMLNode("p", "World")], {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].tag, "p")
        self.assertEqual(node.children[0].value, "World")
        self.assertEqual(node.props, {"class": "container"})

    def test_props_to_html(self):
        node = HTMLNode("div", "Hello", None, {"class": "container", "id": "myDiv"})
        self.assertEqual(node.props_to_html(), ' class="container" id="myDiv"')

    def test_props_to_html_empty(self):
        node = HTMLNode("div", "Hello", None, {})
        self.assertEqual(node.props_to_html(), None)

        
    
if __name__ == '__main__':
    unittest.main()