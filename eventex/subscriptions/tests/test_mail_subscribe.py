from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Fernando Fiorentin', cpf='12345678901',
                    email='fernandoffiorentin@gmail.com', phone='54-99905-4297')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com', 'fernandoffiorentin@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Fernando Fiorentin',
            '12345678901',
            'fernandoffiorentin@gmail.com',
            '54-99905-4297',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
