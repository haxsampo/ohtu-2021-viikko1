import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_konstruktori_korjaa_negatiivisen_tilavuuden(self):
        varas = Varasto(-5,-5)
        self.assertAlmostEqual(varas.tilavuus, 0)

    def test_konstruktori_korjaa_negatiivisen_saldon(self):
        varas = Varasto(-5,-5)
        self.assertAlmostEqual(varas.saldo, 0)

    def test_konstruktori_tayttaa_saldon_tilavuuden_mukaan(self):
        varas = Varasto(3, 5)
        self.assertAlmostEqual(varas.saldo,3)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_neg_lisays_ei_muuta_saldoa(self):
        curSaldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(curSaldo, self.varasto.saldo)

    def test_lisays_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(100000)
        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_neg_ottaminen_ei_muuta(self):
        curSaldo = self.varasto.saldo
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(curSaldo, self.varasto.saldo)

    def test_kaikki_mita_voidaan(self):
        self.varasto.lisaa_varastoon(2)
        curSaldo = self.varasto.saldo
        self.assertAlmostEqual(curSaldo, self.varasto.ota_varastosta(10000))

    def test_print(self):
        #varas = Varasto(1)
        vastaus = str(self.varasto)
        self.assertAlmostEqual(vastaus, "saldo = 0, vielä tilaa 10")
