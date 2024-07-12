import pandas as pd
import numpy as np
from random import randint, choice, uniform
from faker import Faker
from tqdm import tqdm

# Initialize Faker to generate random data
fake = Faker()

# Define the parameters for the dataset
start_date = '2024-01-01'
end_date = '2024-07-18'
num_records = 980  # Specify the total number of records you want to generate
transaction_ids = [f'T00{i+1}' for i in range(100)]  # Adjust the range as needed for unique transaction IDs
customer_ids = [f'C00{i+1}' for i in range(100)]  # Adjust the range as needed for unique customer IDs
store_ids = ['S001', 'S002', 'S003', 'S004', 'S005']
categories = [
    ('Electronics', ['Laptops', 'Smartphones', 'Headphones', 'Gaming Consoles', 'Digital Cameras', 'Printers', 'Routers', 'Wearable Devices', 'Home Assistants', 'Bluetooth Speakers']),
    ('Home Appliances', ['Washing Machines', 'Refrigerators', 'Microwave Ovens', 'Vacuum Cleaners', 'Coffee Makers', 'Dishwashers', 'Electric Kettles', 'Air Purifiers', 'Water Heaters', 'Blenders']),
    ('Fashion and Accessories', ['Shoes', 'Handbags', 'Sunglasses', 'Watches', 'Jackets', 'Jewelry', 'Belts', 'Hats', 'Scarves', 'Gloves']),
    ('Health and Wellness', ['Vitamins', 'Supplements', 'Skincare Products', 'Haircare Products', 'Fitness Equipment', 'Yoga Accessories', 'Massage Devices', 'Health Monitors', 'Protein Powders', 'Essential Oils']),
    ('Books and Media', ['Fiction Books', 'Non-Fiction Books', 'eBooks', 'Audiobooks', 'Magazines', 'CDs', 'DVDs', 'Vinyl Records', 'Comic Books', 'Graphic Novels']),
    ('Sports and Outdoors', ['Bicycles', 'Treadmills', 'Yoga Mats', 'Dumbbells', 'Camping Gear', 'Running Shoes', 'Sports Apparel', 'Fitness Trackers', 'Water Bottles', 'Hiking Boots'])
    ('Toys and Games', ['Board Games', 'Puzzles', 'Action Figures', 'Dolls', 'LEGO Sets', 'RC Cars', 'Video Games', 'Stuffed Animals', 'Educational Toys', 'Building Blocks']),
    ('Automotive', ['Car Accessories', 'Motorcycle Gear', 'Car Electronics', 'Tires', 'Car Care Products', 'Motorcycle Helmets', 'Car Tools', 'Car Seats', 'Motorcycle Jackets', 'GPS Devices']),
    ('Home and Garden', ['Furniture', 'Garden Tools', 'Outdoor Furniture', 'Indoor Plants', 'Gardening Supplies', 'Home Decor', 'Lighting', 'Bedding', 'Kitchen Tools', 'BBQ Grills'])

]
payment_methods = ['Cash', 'Credit Card', 'Debit Card', 'Mobile Payment']
loyalty_programs = ['Yes', 'No']
locations = ['Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Hyderabad']
income_levels = ['<25,000', '25,000-49,999', '50,000-74,999', '75,000-99,999', '100,000+']

# Generate random dates between start_date and end_date
date_range = pd.date_range(start=start_date, end=end_date).to_list()

# Function to generate random data
def generate_data(num_records):
    data = []
    for _ in tqdm(range(num_records), desc="Generating records"):
        transaction_id = choice(transaction_ids)
        date = choice(date_range)
        time = fake.time()
        store_id = choice(store_ids)
        category, subcategories = choice(categories)
        subcategory = choice(subcategories)
        product_name = f"{subcategory} {randint(100, 999)}"
        quantity_sold = randint(1, 5)
        price_per_unit = round(uniform(1000, 100000), 2)
        total_sales = round(quantity_sold * price_per_unit, 2)
        discount = round(uniform(0, total_sales * 0.3), 2)
        payment_method = choice(payment_methods)
        customer_id = choice(customer_ids)
        age = randint(21, 84)
        gender = choice(['Male', 'Female'])
        income_level = choice(income_levels)
        location = choice(locations)
        loyalty_program = choice(loyalty_programs)
        purchase_frequency = choice(['High', 'Medium', 'Low'])

        data.append([
            transaction_id, date, time, store_id, product_name, category, subcategory, quantity_sold, 
            price_per_unit, total_sales, discount, payment_method, customer_id, age, gender, income_level, 
            location, loyalty_program, purchase_frequency
        ])
    
    return data

# Column names for the dataset
columns = [
    'Transaction ID', 'Date', 'Time', 'Store ID', 'Product Name', 'Category', 'Subcategory', 'Quantity Sold', 
    'Price per Unit', 'Total Sales', 'Discount', 'Payment Method', 'Customer ID', 'Age', 'Gender', 'Income Level', 
    'Location', 'Loyalty Program', 'Purchase Frequency'
]

# Generate the dataset
data = generate_data(num_records)
df = pd.DataFrame(data, columns=columns)

# Save the dataset to a CSV file
file_path = 'retail_sales_data.csv'
df.to_csv(file_path, index=False)

print(f"Dataset generated and saved to {file_path}")
