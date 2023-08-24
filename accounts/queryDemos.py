#***(1)Return all customers from customer table
customer = Customer.object.all()

#(2)Return first customer in table
firstCustomer = Customer.object.first()

#(3)Return last customer in table
lasatCustomer = Customer.object.last()

#(4)Returns single customer by name
customerByName = Customer.object.get(name='edwin')

#***(5)Returns single customer by id
customerById = Customer.objects.get(id=4)

#***(6)Returns all orders related to customer (firstCustomer variable set above)
firstCustomer.order_set.all()

#(7)***Returns orders customer name: (Query parent model values)
order = Order.object.first()
parentName = order.customer.name

#(8)***Returns products from products table with value of "Out door" in category attribute
products = Products.object.filter(category="Out Door")

#(9)***Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')


#(10)  Returns all products with tag of "Sports":  (Query Many to Many Fields)
productsFiltered = Product.objects.filter(tags__name="Sports")

'''
(11)Bonus
Q:If the customer has more than 1 ball, how would you reflect it in the database?
A: Because there are many different products and this value changes constantly you would most
likely not want to store the value in the database but rather just make this a function we can run
each time we load the customers profile
'''

#Returns the total count for number of time a "Ball" was orderd by the first customer
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

#Return total count for each product ordered
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

#Returns: allOrders: {'Ball': 2, 'BQQ Grill': 1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length =200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length =200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()

