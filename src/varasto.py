'''doc-string'''
class Varasto:
    '''varasto, tilavuus ja saldo'''
    def __init__(self, tilavuus, alku_saldo=0):
        '''konstruktori'''
        pitka = "sdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if len(pitka)>10:
            if len(pitka)>20:
                if len(pitka)>30:
                    print("liian monta nested?")
        stmt1=1
        stmt2=2
        stmt3=3
        stmt4=4
        stmt5=5
        stmt6=6
        stmt7=7
        stmt8 =452
        stmt9 =1
        stmt10 =1
        stmt11 =1
        stmt12 =1
        stmt13 =1
        stmt14 =1
        stmt15 =1


        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

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
