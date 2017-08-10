import random

def inplace_count(goal_state,init):
	count=0
	for i in range(0,3):
		for j in range(0,3):
			if(goal_state[i][j]==init[i][j] and goal_state[i][j]!=''):
				count=count+1
	return count


init=[]

nums=[1,7,3,5,'',4,6,2,8]

def make_grid(nums,init):
	for i in range(1,10):
		if(i%3==0):
			init.append(nums[i-3:i])


def shuffle(init,nums):
	period=5
#shuffling!
	while(period>0):
		ran1=random.randint(0,100)%9
		ran2=random.randint(0,100)%9
		nums[ran1],nums[ran2]=nums[ran2],nums[ran1]
		period=period-1

def is_valid(init,row,col):
	try:
		if(init[row][col]>0):
			return True
	except:
		return False

	

goal_state=[[1,2,3],
			[4,'',5],
			[6,7,8]]


make_grid(nums,init)

def move():


