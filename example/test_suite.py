# -*- coding: utf-8 -*-
import unittest,sys
from test_mathfunc import TestMathFunc1,TestMathFunc2
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
                       
    suite = unittest.TestSuite()
    tests=[TestMathFunc1("test_add"),TestMathFunc2("test_minus"),TestMathFunc2('test_multi'),TestMathFunc2('test_divide')]
    suite.addTests(tests)
    with open('htmlreport.html', 'w') as f:                  #生成HTML报告
        runner = HTMLTestRunner(stream=f,
                                title='主题',
                                description='描述',
                                verbosity=2
                                )
        runner.run(suite)      


  
                                


