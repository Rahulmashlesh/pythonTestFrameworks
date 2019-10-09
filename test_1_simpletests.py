# new to python ???? try formking my forked repo 
# 	30 min interactive and simple python tutorial  
#		-----> github.com/Rahulmashlesh/python-tutorial

# list 
def test_sum_true():
	# true case
	assert sum([1, 2, 3]) == 6

def test_sum_false():
	# false case
	assert sum([1, 1, 1]) == 3   # 6

# tuple 
def test_sum_tuple():
    assert sum((1, 2, 2)) == 5, "Should be 5"


if __name__ == "__main__":
	
	test_sum_true()
	#test_sum_false()
	test_sum_tuple()


	print("Everything passed")



## SOME EXAMPLEs OF TEST FRAMEWORKS
# unittest
# nose or nose2
# pytest