from app import app
import unittest

class Test(unittest.TestCase):
   def setUp(self):
       self.app = app.test_client()

   def test_requisicao(self):
       self.assertEqual(self.result.status_code, 200)

   def test_conteudo(self):
       self.assertEqual(self.result.data.decode('utf-8'), "Pipeline-DevOps")

if __name__ == "__main__":
    unittest.main(verbosity=2)
