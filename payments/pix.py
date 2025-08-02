import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        # criar pagamento na instituicao financeira
        bank_payment_id = uuid.uuid4() 

        # criando codigo copia e cola 
        hash_payment = f'hash_payment_{bank_payment_id}'

        #qr code
        img = qrcode.make(hash_payment)
        # salvando a imagem em png
        img.save(f"static/img/qrcode_payment_{bank_payment_id}.png")



        return {"bank_paymenmt_id": bank_payment_id,
               "qr_code_path": f"qr_code_payment_{bank_payment_id}"}