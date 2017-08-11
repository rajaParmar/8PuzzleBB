import random


class grid_node:
	def __init__(self,grid,cost,blank,parent):
		self.grid=grid.copy()
		#self.path=
		self.cost=0

		for i in range(0,3):
			for j in range(0,3):
				if(self.grid[i][j]==''):
					self.blank=[i,j]
		
		self.parent=parent	



def inplace_count(goal_state,init):
	count=0
	for i in range(0,3):
		for j in range(0,3):
			if(goal_state[i][j]==init[i][j] and goal_state[i][j]!=''):
				count=count+1
	return count


init=[]

nums=[1,7,3,5,'',4,6,2,8]

def swap(grid,f,s):
	grid[f[0]][f[1]],grid[s[0]s[1]]=grid[s[0]s[1]],grid[f[0]][f[1]]

def make_grid(nums,init):
	for i in range(1,10):
		if(i%3==0):
			init.append(nums[i-3:i])

def make_none(list):
	for i in list:
		i=None

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

def move(init):
	row=[-1,1,0,0]
	col=[0,0,-1,1]
	current=grid_node(init,0,[],None)
	children=[0,0,0,0]
	
	while(inplace_count(goal_state,current.grid)!=8):
		for i in range(0,4):
			if(is_valid(current.grid,current.blank[0]+row[i],current.blank[1]+col[i])==True):
				new_grid=current.copy()
				bcords=current.blank
				swap(new_grid,bcords,[new_grid[bcords[0]+row[i]],new_grid[bcords[1]+col[i]]])
				children[i]=grid_node(new_grid,0,[],current)
				new_grid=None
				children[i].cost=inplace_count(goal_state,children[i].grid)
			else:
				children[i]=None
		max=-10
		index=-1
		for i in range(0,4):
			if(children[i]!=None and children[i].cost>max):
				max=children[i].cost
				index=i
		current=children[index]
		make_none(children)











