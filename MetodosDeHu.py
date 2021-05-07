import numpy as np
import matplotlib.pyplot as plt
import cv2
from math import sqrt
import math

print(" ----->  ED - PI  <----- ")


def AbreImagem(): #---------------------------------------------------------------------------------------------------------------
    Ferramenta = []
    Entrada = ["exemplo.png", "alicate.png", "allen.png", "rosca.png","boca.png", "fenda.png"]

    """
    Para usuario entrar com o caminho das imagens:
    #  Entrada[i] = ( input("Digite o caminho da imagem: "))
    """
    
    for i in range(0, 6):
        # Abre a imagem da chave Alicate
        imagem = cv2.imread(Entrada[i])
        imagem = cv2.resize(imagem ,(300,300))
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("Nome da janela", imagem)

        # Morfologia Matematica: dilatacao e erosao
        image1 = cv2.erode(imagem, np.ones((3, 3)))
        image2 = cv2.dilate(imagem, np.ones((3, 3)))

        # Binarização de imagem
        ret,thresh1 = cv2.threshold(image1,200,255,cv2.THRESH_BINARY)

        if (i == 0):
            newImg = list()
            newImg = cv2.HuMoments(cv2.moments(thresh1)).flatten()
            print("\nHu da chave para Comparação: ", newImg)
            listanewImg = []
            for i in newImg:
                listanewImg.append(i)
            ComparaHU(listanewImg, listanewImg)

        else:
            if (i == 1):
                Alicate = list()
                Alicate = cv2.HuMoments(cv2.moments(thresh1)).flatten()
                print("\nHu do Alicate: ", Alicate)
                listaAlicate = []
                for i in Alicate:
                    listaAlicate.append(i)
                ComparaHU(listanewImg, listaAlicate)
                Ferramenta.append((ComparaHU(listanewImg, listaAlicate)))
                ConfereFerramenta(Ferramenta)
                posicao =  ConfereFerramenta(Ferramenta)
            else:
                 if (i == 2):
                    Allen = list()
                    Allen = cv2.HuMoments(cv2.moments(thresh1)).flatten()
                    print("\nHu da chave Allen: ", Allen)
                    listaAllen = []
                    for i in Allen:
                        listaAllen.append(i)
                    ComparaHU(listanewImg, listaAllen)
                    Ferramenta.append(ComparaHU(listanewImg, listaAllen))
                    ConfereFerramenta(Ferramenta)
                    posicao =  ConfereFerramenta(Ferramenta)
                 else:                     
                    if (i == 3):
                        Rosca = list()
                        Rosca = cv2.HuMoments(cv2.moments(thresh1)).flatten()
                        print("\nHu da chave de Rosca: ", Rosca)
                        listaRosca = []
                        for i in Rosca:
                            listaRosca.append(i)
                        ComparaHU(listanewImg, listaRosca)
                        Ferramenta.append(ComparaHU(listanewImg, listaRosca))
                        ConfereFerramenta(Ferramenta)
                        posicao =  ConfereFerramenta(Ferramenta)
                    else:
                        if (i == 4):
                            Boca = list()
                            Boca = cv2.HuMoments(cv2.moments(thresh1)).flatten()
                            print("\nHu da chave de Boca: ", Boca)
                            listaBoca = []
                            for i in Boca:
                                listaBoca.append(i)
                            ComparaHU(listanewImg, listaBoca)
                            Ferramenta.append(ComparaHU(listanewImg, listaBoca))
                            ConfereFerramenta(Ferramenta)
                            posicao =  ConfereFerramenta(Ferramenta)
                        else:
                            if (i == 5):
                                Fenda = list()
                                Fenda = cv2.HuMoments(cv2.moments(thresh1)).flatten()
                                print("\nHu da chave de Fenda: ", Fenda)
                                listaFenda = []
                                for i in Fenda:
                                    listaFenda.append(i)
                                ComparaHU(listanewImg, listaFenda)
                                Ferramenta.append(ComparaHU(listanewImg, listaFenda))
                                ConfereFerramenta(Ferramenta)
                                posicao =  ConfereFerramenta(Ferramenta)
                                MostraFerramenta(posicao)

#-----------------------------------------------------  AbreImagem() ------------------------------------------------------------#


def ConfereFerramenta(lista): #------------------------------------------------------------------------------------------------------
    iMenor = 0
    for index in range(len(lista)):
        if lista[index] < lista[iMenor]:
            iMenor = index
    return iMenor
#-------------------------------------------------  ConfereFerramenta() -------------------------------------------------------#

def MostraFerramenta(posicao):  #----------------------------------------------------------------------------------------
    comparacao = posicao
    print("\n\n")
    if  (comparacao == 0):
        print(" -------->  A imagem é a ferramenta Alicate  <--------")
    elif  (comparacao == 1):
        print(" -------->  A imagem é a ferramenta chave Allen <--------")
    elif  (comparacao == 2):
        print(" -------->  A imagem é a ferramenta chave de Boca <--------")
    elif  (comparacao == 3):
        print(" -------->  A imagem é a ferramenta chave de Fenda <--------")
    elif  (comparacao == 4):
        print(" ---------> A imagem é a ferramenta chave de Rosca <---------")
    else:
        print("Essa imagem não é uma ferramenta")
#-------------------------------------------------  ConfereFerramenta() -------------------------------------------------------#

def  ComparaHU(listaEntrada, listaFerramenta) :#---------------------------------------------------------------------
    soma = 0
    for i in range(0,5):
        compara = sqrt((listaEntrada[i] - listaFerramenta[i]) **2)

        soma += (compara)
    print('Comparação das ferramentas:  {:.8f}' .format(soma))
    return soma
#------------------------------------------------------  ComparaHU() -----------------------------------------------------------#



def main():
        AbreImagem()
    
        
#------
# MAIN
#------
if __name__=="__main__":
    main()
    
