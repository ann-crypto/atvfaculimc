import wx


# Função para calcular o IMC
def calcular_imc(altura_cm, peso_kg):
    try:
        altura_m = float(altura_cm) / 100  # Converte para metros
        peso = float(peso_kg)
        imc = peso / (altura_m ** 2)
        return round(imc, 2)
    except ValueError:
        return None


# Classe principal da interface gráfica
class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(240, 240, 240))  # Cor de fundo
        self.SetSize((400, 350))
        self.SetTitle("Calculadora de IMC")

        # Layout com o uso de GridBagSizer
        sizer = wx.GridBagSizer(5, 5)  # 5px de espaçamento entre os widgets

        # Rótulos e campos de entrada
        nome_label = wx.StaticText(self.panel, label="Nome do Paciente:")
        self.nome_text = wx.TextCtrl(self.panel)

        endereco_label = wx.StaticText(self.panel, label="Endereço Completo:")
        self.endereco_text = wx.TextCtrl(self.panel)

        altura_label = wx.StaticText(self.panel, label="Altura (cm):")
        self.altura_text = wx.TextCtrl(self.panel)

        peso_label = wx.StaticText(self.panel, label="Peso (kg):")
        self.peso_text = wx.TextCtrl(self.panel)

        # Campo para mostrar o resultado do IMC
        self.resultado_label = wx.StaticText(self.panel, label="Resultado do IMC: -")

        # Botões
        self.calcular_btn = wx.Button(self.panel, label="Calcular")
        self.calcular_btn.Bind(wx.EVT_BUTTON, self.on_calcular)

        self.reiniciar_btn = wx.Button(self.panel, label="Reiniciar")
        self.reiniciar_btn.Bind(wx.EVT_BUTTON, self.on_reiniciar)

        self.sair_btn = wx.Button(self.panel, label="Sair")
        self.sair_btn.Bind(wx.EVT_BUTTON, self.on_sair)

        # Organizando os widgets no GridBagSizer
        sizer.Add(nome_label, pos=(0, 0), flag=wx.LEFT | wx.TOP, border=10)
        sizer.Add(self.nome_text, pos=(0, 1), flag=wx.EXPAND | wx.TOP, border=10)

        sizer.Add(endereco_label, pos=(1, 0), flag=wx.LEFT, border=10)
        sizer.Add(self.endereco_text, pos=(1, 1), flag=wx.EXPAND, border=10)

        sizer.Add(altura_label, pos=(2, 0), flag=wx.LEFT, border=10)
        sizer.Add(self.altura_text, pos=(2, 1), flag=wx.EXPAND, border=10)

        sizer.Add(peso_label, pos=(3, 0), flag=wx.LEFT, border=10)
        sizer.Add(self.peso_text, pos=(3, 1), flag=wx.EXPAND, border=10)

        sizer.Add(self.resultado_label, pos=(4, 0), span=(1, 2), flag=wx.LEFT | wx.TOP, border=10)

        sizer.Add(self.calcular_btn, pos=(5, 0), flag=wx.ALL | wx.CENTER, border=10)
        sizer.Add(self.reiniciar_btn, pos=(5, 1), flag=wx.ALL | wx.CENTER, border=10)
        sizer.Add(self.sair_btn, pos=(6, 0), span=(1, 2), flag=wx.ALL | wx.CENTER, border=10)

        self.panel.SetSizerAndFit(sizer)

    # Função chamada quando o botão "Calcular" é pressionado
    def on_calcular(self, event):
        nome = self.nome_text.GetValue()
        endereco = self.endereco_text.GetValue()
        altura = self.altura_text.GetValue()
        peso = self.peso_text.GetValue()

        if nome and endereco and altura and peso:
            imc = calcular_imc(altura, peso)
            if imc:
                self.resultado_label.SetLabel(f"Resultado do IMC: {imc}")
            else:
                self.resultado_label.SetLabel("Valores inválidos. Tente novamente.")
        else:
            self.resultado_label.SetLabel("Por favor, preencha todos os campos.")

    # Função chamada quando o botão "Reiniciar" é pressionado
    def on_reiniciar(self, event):
        self.nome_text.SetValue("")
        self.endereco_text.SetValue("")
        self.altura_text.SetValue("")
        self.peso_text.SetValue("")
        self.resultado_label.SetLabel("Resultado do IMC: -")

    # Função chamada quando o botão "Sair" é pressionado
    def on_sair(self, event):
        self.Close()


# Função principal para rodar a aplicação
def main():
    app = wx.App(False)
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
