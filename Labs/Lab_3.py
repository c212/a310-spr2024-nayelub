# permutation and factorial
def perm(word):
  # base case, empty string
  answer = []
  if len(word) == 0:
    return ['']
  # inductive case
  for i in range(len(word)):
    letter = word[i]
    remaining = word[:i] + word[i+1:]
    # every other character in the word
    a = perm(remaining)
    for w in a:
        answer = answer + [ letter + w ]
  return answer
  
perm('abc')

def fact(n):
  if n==0:
    return 1
  return n * fact(n-1)

fact(3)


class bst:
  #step 1 initialization
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
  #step 2 insertion
    def insert(self,key):
        if self.key == key:
            return
        elif self.key<key: # new > root
            if self.right == None:
                self.right = bst(key)
                return
            else:
                self.right.insert(key)
        else: #new node is less than root
            if self.left == None:
                self.left = bst(key)
                return
            else:
                self.left.insert(key)
    def isLeaf(self):
      if self.left == None and self.right == None:
        return True

    def delete(self,key):
        if self.key>key:
            if self.left.key == key:
                if self.left.isLeaf()==True:
                    self.left=None
                    return
            self.left.delete(key)
        elif self.key<key:
            if self.right.key == key:
                if self.right.isLeaf()==True:
                    self.right=None
                    return
            self.right.delete(key)
        else:
            if self.right!=None:    #to find smallest value in right
                temp = self.right  #using this to go deep
                prev_node = self   #using this to go left or right
                k = 0
                while temp.left!=None:
                    if k==0:
                        prev_node=prev_node.right
                        k+=1
                    else:
                        prev_node=prev_node.left
                        k+=1
                    temp=temp.left
                self.key = temp.key
                if k>0:
                    prev_node.left=temp.right
                else:
                    prev_node.right=temp.right
            elif self.left!=None:
                temp = self.left
                prev_node = self
                k = 0
                while temp.right!=None:
                    if k==0:
                        prev_node=prev_node.left
                        k+=1
                    else:
                        prev_node=prev_node.right
                        k+=1
                    temp=temp.right
                self.key = temp.key
                if k>0:
                    prev_node.right=temp.left
                else:
                    prev_node.left=temp.left
            else:
                print("You are root, can't delete last node")


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()#you can replace with w,h,m
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()#you can replace with w,h,m
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()# (n =1,p=1,x=0) you can replace with l_w,l_h,l_m
        right, m, q, y = self.right._display_aux() #m=1,q=1,y=0 you can replace with r_w,r_h,r_m
        s = '%s' % self.key
        u = len(s)#u=1
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2




a = bst(50)
a.insert(30)
a.insert(70)
a.insert(60)
a.insert(40)
a.insert(10)
a.insert(90)
a.insert(80)
a.insert(3)
a.insert(1)
a.display()

a.delete(50)
a.display()
