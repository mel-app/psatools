import pytest
from pytest import approx
from psatools.eemath import *  


def test_calci():
    assert calci(10,11) == approx(524.86)

def test_calcp_withpf():   
    assert calcp(0.5,220,0.95) == approx(180.9993)

def test_calcp_nopf():   
    assert calcp(0.5,220) == approx(190.5255)

def test_calcpf():
    assert calcpf(10,0.58785,11) == approx(0.8928534)

def test_calcq():
    assert calcq(15,10) == approx (11.18033)                                   

def test_calcs():
    assert calcs(3,4) == approx(5) 
    assert calcs(I = 1, V=220) == approx(381.051)

def test_calcir():   
    assert calcir(10000,11000,2017,2019) == approx(.04880884)

def test_calcshcs():                   
    assert calcshcs(0.1,11) == approx(52.4863881) 
