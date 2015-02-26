import heapq

# string, string, int -> bool
def sameplaceheur(gstring,sstring,i):
    if i >= len(gstring) or i >= len(sstring):
        return False
    else:
        if sstring[i] == gstring[i]:
            return True
        return False
assert(sameplaceheur('hag','rag',1) == True)

# string,string -> [int]
def sameindexlistconstructor(gstring,string):
    return [j for j in range(max([len(gstring),len(string)])) if sameplaceheur(gstring,string,j)]
assert(sameindexlistconstructor('cat','hat') == [1,2])

# string -> [string]
def deletechar(goal,string):
    succs = []
    for i in range(len(string)):
        if sameplaceheur(goal,string,i) == False:
            succs += [string[:i]+string[i+1:]]
    return succs
assert(deletechar('hi','gas') == ['as','gs','ga'])

# string -> [string]
def addchar(goal,string):
    succs = []
    for l in 'abcdefghijklmnopqrstuvwxyz':
        succs += [l+string]
        succs += [string+l]
        for i in range(len(string)-1):
            succs += [string[:i+1]+l+string[i+1:]]
    return succs
#print addchar('bath','cat')

# string -> [string]
def editchar(goal,string):
    succs = []
    for i in range(len(string)):
        diff = ord(goal[i]) - ord(string[i])
        newchar = chr(ord(string[i]) + diff)
        succs += [string[:i]+newchar+string[i+1:]]

#    for l in 'abcdefghijklmnopqrstuvwxyz':
#        for i in range(len(string)):
#            if sameplaceheur(goal,string,i) == False and string[i] != l:
#                succs += [string[:i]+l+string[i+1:]]
    return succs
#assert below tested with only 'a' instead of entire alphabet string
#assert(editchar('cat') == ['aat','caa'])
#print editchar('cog','cat')

# string,string -> int
def findprefix(goal,string):
    """
    Returns the index marking the last letter in the prefix of the
    string that matches the goal.
    """
    ind = sameindexlistconstructor(goal,string)
    j = -1
    for i in range(len(ind)):
        if i == ind[i]:
            j = i
    return j

assert(findprefix('jgiek','jgiwkw') == 2)
assert(findprefix('jgiek','jgiwww') == 2)
assert(findprefix('car','car') == 2)
assert(findprefix('sdf','ert') == -1)

# string -> int
def weightstate(stringleft):
    return len(stringleft)

# string,string -> string
def editstring(goal,start):
    editlist = []
    heapq.heappush(editlist,(weightstate(start),start))
    visited = set()
    while len(editlist) > 0:
        string = heapq.heappop(editlist)[1]
        print string
        if string not in visited:
            preindex = findprefix(goal,string)
            if preindex == len(goal)-1:
                print string
                return string
            else:
                gleft = goal[preindex+1:]
                sleft = string[preindex+1:]
                if len(sleft) > len(gleft):
                    successors = deletechar(gleft,sleft)
                if len(sleft) < len(gleft):
                    successors = addchar(gleft,sleft)
                if len(sleft) == len(gleft):
                    successors = editchar(gleft,sleft)
                visited.add(string)
                for s in successors:
                    w = weightstate(s)
                    node = (w,string[:preindex+1]+s)
                    heapq.heappush(editlist,node)

g = 'supercalifragialisticexpialidoscious'
s = 'b'
editstring(g,s)
