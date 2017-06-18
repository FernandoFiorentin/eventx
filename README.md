#Eventex

Sistema de eventos encomendado pela Morena

##Como desenvolver?

1. Clone o repositório
2. Crie um virtual env com python 3.5
3. Ative o virtual env
4. Instale as dependecias
5. Configure a instancia com o .env
6. Execute os testes

```console
git clone git@github.com:henriquebastos/eventex.git wttd
cd wttd
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

##Como fazer deploy?

1. Crie uma instancia no heroku
2. Envie as configuraçõs para o heroku
3. Defina uma SECRET_KEY segura para a instancia
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroky create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
@configura o email
git push heroku master --force
```