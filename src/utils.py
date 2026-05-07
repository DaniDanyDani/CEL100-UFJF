"""
Módulo de Utilidades para Processamento Digital de Sinais.

Este módulo fornece funções para manipulação de arquivos de áudio e
processamento de sequências discretas.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile


def carregar_audio(caminho_arquivo):
    """
    Lê um arquivo no formato .wav e extrai os dados da sequência e metadados.

    Args:
        caminho_arquivo (str): O caminho relativo ou absoluto para o arquivo .wav.

    Returns:
        tuple: Uma tupla contendo:
            - x_n (numpy.ndarray): A sequência discretizada do sinal {x[n]}.
            - info (dict): Dicionário contendo os seguintes metadados:
                - 'bits' (int): Número de bits utilizados na quantização.
                - 'N' (int): Número total de amostras da sequência.
                - 'fs' (int): Taxa de amostragem em Hz.
                - 'ts' (float): Período de amostragem em segundos.
    """
    # Importação do arquivo e obtenção da sequência {x[n]}
    fs, x_n = wavfile.read(caminho_arquivo)
    
    # Cálculo do número de bits baseado no tamanho do item em bytes
    bit_depth = x_n.dtype.itemsize * 8
    
    # Obtenção do número total de amostras
    num_amostras = len(x_n)
    
    # Cálculo do período de amostragem (Ts = 1/Fs)
    ts = 1.0 / fs
    
    info = {
        "fs": fs,
        "ts": ts,
        "bits": bit_depth,
        "N": num_amostras
    }
    
    return x_n, info

def plot_sequence(x_n, metadados, titulo="Forma de Onda da Sequência x[n]"):
    """
    Gera a representação gráfica da sequência x[n] de forma discreta e contínua.

    Cria um gráfico de hastes (stem plot) para os valores discretos e uma 
    linha tracejada para representar a interpolação da forma de onda.

    Args:
        x_n (numpy.ndarray): A sequência de amostras obtida do arquivo.
        metadados (dict): Dicionário contendo 'ts' (período de amostragem).
        titulo (str): Título do gráfico.
    """
    # Criação do eixo do tempo em segundos
    n = np.arange(len(x_n))
    tempo = n * metadados['ts']

    plt.figure(figsize=(12, 5))

    # Plota a interpolação (forma de onda) tracejada
    plt.plot(tempo, x_n, '--', color='gray', alpha=0.5, label='Interpolação (Analógico)')

    # Plota a sequência discreta (hastes)
    markerline, stemlines, _ = plt.stem(tempo, x_n, label='Sequência x[n] (Discreto)')
    
    plt.setp(markerline, markersize=3)
    plt.setp(stemlines, linewidth=0.5)

    plt.title(titulo)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.show()