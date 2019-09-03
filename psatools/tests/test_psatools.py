import unittest
import psatools

class Testpsafuncs(unittest.TestCase):

    def test_calci(self):
        self.assertAlmostEqual(psatools.calci(10,11), 524.86, places=2,
                         msg="Should be 524.86")

    def test_calcp_withpf(self):   
        self.assertAlmostEqual(psatools.calcp(0.5,220,0.95), 181.0, places=2,
                         msg="Should be 181.0")

    def test_calcp_nopf(self):   
        self.assertAlmostEqual(psatools.calcp(0.5,220), 190.53, places=2,
                         msg="Should be 190.53")

    def test_calcpf(self):
        self.assertAlmostEqual(psatools.calcpf(10,0.58785,11),0.893,places=3,
                        msg="Should be 0.893")   

    def test_calcq(self):
        self.assertAlmostEqual(psatools.calcq(15,10),11.18,places=2, 
                              msg="Should be 11.18")                                   

    def test_calcs(self):
        self.assertAlmostEqual(psatools.calcs(3,4),5,places=2, 
                              msg="Should be 5") 

    def test_calcir(self):   
        self.assertAlmostEqual(psatools.calcir(10000,11000,2017,2019),
                                0.0488,places=4, 
                              msg="Should be 0.0488") 
                       

if __name__ == "__main__":
    unittest.main()