def destructure_branches(branches):
	return branches.splitlines()
    
def unify_commands(commands):
	return '\n'.join(commands)
    	

def delete_git_branches(branches):
    delete_commands = []
    for branch in destructure_branches(branches):
        delete_commands.append('git branch -D ' + branch)
    return unify_commands(delete_commands)

def main():
    branches = """test1
test2"""
    delete_commands = delete_git_branches(branches)
    print(delete_commands)
    
if __name__ == '__main__':
	main()

###### output #######
# git branch -D test1
# git branch -D test2
#####################
