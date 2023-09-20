class TreeNode(object):
    def __init__(self,left,right,val):
        self.left=left
        self.right=right
        self.val=val
        self.root=None
class oneDTree(object):
    def __init__(self,P,k):
        if P==0:
            self.root=None
        elif len(P)==1:
            self.root=TreeNode(None,None,P[0])
        elif len(P)==2:
            a=TreeNode(None,None,P[0])
            b=TreeNode(None,None,P[1])
            self.root=TreeNode(a,b,P[0])
        else:
            n=len(P)
            if n%2==1:
                self.root=TreeNode(oneDTree(P[0:(n//2)+1],k).root,oneDTree(P[(n//2)+1:n],k).root,P[n//2])
            else:
                if k%2==0:
                    self.root=TreeNode(oneDTree(P[0:(n//2)+1],k+1).root,oneDTree(P[(n//2)+1:n],k+1).root,P[n//2])
                elif k%2==1:
                    self.root=TreeNode(oneDTree(P[0:(n//2)],k+1).root,oneDTree(P[(n//2):n],k+1).root,P[(n//2)-1])
    def preorderpartwise(self,node):
        if node.left==None and node.right==None:
            return [node.val]
        elif node.left==None:
            return [node.val,node.right.val]
        elif node.right==None:
            return [node.val,node.left.val]
        else:
            return [node.val]+self.preorderpartwise(node.left)+self.preorderpartwise(node.right)
    def preorder(self):
        return self.preorderpartwise(self.root)
    def splitnodefromnode(self,x1,x2,node):
        if node==None:
            return None
        elif node.val[1]>x1 and node.val[1]<x2:
            return node
        elif node.val[1]<x1 and node.right!= None:
            return self.splitnodefromnode(x1,x2,node.right)
        elif node.val[1]>x2 and node.left != None:
            return self.splitnodefromnode(x1,x2,node.left)
        elif node.val[1]<x1 and node.right == None:
            return None
        elif node.val[1]>x2 and node.left == None:
            return None
    def splitnode(self,x1,x2):
        return self.splitnodefromnode(x1,x2,self.root)
    def leaves(self,node):
        if node.left==None and node.right==None:
            return [node.val]
        elif node==None:
            return []
        else:
            return self.leaves(node.left)+self.leaves(node.right)
    def traverseleft(self,node,x):
        if node==None:
            return []
        elif node.left==None and node.right==None:
            if node.val[1]>=x:
                return [node.val]
            elif node.val[1]<x:
                return []
        else:
            if node.val[1]>=x:
                return self.traverseleft(node.left,x)+self.leaves(node.right)
            else:
                return self.traverseleft(node.right,x)
    def traverseright(self,node,x):
        if node==None:
            return []
        elif node.left==None and node.right==None:
            if node.val[1]<=x:
                return [node.val]
            elif node.val[1]>x:
                return []
        else:
            if node.val[1]<=x:
                return self.traverseright(node.right,x)+self.leaves(node.left)
            else:
                return self.traverseright(node.left,x)
    def search(self,x1,x2):
        n=self.splitnode(x1,x2)
        if n==None:
            return []
        elif n.left==None and n.right==None:
            return [n.val]
        else:
            return self.traverseleft(n.left,x1)+self.traverseright(n.right,x2)
def leftsort(P,x):
    n=len(P)
    l=[]
    i=0
    while i<n:
        if P[i][0]<=x:
            l.append(P[i])
            i=i+1
        else:
            i=i+1
    return l
def rightsort(P,x):
    n=len(P)
    l=[]
    i=0
    while i<n:
        if P[i][0]>x:
            l.append(P[i])
            i=i+1
        else:
            i=i+1
    return l
class twoDTree(object):
    def __init__(self,Px,Py,k):
        if len(Px)==1:
            self.root=TreeNode(None,None,[Px[0],None])
        elif len(Px)==0:
            self.root=None
        elif len(Px)==2:
            a=TreeNode(None,None,[Px[0],None])
            b=TreeNode(None,None,[Px[1],None])
            self.root=TreeNode(a,b,[Px[0],oneDTree(Py,1)])
        else:
            n=len(Px)
            if n%2==1:
                self.root=TreeNode(twoDTree(Px[0:(n//2)+1],leftsort(Py,Px[n//2][0]),k).root,twoDTree(Px[(n//2)+1:n],rightsort(Py,Px[n//2][0]),k).root,[Px[n//2],oneDTree(Py,1)])
            else:
                if k%2==0:
                    self.root=TreeNode(twoDTree(Px[0:(n//2)+1],leftsort(Py,Px[n//2][0]),k+1).root,twoDTree(Px[(n//2)+1:n],rightsort(Py,Px[n//2][0]),k+1).root,[Px[n//2],oneDTree(Py,1)])
                elif k%2==1:
                    self.root=TreeNode(twoDTree(Px[0:(n//2)],leftsort(Py,Px[(n//2)-1][0]),k+1).root,twoDTree(Px[(n//2):n],rightsort(Py,Px[(n//2)-1][0]),k+1).root,[Px[(n//2)-1],oneDTree(Py,1)])
    def splitnodefromnode(self,x1,x2,node):
        if node==None:
            return None
        elif node.val[0][0]>=x1 and node.val[0][0]<=x2:
            return node
        elif node.val[0][0]<x1 and node.right!= None:
            return self.splitnodefromnode(x1,x2,node.right)
        elif node.val[0][0]>x2 and node.left != None:
            return self.splitnodefromnode(x1,x2,node.left)
        elif node.val[0][0]<x1 and node.right == None:
            return None
        elif node.val[0][0]<x1 and node.left == None:
            return None
    def splitnode(self,x1,x2):
        return self.splitnodefromnode(x1,x2,self.root)
    def traverseleft(self,node,x1,y1,y2):
        if node==None:
            return []
        elif node.left==None and node.right==None:
            if node.val[0][0]>=x1 and y1<=node.val[0][1] and node.val[0][1]<=y2:
                return [node.val[0]]
            else:
                return []
        else:
            if node.val[0][0]>=x1 and node.right.val[1]!=None:
                return self.traverseleft(node.left,x1,y1,y2)+node.right.val[1].search(y1,y2)
            elif node.val[0][0]>=x1 and node.right.val[1]==None:
                if node.right.val[0][1]<=y2 and node.right.val[0][1]>=y1:
                    return self.traverseleft(node.left,x1,y1,y2)+[node.right.val[0]]
                else:
                    return self.traverseleft(node.left,x1,y1,y2)
            else:
                return self.traverseleft(node.right,x1,y1,y2)
    def traverseright(self,node,x1,y1,y2):
        if node==None:
            return []
        elif node.left==None and node.right==None:
            if node.val[0][0]<=x1 and y1<=node.val[0][1] and node.val[0][1]<=y2:
                return [node.val[0]]
            else:
                return []
        else:
            if node.val[0][0]<=x1 and node.left.val[1]!=None:
                return self.traverseright(node.right,x1,y1,y2)+node.left.val[1].search(y1,y2)
            elif node.val[0][0]<=x1 and node.left.val[1]==None:
                if node.left.val[0][1]<=y2 and node.left.val[0][1]>=y1:
                    return self.traverseright(node.right,x1,y1,y2)+[node.left.val[0]]
                else:
                    return self.traverseright(node.right,x1,y1,y2)
            else:
                return self.traverseright(node.left,x1,y1,y2)
    def preorderpartwise(self,node):
        if node.left==None and node.right==None:
            return [node.val]
        elif node.left==None:
            return [node.val,node.right.val]
        elif node.right==None:
            return [node.val,node.left.val]
        else:
            return [node.val]+self.preorderpartwise(node.left)+self.preorderpartwise(node.right)
    def preorder(self):
        return self.preorderpartwise(self.root)
    def search(self,x1,x2,y1,y2):
        n=self.splitnode(x1,x2)
        if n==None:
            return []
        elif n.left==None and n.right==None:
            if n.val[0][1]<=y2 and n.val[0][1]>=y1:
                return [n.val[0]]
            else:
                return []
        else:
            return self.traverseleft(n.left,x1,y1,y2)+self.traverseright(n.right,x2,y1,y2)
def xsort(P):
    l=[]
    i=0
    while i<len(P):
        l.append([P[i][0],i])
        i=i+1
    l.sort()
    n=len(l)
    l2=[]
    j=0
    while j<n:
        l2.append(P[l[j][1]])
        j=j+1
    return l2
def ysort(P):
    l=[]
    i=0
    while i<len(P):
        l.append([P[i][1],i])
        i=i+1
    l.sort()
    n=len(l)
    l2=[]
    j=0
    while j<n:
        l2.append(P[l[j][1]])
        j=j+1
    return l2
class PointDatabase(twoDTree):
    def __init__(self,pointlist):
        n=len(pointlist)
        i=0
        l=[]
        while i<n:
            l.append(list(pointlist[i]))
            i=i+1
        Px=xsort(l)
        Py=ysort(l)
        self.root=twoDTree(Px,Py,1).root
    def searchNearby(self,q,d):
        q=list(q)
        x=q[0]
        y=q[1]
        l=self.search(x-d,x+d,y-d,y+d)
        p=[]
        n=len(l)
        i=0
        while i<n:
            p.append(tuple(l[i]))
            i=i+1
        return p