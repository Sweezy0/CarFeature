class Car:
    brand=""
    model=""
    color=""
    number_plate=""
car1=Car()
car1.brand="Audi"
car1.model="Rs7"
car1.color="Black"
car1.number_plate="06 RS 007"

car2=Car()
car2.brand="Mercedes"
car2.model="G63 AMG"
car2.color="Black"
car2.number_plate="06 G 063"

print("---CAR 1--- ")
print("brand:{}\nmodel:{}\ncolor:{}\number_plate:{}".format(car1.brand,car1.model,car1.color,car1.number_plate))

print("---CAR 2---")
print("brand:{}\nmodel:{}\ncolor:{}\number_plate:{}".format(car2.brand,car2.model,car2.color,car2.number_plate))
