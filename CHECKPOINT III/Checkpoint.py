class Mensagem:
    def __init__(self, mensagem, data_envio=None):
        self.mensagem = mensagem
        self.data_envio = data_envio or "Agora"

    def detalhes(self):
        return f"Mensagem: {self.mensagem} (Enviado em: {self.data_envio})"

class Texto(Mensagem):
    def detalhes(self):
        return f"Texto: {self.mensagem} (Enviado em: {self.data_envio})"

class Video(Mensagem):
    def __init__(self, mensagem, arquivo, formato, duracao, data_envio=None):
        super().__init__(mensagem, data_envio)
        self.arquivo = arquivo
        self.formato = formato
        self.duracao = duracao

    def detalhes(self):
        return f"Vídeo: {self.mensagem} - Arquivo: {self.arquivo} ({self.formato}) - Duração: {self.duracao}s (Enviado em: {self.data_envio})"

class Foto(Mensagem):
    def __init__(self, mensagem, arquivo, formato, data_envio=None):
        super().__init__(mensagem, data_envio)
        self.arquivo = arquivo
        self.formato = formato

    def detalhes(self):
        return f"Foto: {self.mensagem} - Arquivo: {self.arquivo} ({self.formato}) (Enviado em: {self.data_envio})"

class Arquivo(Mensagem):
    def __init__(self, mensagem, arquivo, formato, data_envio=None):
        super().__init__(mensagem, data_envio)
        self.arquivo = arquivo
        self.formato = formato

    def detalhes(self):
        return f"Arquivo: {self.mensagem} - Arquivo: {self.arquivo} ({self.formato}) (Enviado em: {self.data_envio})"

class Canal:
    def __init__(self, nome):
        self.nome = nome

    def enviar(self, mensagem, identificador):
        return f"Enviando via {self.nome} para {identificador}: {mensagem.detalhes()}"

class WhatsApp(Canal):
    def __init__(self):
        super().__init__("WhatsApp")

    def enviar(self, mensagem, identificador):
        return f"Enviando via {self.nome} para telefone {identificador}: {mensagem.detalhes()}"

class Telegram(Canal):
    def __init__(self):
        super().__init__("Telegram")

    def enviar(self, mensagem, identificador):
        tipo = "telefone" if identificador.startswith("+") else "usuário"
        return f"Enviando via {self.nome} para {tipo} {identificador}: {mensagem.detalhes()}"

class Facebook(Canal):
    def __init__(self):
        super().__init__("Facebook")

    def enviar(self, mensagem, identificador):
        return f"Enviando via {self.nome} para usuário {identificador}: {mensagem.detalhes()}"

class Instagram(Canal):
    def __init__(self):
        super().__init__("Instagram")

    def enviar(self, mensagem, identificador):
        return f"Enviando via {self.nome} para usuário {identificador}: {mensagem.detalhes()}"

if __name__ == "__main__":
    msg_texto = Texto("Olá, mundo!")
    msg_video = Video("Vídeo legal", "video.mp4", "mp4", 120)
    msg_foto = Foto("Foto bonita", "foto.jpg", "jpg")
    msg_arquivo = Arquivo("Documento", "doc.pdf", "pdf")

    whatsapp = WhatsApp()
    telegram = Telegram()
    facebook = Facebook()
    instagram = Instagram()

    print(whatsapp.enviar(msg_texto, "+1234567890"))
    print(telegram.enviar(msg_video, "@usuario"))
    print(facebook.enviar(msg_foto, "usuario_fb"))
    print(instagram.enviar(msg_arquivo, "usuario_ig"))
