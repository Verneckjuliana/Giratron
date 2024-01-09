import random
import pyttsx3
import time

class Giratron:
    cores = ['vermelho', 'verde', 'azul', 'amarelo']
    numeros = ['um', 'dois', 'três', 'quatro']

    @staticmethod
    def gerar_sequencia(tamanho):
        return [random.choice(Giratron.cores + Giratron.numeros) for _ in range(tamanho)]

    @classmethod
    def reproduzir_sequencia(cls, sequencia):
        engine = pyttsx3.init()
        for item in sequencia:
            engine.say(item)
            engine.runAndWait()
            time.sleep(1)
        engine.stop()

    @staticmethod
    def adivinhar_sequencia(tentativas, sequencia):
        #lógica para adivinhar a sequência
        #implemente conforme necessário
        palpite = input(f'Tentativa {tentativas}: Digite a sequência (separada por espaços): ').split()
        return palpite == sequencia

class GiratronGenius(Giratron):
    @staticmethod
    def adivinhar_sequencia(tentativas, sequencia):
        #lógica específica para adivinhar a sequência no modo Genius (cores + números)
        #implemente conforme necessário
        palpite = input(f'Tentativa {tentativas}: Digite a sequência (separada por espaços): ').split()
        return palpite == sequencia

if __name__ == "__main__":
    tentativas = 1
    tamanho_sequencia = 3  #tamanho inicial da sequência

    while True:
        #giratron
        sequencia_giratron = Giratron.gerar_sequencia(tamanho_sequencia)
        Giratron.reproduzir_sequencia(sequencia_giratron)
        acertou_giratron = Giratron.adivinhar_sequencia(tentativas, sequencia_giratron)

        #GiratronGenius (polimorfismo)
        sequencia_genius = GiratronGenius.gerar_sequencia(tamanho_sequencia)
        GiratronGenius.reproduzir_sequencia(sequencia_genius)
        acertou_genius = GiratronGenius.adivinhar_sequencia(tentativas, sequencia_genius)

        if acertou_giratron or acertou_genius:
            print("Parabéns!")
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")
            tentativas += 1
            tamanho_sequencia += 1  #aumenta o tamanho da sequência para a próxima jogada
        else:
            print("Você errou! TROUXA KKKKKKKKKKKKKKKK")
            break  #encerra o jogo se o jogador errar
