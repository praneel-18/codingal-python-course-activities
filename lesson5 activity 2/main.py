actual_cost=float(input("enter the actual cost:"))
sale_amount=float(input("enter the sale amount"))

if sale_amount>actual_cost:
    profit=sale_amount - actual_cost
    print("profit",profit)

else:
    loss=actual_cost - sale_amount   

    print("loss",loss) 
   
