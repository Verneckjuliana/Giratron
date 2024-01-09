import random
import pyttsx3
import time

class Genius:
    cores = ['vermelho', 'verde', 'azul', 'amarelo']

    @staticmethod
    def gerar_sequencia(tamanho):
        return [random.choice(Genius.cores) for _ in range(tamanho)]

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
        palpite = input(f'Tentativa {tentativas}: Digite a sequência de cores (separada por espaços): ').split()
        return palpite == sequencia

class Giratron(Genius):
    #giratron herda de Genius, mas não adiciona comportamento adicional
    pass

if __name__ == "__main__":
    tentativas = 1
    tamanho_sequencia = 3  #tamanho inicial da sequência

    while True:
        #genius
        sequencia_genius = Genius.gerar_sequencia(tamanho_sequencia)
        Genius.reproduzir_sequencia(sequencia_genius)
        acertou_genius = Genius.adivinhar_sequencia(tentativas, sequencia_genius)

        if acertou_genius:
            print("Parabéns! Você acertou.")
            tentativas += 1
            tamanho_sequencia += 1  #aumenta o tamanho da sequência para a próxima jogada
        else:
            print("Errou! Tente novamente.")
            break  #encerra o jogo se o jogador errar
