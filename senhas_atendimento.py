import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class SenhasAtendimento(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('senhas_atendimento.ui', self)

        self.cont_atend_prioritario = 0
        self.cont_atend_normal = 0

        self.btn_prioritario.clicked.connect(self.atendimento_prioriatario)
        self.btn_normal.clicked.connect(self.atendimento_normal)

    def gerar_senhas(self, tipo_senha):
        if tipo_senha == 'prioritario':
            self.cont_atend_prioritario += 1
            numero = self.cont_atend_prioritario
            prefixo = "A"

        else:
            self.cont_atend_normal += 1
            numero = self.cont_atend_normal
            prefixo = "B"

        senha = f"{prefixo}{numero:03}"
        self.txt_senha.setText(senha)

    def atendimento_prioriatario(self):
        self.gerar_senhas('prioritario')

    def atendimento_normal(self):
        self.gerar_senhas('normal')

def main():
    app = QApplication(sys.argv)
    window = SenhasAtendimento()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()