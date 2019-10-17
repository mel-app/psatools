""" Useful tools for electrical power engineering
List of tools:
calci
calcp
calcs
calcc
calcir
calcpf
 """
import math
import numpy

       
def calci(MVA, kV):
    """ Calculates three phase I in amps from MVA and kV"""
    return round(MVA / (kV * 3**0.5) * 1000, 2)
    
def calcpf(MW, kA, kV):
    """ Calculates three phase pf from MW, kV and kA"""
    return MW / (kV * kA * 3**0.5)

def calcp(kA, kV, cosphi = 1.0):
    """ Calculates three phase P in MW from kA and kV
    takes an optional input power factor""" 
    return 3**(0.5) * kV * kA * cosphi    

def calcq(S, P):
    """ Calculates reactive power given S and P
    """
    assert S > P, "S must be greater than P"
    return (S**2 - P**2)**0.5    
    
def calcs(MW=None, Mvar=None, I=None, V=None):
    """ Calculates S from two out of MW, Mvar, I, and V
    
    If providing I, then V is compulsory
    If provding I, then either MW and Mvar is compulsory
    
    """
    #run some checks
    try:
        if I is not None and V is None:
            raise Exception("Voltage required if current entered")
    except Exception as e:
        print(e)
        raise

    inputs = 0
    #count number of None arguments we get
    if Mvar is not None:
        inputs += 1
    if MW is not None:
        inputs += 1

    try:
        if inputs < 2 and I is None:
            raise Exception("MW, Mvar are required if I not entered.")
    except Exception as e:
        print(e)
        raise

    if MW is not None and Mvar is not None:    
        return (MW**2 + Mvar**2)**0.5
    else:
        #calculate using I and V
        return (3**0.5 * V * I)   
  
def calcir(init,final,startyear,endyear):
    """Calculates growth rate based on a start value and end value and a start
    year and end year.  Assumed annual compounding."""
    return (math.exp(math.log(final/init)/(endyear-startyear))-1)

def calcshcs(Zpu, Vnom, Vpu=1.0):
    """Calculates the short circuit current in Amperes.
    Vpu = Pre-fault voltage (optional) 
    Vnom = Vnom in kV
    Zpu = Impedance in per unit on 100 MVA base
    """
    Spu = Vpu / Zpu
    return 100 * Spu / (3**0.5 * Vnom)  
    