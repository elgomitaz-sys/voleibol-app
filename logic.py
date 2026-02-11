class PartidoVoleibol:
    def __init__(self):
        self.puntos = {"A": 0, "B": 0}
        self.sets = {"A": 0, "B": 0}
        self.set_actual = 1
        self.max_sets = 5
        self.terminado = False

    def punto(self, equipo):
        if self.terminado:
            return
        if equipo not in ("A", "B"):
            return

        self.puntos[equipo] += 1
        self._verificar_set()

    def restar_punto(self, equipo):
        if self.terminado:
            return
        if self.puntos[equipo] > 0:
            self.puntos[equipo] -= 1

    def _verificar_set(self):
        a, b = self.puntos["A"], self.puntos["B"]
        limite = 15 if self.set_actual == 5 else 25

        if (a >= limite or b >= limite) and abs(a - b) >= 2:
            ganador = "A" if a > b else "B"
            self.sets[ganador] += 1
            self.puntos = {"A": 0, "B": 0}
            self.set_actual += 1

            if self.sets[ganador] == 3:
                self.terminado = True

    def reiniciar_set(self):
        if self.terminado:
            return
        self.puntos = {"A": 0, "B": 0}

    def reiniciar_partido(self):
        self.__init__()

    def ganador(self):
        if self.sets["A"] == 3:
            return "Equipo A"
        if self.sets["B"] == 3:
            return "Equipo B"
        return None
