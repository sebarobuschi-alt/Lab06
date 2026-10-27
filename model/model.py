from database.DB_connect import get_connection
from errno import errorcode
from database import DB_connect
import mysql.connector
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        lista_strumenti = []
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM strumento")
        if cursor is None:
            lista_strumenti = None

        else:

            for strumento in cursor:
                lista_strumenti.append(strumento)

        return lista_strumenti

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        lista_strumenti_tipo= []
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM strumento")
        if cursor is None or tipo is None:
            lista_strumenti_tipo = None

        else:

            for strumento in cursor:
                if strumento['tipo'] == str(tipo):

                    lista_strumenti_tipo.append(strumento['codice'])

        return lista_strumenti_tipo

