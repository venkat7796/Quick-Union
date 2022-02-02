class quick_union(object):
    def __init__(self,n):
        self.arr = [0] * n
        for i in range(n):
            self.arr[i] = i
    
    def connected(self,p,q):
        if self.arr[p] == self.arr[q]:
            return True
        else:
            return False
    def root(self,node):
        while node != self.arr[node]:
            node = self.arr[node]
        return node
        
    def union(self,p,q):
        id1 = self.root(p)
        id2 = self.root(q)
        self.arr[id1] = id2
    
    def print_arr(self):
        print(self.arr)

c = quick_union(10)
c.union(4,3)
c.union(3,8)
c.union(6,5)
c.union(9,4)
c.union(2,1)
print(c.connected(8,9))
print(c.connected(5,0))
c.union(5,0)
c.union(7,2)
c.union(6,1)
c.union(7,3)
c.print_arr()
