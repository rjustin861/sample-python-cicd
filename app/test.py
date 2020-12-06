import unittest
import json
from app import application

class TestArithmetic(unittest.TestCase):
    def setUp(self):
        self.app = application.test_client()
    
    def test_param_as_string_1(self):
        # To test whether the number x and y is passed as a string (x and y is still a number)
        response = self.app.post('/arithmetic', query_string={"x":'5', 'y':'2', 'operation':'+'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual({"results": 7}, data)
    
    def test_param_as_string_2(self):
        # To test whether x and y is passed as a string (x and y is not a number)
        response = self.app.post('/arithmetic', query_string={"x":'hello', 'y':'world', 'operation':'+'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual({"status": '400 Bad Request: The browser (or proxy) sent a request that this '
+            'server could not understand.'}, data)

    def test_sum(self):
        # To test sum operation
        response = self.app.post('/arithmetic', query_string={'x':5, 'y':2, 'operation':'+'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual({"results": 7}, data)
    
    def test_minus(self):
        # To test minus operation
        response = self.app.post('/arithmetic', query_string={'x':5, 'y':2, 'operation':'-'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual({"results": 3}, data)
    
    def test_multiply(self):
        # To test multiply operation
        response = self.app.post('/arithmetic', query_string={'x':5, 'y':2, 'operation':'*'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual({"results": 10}, data)
    
    def test_division(self):
        # To test division operation
        response = self.app.post('/arithmetic', query_string={'x':6, 'y':2, 'operation':'/'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual({"results": 3}, data)

if __name__ == '__main__':
    unittest.main()