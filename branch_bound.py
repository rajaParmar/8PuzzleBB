import random


class grid_node:
	def __init__(self,grid,cost,blank,parent,child_type):
		self.grid=grid.copy()
		#self.path=
		self.cost=0
		self.child_type=child_type

		for i in range(0,3):
			for j in range(0,3):
				if(self.grid[i][j]==''):
					self.blank=[i,j]
		
		self.parent=parent	


def print_grid(grid):
	for i in grid:
		print(i)


def const_child_type(i):
	types=['l','r','u','d']
	return types[i]


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
	grid[f[0]][f[1]],grid[s[0]][s[1]]=grid[s[0]][s[1]],grid[f[0]][f[1]]

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


def is_valid_child(desc_child,desc_parent):
	if((desc_child=='l' and desc_child=='r') or(desc_child=='r' and desc_parent=='l')):
		return False
	if((desc_child=='u' and desc_child=='d') or(desc_child=='d' and desc_parent=='u')):
		return False
	return True

	

goal_state=[[1,2,3],
			[4,'',5],
			[6,7,8]]


make_grid(nums,init)



def move(init):

	row=[0,0,-1,1]
	col=[-1,1,0,0]#left right up and down
	current=grid_node(init,0,[],None,'')
	children=[0,0,0,0]
	
	print_grid(init)


	while(inplace_count(goal_state,current.grid)!=8):
		for i in range(0,4):
			if((is_valid(current.grid,current.blank[0]+row[i],current.blank[1]+col[i])==True) and is_valid_child(const_child_type(i),current.child_type)):
				new_grid=current.grid.copy()
				bcords=current.blank
				swap(new_grid,bcords,[current.blank[0]+row[i],current.blank[1]+col[i]])
				children[i]=grid_node(new_grid,0,[],current,const_child_type(i)) #creation of children
				new_grid=None
				children[i].cost=inplace_count(goal_state,children[i].grid)
				#print(children[i].cost)
			else:
				children[i]=None
		index=-1
		for i in range(0,4):
			if(children[i]!=None  and children[i].cost>current.cost ): #selection of best
				#max=children[i].cost
				index=i
		if(index==-1):
			print("No solution found!")
			break
		print(index)
		current=children[index] #replacing current with best
		make_none(children)
		print_grid(current.grid)
		print(current.child_type)


move(init)

# node=grid_node(init,0,[0,0],None,'')
# print(node.blank)






