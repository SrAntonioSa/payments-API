from flask import Flask, jsonify, request
from repository.database import db
from db_models.payment import Payment 
from datetime import datetime, timedelta

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'


db.init_app(app)


# rota para criar um pagamento 
@app.route('/payments/pix', methods=['POST'])
# funcao que cria um novo pagamento 
def create_payment_pix():
    data = request.get_json()
    #validacoes
    if 'value' not in data:
        return jsonify({"message":"invalid value"}),400
    
    # usando as funcoes de data para criar uma chave temporaria
    expiration_date = datetime.now() + timedelta(minutes=30)


    # novo pagamento informando os valores de VALOR e a data de expiraCao
    new_payment = Payment(value = data['value'], expiration_date = expiration_date)
    

    # gravando as informacoes no banco de dadops 
    db.session.add(new_payment)
    db.session.commit()

    # a funcao retorna um arquivo json confirmando a transacao e os dados da mesma
    return jsonify({"message": " The payment has been created",
                    "payment": new_payment.to_dict()})

# rota para receber confirmaçao de pagamento WEBHOOK
@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({"message": " The payment has been confirmed"})

#vizualiza pagamento e conexao com websocket
@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return 'pagamento pix'

if __name__ == '__main__':
    app.run(debug=True)
