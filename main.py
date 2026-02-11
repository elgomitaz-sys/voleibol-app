from kivy.config import Config

Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty

from logic import PartidoVoleibol


class Marcador(BoxLayout):
    puntos_a = StringProperty("0")
    puntos_b = StringProperty("0")
    sets_a = StringProperty("0")
    sets_b = StringProperty("0")
    set_actual = StringProperty("1")
    estado = StringProperty("")
    bloqueado = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.partido = PartidoVoleibol()
        self.actualizar()

    def punto_a(self):
        self.partido.punto("A")
        self.actualizar()

    def punto_b(self):
        self.partido.punto("B")
        self.actualizar()

    def restar_a(self):
        self.partido.restar_punto("A")
        self.actualizar()

    def restar_b(self):
        self.partido.restar_punto("B")
        self.actualizar()

    def reiniciar_set(self):
        self.partido.reiniciar_set()
        self.actualizar()

    def reiniciar_partido(self):
        self.partido.reiniciar_partido()
        self.actualizar()

    def actualizar(self):
        self.puntos_a = str(self.partido.puntos["A"])
        self.puntos_b = str(self.partido.puntos["B"])
        self.sets_a = str(self.partido.sets["A"])
        self.sets_b = str(self.partido.sets["B"])
        self.set_actual = str(self.partido.set_actual)
        self.bloqueado = self.partido.terminado

        ganador = self.partido.ganador()
        self.estado = f"Ganador: {ganador}" if ganador else ""


class VoleibolApp(App):
    def build(self):
        return Marcador()


if __name__ == "__main__":
    VoleibolApp().run()
