# Task 1: Data Types and Slicing
mixed_data = [10, "apple", 3.14, "banana", 25, 8.7, "orange", 42]

# Slicing
print("Task 1:")
print("First three elements:", mixed_data[:3])
print("Elements from 2nd to 5th position:", mixed_data[1:5])
print("Last two elements:", mixed_data[-2:])
print("\n")

# Task 2: Functions
def calculate_discount(original_price, discount_percentage=10):
    discounted_price = original_price - (original_price * discount_percentage / 100)
    return discounted_price

# Demonstrate the function
discounted_price = calculate_discount(100)
print("Task 2:")
print("Discounted Price:", discounted_price)
print("\n")

# Task 3: Control Flow
if discounted_price < 50:
    print("Low-cost item.")
elif 50 <= discounted_price <= 100:
    print("Moderate-cost item.")
else:
    print("High-cost item.")
print("\n")

# Task 3: Loop through mixed_data
print("Task 3:")
for item in mixed_data:
    print(f"{item} - {type(item)}")
print("\n")

# Task 4: File Handling
with open("product_descriptions.txt", "r") as file:
    descriptions = file.read().splitlines()

formatted_descriptions = [description.title() for description in descriptions]

with open("formatted_descriptions.txt", "w") as file:
    file.write("\n".join(formatted_descriptions))
print("Task 4: File Handling - Check formatted_descriptions.txt file.\n")

# Task 5: Advanced-Data Structure
customer_info = {'name': 'John Doe', 'age': 30, 'purchase_history': ['Book', 'Laptop', 'Shoes']}
print("Task 5:")
print("Customer's Name:", customer_info['name'])
print("Second Purchase:", customer_info['purchase_history'][1])
print("\n")

# Task 6: Classes and Objects
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}")

# Create an instance of the Book class
book_instance = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
print("Task 6:")
book_instance.display_info()
