from django.test import TestCase
from django.urls import reverse


class KillSwitchTest(TestCase):
    def test_no_danger_keyword_in_production(self):
        """
        LOGIQUE DE BLOCAGE :

        - Si 'Attention' est present -> Le test ECHOUE (bloque GitHub).
        - Si 'Attention' est absent -> Le test PASSE (autorise le deploiement).
        """
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Attention")
