## PYTEST

## pytest has some other great features:

# Support for the built-in assert statement instead of using special self.assert*() methods
# Support for filtering for test cases
# Ability to rerun from the last failing test
# An ecosystem of hundreds of plugins to extend the functionality


# very simple looking test cases !!!


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 5, "Should be 5"

## to execute install and run command 
# pip3 install pytest --user
# pytest 

# MOre about pytest: https://nose2.readthedocs.io/en/latest/
# test cases need to be in the pattern test_*.py