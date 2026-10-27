import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view
        self._view.pulsante_mostra_strumenti = self.mostra_strumenti
        self._view.pulsante_cerca_strumenti = self.cerca_strumenti_tipo

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostra_strumenti(self,e):
        strumenti = self._model.get_strumenti()
        self._view.lista_strumenti.controls.clear()
        if not strumenti:
            self._view.lista_strumenti.controls.append(
                    ft.Text("Nessuno strumento trovato nel database.", color=ft.colors.RED)
                )
        else:
            for s in strumenti:
                disp_str = "disponibile" if s.disponibile else "non disponibile"
                info_testo = (f"{s.codice} - {s.marca} | {s.anno_acquisto} | {s.valore}€ | {disp_str}"
                )
                self._view.lista_strumenti.controls.append(ft.Text(info_testo, size = 14))
                self._view.update()



    def cerca_strumenti_tipo(self,e):
        tipo_cercato = self._view.input_tipo_strumento.value
        if not self._model.lista_strumenti:
            self._model.get_strumenti()

            risultati = self._model.lista_strumenti.cerca_strumenti_per_tipo(tipo_cercato)
            self._view.lista_strumenti_ricerca.controls.clear()

        if not risultati:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text("Nessun risultato trovato"))
        else:
            for s in risultati:
                self._view.lista_strumenti_ricerca.controls.append(
                    info_testo = f"{s.codice} - {s.marca} | {s.anno_acquisto} | {s.valore}€"
                    )
        self._view.update()
