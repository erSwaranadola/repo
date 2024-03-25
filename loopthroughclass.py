class data:
    def Add(self): 
        list1=[1,2,3,4,5]
        list2=[1,2,3,4,5]
        n=0
        for i in range(len(list1)):
            n+=list1[i]+list2[i]
        print(n)

d =data()
d.Add()