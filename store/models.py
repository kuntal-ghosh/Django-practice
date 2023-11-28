from django.db import models

# Create your models here.

class Category(models.Model):
    name:models.CharField(max_length=255)
    product=models.ForeignKey('Product', on_delete=models.SET_NULL,null=True,related_name='+')
    
class Promotion(models.Model):
    description=models.CharField(max_length=255)
    discount=models.DecimalField(max_digits=6,decimal_places=2)
class Product(models.Model):
    CATEGORY_ELECTRONICS="ELECTRONICS"
    CLOTHING="Clothing"
    CATEGORIES=[ 
    (CATEGORY_ELECTRONICS, "ElectronICS"),
    (CLOTHING, "Clothing"),
]
    slug=models.SlugField(default="-")
    name = models.CharField(max_length=255)
    description = models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    stock_quantity = models.IntegerField()
    category=models.CharField(max_length=255,choices=CATEGORIES,default=CLOTHING)
    # manufacturer = models.ForeignKey
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    category:models.ForeignKey(Category,on_delete=models.PROTECT)
    promotion:models.ManyToManyField(Promotion)

    
class User(models.Model):
    name=models.CharField(max_length=255)
    description = models.TextField()
    email=models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(255)
    # address=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=255)   
    birth_date=models.DateField(null=True) 
    
class Order(models.Model):
    PENDING="pending"
    COMPLETE="complete"
    FAILED="failed"
    PAYMENT_STATUS=[
          (PENDING,"Pending"),
          (COMPLETE,"Complete"),
          (FAILED,"Failed")
      ]
    status=models.CharField(choices=PAYMENT_STATUS)
    order_date=models.DateTimeField(auto_now=True)
    total_amount=models.DecimalField(max_digits=6,decimal_places=2)
    placed_at=models.DateTimeField(auto_now_add=True)
    customer=models.ForeignKey(User,on_delete=models.PROTECT)  
    #   USER  
 
class OrderItem(models.Model):
     order=models.ForeignKey(Order, on_delete=models.PROTECT)
     product=models.ForeignKey(Product, on_delete=models.PROTECT)
     quantity=models.PositiveIntegerField()
     unit_price=models.DecimalField(max_digits=6,decimal_places=2)
     
     
class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()
    
    # addgress model
class Address(models.Model):
    street =models.CharField(max_length=255)
    city =models.CharField(max_length=255)
    # customer = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
        
        
