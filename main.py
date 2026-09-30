"""Menu interattivo da console per gestire una scuola e i suoi studenti."""

from classes.Scuola import Scuola
from classes.studente import Studente


def _leggi_testo(prompt):
	"""Chiede testo finché l'utente non inserisce un valore non vuoto."""
	while True:
		valore = input(prompt).strip()
		if valore:
			return valore
		print("Il campo non può essere vuoto.")


def _leggi_eta():
	"""Legge un'età intera positiva."""
	while True:
		try:
			eta = int(input("Età: ").strip())
			if eta > 0:
				return eta
			print("Inserisci un'età maggiore di zero.")
		except ValueError:
			print("Inserisci un numero intero valido.")


def _aggiungi_studente(scuola):
	print("\n--- NUOVO STUDENTE ---")
	nome = _leggi_testo("Nome: ")
	cognome = _leggi_testo("Cognome: ")
	eta = _leggi_eta()
	citta = _leggi_testo("Città di residenza: ")

	while True:
		classificazione = input("Classificazione (biennio/triennio): ").strip().lower()
		if classificazione in Studente.CLASSIFICAZIONI_VALIDE:
			break
		print("Valore non valido: scegli biennio oppure triennio.")

	studente = Studente(nome, cognome, eta, citta, classificazione)
	scuola.aggiungi_studente(studente)
	print(f"Studente {nome} {cognome} aggiunto correttamente.")


def _mostra_studenti(studenti):
	if not studenti:
		print("Nessuno studente trovato.")
		return
	for numero, studente in enumerate(studenti, 1):
		print(f"{numero}. {studente}")


def _cerca_per_cognome(scuola):
	cognome = _leggi_testo("Cognome da cercare: ")
	_mostra_studenti(scuola.ricerca_per_cognome(cognome))


def _cerca_per_eta(scuola):
	eta = _leggi_eta()
	_mostra_studenti(scuola.ricerca_per_eta(eta))


def main():
	scuola = Scuola()
	azioni = {
		"1": ("Aggiungi studente", lambda: _aggiungi_studente(scuola)),
		"2": ("Mostra tutti gli studenti", lambda: _mostra_studenti(scuola.studenti)),
		"3": ("Cerca studenti per cognome", lambda: _cerca_per_cognome(scuola)),
		"4": ("Cerca studenti per età", lambda: _cerca_per_eta(scuola)),
		"5": ("Mostra numero di studenti", lambda: print(
			f"Studenti iscritti: {scuola.conteggio_studenti()}"
		)),
	}

	while True:
		print("\n========== GESTIONE SCUOLA ==========")
		for numero, (descrizione, _) in azioni.items():
			print(f"{numero}. {descrizione}")
		print("0. Esci")

		scelta = input("Seleziona un'operazione: ").strip()
		if scelta == "0":
			print("Arrivederci!")
			return
		if scelta not in azioni:
			print("Scelta non valida. Riprova.")
			continue

		try:
			azioni[scelta][1]()
		except (EOFError, KeyboardInterrupt):
			print("\nOperazione interrotta.")
			return


if __name__ == "__main__":
	main()
