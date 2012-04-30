"""
caselib
~~~~~~~

A string converter between different naming convention.

>>> caselib.convert('HelloWorld', caselib.CamelCase, caselib.snake_case)
'hello_world'
>>> caselib.convert('HELLO_WORLD', caselib.SNAKE_CASE, caselib.camelCase)
'helloWorld'

Links
`````

* `GitHub repository <http://github.com/sublee/caselib>`_
* `development version
  <http://github.com/sublee/caselib/zipball/master#egg=caselib-dev>`_

"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import unittest


class CaselibTestCase(unittest.TestCase):

    def test_convert(self):
        from caselib import convert, CamelCase, camelCase, snake_case, \
                            SNAKE_CASE, hypen_case, HYPEN_CASE
        assert 'helloWorld'  == convert(CamelCase, camelCase, 'HelloWorld')
        assert 'hello_world' == convert(CamelCase, snake_case, 'HelloWorld')
        assert 'HELLO_WORLD' == convert(CamelCase, SNAKE_CASE, 'HelloWorld')
        assert 'HelloWorld'  == convert(camelCase, CamelCase, 'helloWorld')
        assert 'hello_world' == convert(camelCase, snake_case, 'helloWorld')
        assert 'HELLO_WORLD' == convert(camelCase, SNAKE_CASE, 'helloWorld')
        assert 'HelloWorld'  == convert(snake_case, CamelCase, 'hello_world')
        assert 'helloWorld'  == convert(snake_case, camelCase, 'hello_world')
        assert 'HELLO_WORLD' == convert(snake_case, SNAKE_CASE, 'hello_world')
        assert 'HelloWorld'  == convert(SNAKE_CASE, CamelCase, 'HELLO_WORLD')
        assert 'helloWorld'  == convert(SNAKE_CASE, camelCase, 'HELLO_WORLD')
        assert 'hello_world' == convert(SNAKE_CASE, snake_case, 'HELLO_WORLD')
        assert 'hello-world' == convert(SNAKE_CASE, hypen_case, 'HELLO_WORLD')
        assert 'hello-world' == convert(camelCase, hypen_case, 'helloWorld')
        assert 'HELLO-WORLD' == convert(camelCase, HYPEN_CASE, 'helloWorld')


def test_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(CaselibTestCase))
    return suite


setup(
    name='caselib',
    version='0.1.0',
    license='BSD',
    author='Heungsub Lee',
    author_email='h@subl.ee',
    description='A string converter between different naming convention',
    long_description=__doc__,
    platforms='any',
    py_modules=['caselib'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    test_suite='__main__.test_suite'
)
