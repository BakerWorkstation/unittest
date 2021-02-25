# -*- coding: utf-8 -*-

import unittest,sys
from mathfunc import *


class TestMathFunc1(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print "begin execute "
        
    @classmethod
    def tearDownClass(cls):
        print "end execute "

  
    def test_add(self):
        self.assertEqual(3,add(1,2))
        
    
    def test_minus(self):
        self.assertEqual(1,minus(2,1))



class TestMathFunc2(unittest.TestCase):

    def test_minus(self):
        self.assertEqual(1,minus(2,1)) 
        
    @unittest.skipIf(sys.platform=="linux2","no execute")  
    def test_multi(self):
        self.assertEqual(1,multi(1,1))
        
        
    def test_divide(self):
        self.assertEqual(2,divide(6,3))
    

