class Studente:
	"""Rappresenta uno studente con la relativa classificazione scolastica."""

	CLASSIFICAZIONI_VALIDE = {"biennio", "triennio"}

	def __init__(self, nome, cognome, eta, citta_residenza, classificazione):
		if classificazione.lower() not in self.CLASSIFICAZIONI_VALIDE:
			raise ValueError("La classificazione deve essere 'biennio' o 'triennio'.")

		self.nome = nome
		self.cognome = cognome
		self.eta = eta
		self.citta_residenza = citta_residenza
		self.classificazione = classificazione.lower()

	def __str__(self):
		return self.to_string()

	def to_string(self):
		return (
			f"Studente: {self.nome} {self.cognome}, "
			f"età: {self.eta}, "
			f"città di residenza: {self.citta_residenza}, "
			f"classificazione: {self.classificazione}"
		)
