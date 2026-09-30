from .studente import Studente


class Scuola:
	"""Gestisce l'elenco degli studenti iscritti."""

	def __init__(self):
		self.studenti = []

	def aggiungi_studente(self, studente):
		if not isinstance(studente, Studente):
			raise TypeError("studente deve essere un'istanza di Studente")
		self.studenti.append(studente)

	def ricerca_per_cognome(self, cognome):
		"""Restituisce gli studenti con il cognome indicato."""
		return [
			studente for studente in self.studenti
			if studente.cognome.lower() == cognome.lower()
		]

	def ricerca_per_eta(self, eta):
		"""Restituisce gli studenti con l'eta indicata."""
		return [studente for studente in self.studenti if studente.eta == eta]

	def conteggio_studenti(self):
		"""Restituisce il numero totale degli studenti."""
		return len(self.studenti)
