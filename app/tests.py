from django.test import TestCase

class PruebasCI(TestCase):
    def test_suma_basica(self):
        self.assertEqual(2 + 2, 4)

    def test_acceso_login_admin(self):
        respuesta = self.client.get('/admin/login/')
        self.assertEqual(respuesta.status_code, 200)