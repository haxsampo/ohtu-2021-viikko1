'''doc-string'''
class Varasto:
    '''varasto, tilavuus ja saldo'''
    def __init__(self, tilavuus, alku_saldo=0):
        '''konstruktori'''
        rikkoja = "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.vahentaa_kompleksisuutta_kysym(tilavuus)
        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    def vahentaa_kompleksisuutta_kysym(self, til):
        '''tässä pitää olla stringi'''
        pal = 0.0
        if til > 0.0:
            pal = til
        self.tilavuus = pal


    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        '''tilavuus - saldo'''
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        '''lisää varastoon'''
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        '''palauttaa halutun määrän, kaiken mitä voi, tai nollan'''
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
