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
        self.lista_strumenti = []


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

        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM strumento")

        self.lista_strumenti = []
        try:
            if cursor is None:
               return None

            else:

                for row in cursor.fetchall():

                    s = Strumento(
                        codice=row['codice'],
                        tipo=row['tipo'],
                        marca=row['marca'],
                        anno_acquisto=row['anno_acquisto'],
                        valore=row['valore'],
                        disponibile=bool(row['disponibile'])
                    )
                    self.lista_strumenti.append(s)
                return self.lista_strumenti
        finally:
            cursor.close()
            cnx.close()




    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None

        """
        lista_strumenti_ricerca = []

        tipo_cercato = str(tipo)

        if not self.lista_strumenti or not isinstance(tipo,str):
            return None


        else:
             for s in self.lista_strumenti:
                 if s.tipo == tipo_cercato:
                     lista_strumenti_ricerca.append(s)
             return lista_strumenti_ricerca


