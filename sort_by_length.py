order=input("Enter the direction in which you want to arrange(asc/des):")
print("You have choosed :",order)

tuple_val=('Hello','This','is','Ash')

def arrangement(order, tuple_value):
    if order=='asc':
        return tuple(sorted(tuple_val,key=len))
    elif order=='des':
        return tuple(sorted(tuple_val,key=len,reverse=True))
    else:
        raise ValueError("invalid choosen. So choose aes or des")
    
print(arrangement(order,tuple_val))
    
