class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 0.5

class WhippedCreamDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1.5

# Create a plain coffee
coffee = Coffee()
print("Plain Coffee Cost:", coffee.cost())  # Outputs: Plain Coffee Cost: 5

# Add milk
coffee_with_milk = MilkDecorator(coffee)
print("Coffee with Milk Cost:", coffee_with_milk.cost())  # Outputs: Coffee with Milk Cost: 6

# Add sugar
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print("Coffee with Milk and Sugar Cost:", coffee_with_milk_and_sugar.cost())  # Outputs: Coffee with Milk and Sugar Cost: 6.5

# Add whipped cream
fancy_coffee = WhippedCreamDecorator(coffee_with_milk_and_sugar)
print("Fancy Coffee Cost:", fancy_coffee.cost())  # Outputs: Fancy Coffee Cost: 8




# Explanation:
# Component: This is an abstract class or interface that defines the cost() method. It represents the core functionality (in this case, a coffee).

# Coffee: This is a concrete class that implements the Component interface. It represents the plain coffee and provides a base implementation for the cost() method.

# Decorator: This is an abstract class that also implements the Component interface. It contains a reference to a Component object (i.e., the coffee it decorates). The Decorator class itself does not add behavior; it delegates the cost() method to the Component it wraps.

# Concrete Decorators (MilkDecorator, SugarDecorator, WhippedCreamDecorator): These are concrete classes that extend the Decorator class. They add specific functionality by modifying the cost() method. Each concrete decorator adds its own cost to the total.

# How It Works:
# The Component interface ensures that all objects (both base objects and decorators) have the cost() method.
# The Coffee class provides the base cost.
# The Decorator class holds a reference to a Component and forwards the cost() method call to this component.
# Each Concrete Decorator adds its own behavior (extra cost) before or after delegating the call to the wrapped Component.
