class Car:
    def __init__(self, fuel, mileage, km_run, fuel_capacity):
        self.fuel = fuel
        self.mileage = mileage
        self.km_run = km_run
        self.fuel_capacity = fuel_capacity

    def change_mileage(self, nem_mileage):
        self.mileage = nem_mileage

    def reset_km_run(self):
        self.km_run = 0

    def change_capacity(self, new_fuel_capacity):
        self.fuel_capacity = new_fuel_capacity

    def display_info(self):
        print("The car's Condition")
        print('-----------------------')
        print('Current Fuel:', self.fuel)
        print('Current (km/l):', self.mileage)
        print('Kilometers run till now:', self.km_run)
        print('Maximum fuel capacity (in liters):', self.fuel_capacity)

    def run(self, km):
        liters_to_run = km / self.mileage
        if self.fuel > liters_to_run:
            print('Successfully run!')
            self.km_run += km
            self.fuel -= liters_to_run
        else:
            print('Insufficient fuel!')

    def refiil(self, liters):
        if self.fuel + liters > self.fuel_capacity:
            print("We can't add that much fuel")
        else:
            self.fuel += liters
            print('Successfully refilled!')

a = Car(50, 12, 32, 100)
a.display_info()

a.run(15)
a.display_info()

a.refiil(10)
a.display_info()