import pandas as pd
import numpy as np
from random import randint, choice, uniform
from datetime import datetime, timedelta
from faker import Faker
from tqdm import tqdm

# Initialize Faker to generate random data
fake = Faker()

# Define the parameters for the dataset
start_date = '2020-01-01'
end_date = '2024-07-18'
num_records = 9020  # Specify the total number of records you want to generate

# Generating IDs
transaction_ids = [f'T00{i+1}' for i in range(num_records)]
customer_ids = [f'C00{i+1}' for i in range(850)]
store_ids = ['S001', 'S002', 'S003', 'S004', 'S005']
product_ids = [f'P00{i+1}' for i in range(380)]
supplier_ids = [f'SUP00{i+1}' for i in range(65)]

# Categories and Subcategories
categories = [
    ('Electronics', ['Laptops', 'Smartphones', 'Headphones', 'Gaming Consoles', 'Digital Cameras', 'Printers', 'Routers', 'Wearable Devices', 'Home Assistants', 'Bluetooth Speakers']),
    ('Home Appliances', ['Washing Machines', 'Refrigerators', 'Microwave Ovens', 'Vacuum Cleaners', 'Coffee Makers', 'Dishwashers', 'Electric Kettles', 'Air Purifiers', 'Water Heaters', 'Blenders']),
    ('Fashion and Accessories', ['Shoes', 'Handbags', 'Sunglasses', 'Watches', 'Jackets', 'Jewelry', 'Belts', 'Hats', 'Scarves', 'Gloves']),
    ('Health and Wellness', ['Vitamins', 'Supplements', 'Skincare Products', 'Haircare Products', 'Fitness Equipment', 'Yoga Accessories', 'Massage Devices', 'Health Monitors', 'Protein Powders', 'Essential Oils']),
    ('Books and Media', ['Fiction Books', 'Non-Fiction Books', 'eBooks', 'Audiobooks', 'Magazines', 'CDs', 'DVDs', 'Vinyl Records', 'Comic Books', 'Graphic Novels']),
    ('Sports and Outdoors', ['Bicycles', 'Treadmills', 'Yoga Mats', 'Dumbbells', 'Camping Gear', 'Running Shoes', 'Sports Apparel', 'Fitness Trackers', 'Water Bottles', 'Hiking Boots']),
    ('Toys and Games', ['Board Games', 'Puzzles', 'Action Figures', 'Dolls', 'LEGO Sets', 'RC Cars', 'Video Games', 'Stuffed Animals', 'Educational Toys', 'Building Blocks']),
    ('Automotive', ['Car Accessories', 'Motorcycle Gear', 'Car Electronics', 'Tires', 'Car Care Products', 'Motorcycle Helmets', 'Car Tools', 'Car Seats', 'Motorcycle Jackets', 'GPS Devices']),
    ('Home and Garden', ['Furniture', 'Garden Tools', 'Outdoor Furniture', 'Indoor Plants', 'Gardening Supplies', 'Home Decor', 'Lighting', 'Bedding', 'Kitchen Tools', 'BBQ Grills'])
]

# Payment methods, loyalty programs, locations, and income levels
payment_methods = ['Cash', 'Credit Card', 'Debit Card', 'Mobile Payment']
loyalty_programs = ['Yes', 'No']
locations = ['Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Hyderabad']
income_levels = ['<25,000', '25,000-49,999', '50,000-74,999', '75,000-99,999', '100,000+']

# Generate random dates between start_date and end_date
date_range = pd.date_range(start=start_date, end=end_date).to_list()

# Function to generate customers data
def generate_customers(num_customers):
    customers = []
    for i in range(num_customers):
        customer_id = customer_ids[i]
        age = randint(21, 84)
        gender = choice(['Male', 'Female'])
        name = fake.name()
        income_level = choice(income_levels)
        location = choice(locations)
        loyalty_program = choice(loyalty_programs)
        purchase_frequency = choice(['High', 'Medium', 'Low'])
        mail_id = fake.email()
        
        customers.append([customer_id, age, gender, name, income_level, location, loyalty_program, purchase_frequency, mail_id])
    
    return customers

# Function to generate store data
def generate_stores():
    stores = []
    for store_id in store_ids:
        store_location = choice(locations)
        store_size = choice(['Small', 'Medium', 'Large'])
        store_manager = fake.name()
        opening_date = fake.date_between_dates(date_start=pd.to_datetime('2010-01-01'), date_end=pd.to_datetime('2023-12-31'))
        
        stores.append([store_id, store_location, store_size, store_manager, opening_date])
    
    return stores

# Function to generate product data
def generate_products(num_products):
    products = []
    for i in range(num_products):
        product_id = product_ids[i]
        category, subcategories = choice(categories)
        subcategory = choice(subcategories)
        product_name = f"{subcategory} {randint(100, 999)}"
        supplier_id = choice(supplier_ids)
        cost_price = round(uniform(500, 50000), 2)
        retail_price = round(cost_price * uniform(1.1, 2.0), 2)
        
        products.append([product_id, product_name, category, subcategory, supplier_id, cost_price, retail_price])
    
    return products

# Function to generate a random time between 10:00 AM and 10:00 PM
def generate_time():
    start = datetime.strptime("10:00 AM", "%I:%M %p")
    end = datetime.strptime("10:00 PM", "%I:%M %p")
    random_time = start + (end - start) * uniform(0, 1)
    return random_time.strftime("%I:%M %p")

# Function to generate sales data
def generate_sales(num_records):
    sales = []
    for _ in tqdm(range(num_records), desc="Generating records"):
        transaction_id = choice(transaction_ids)
        date = choice(date_range)
        time = generate_time()
        store_id = choice(store_ids)
        product_id = choice(product_ids)
        quantity_sold = randint(1, 5)
        price_per_unit = round(uniform(1000, 100000), 2)
        total_sales = round(quantity_sold * price_per_unit, 2)
        discount = round(uniform(0, total_sales * 0.3), 2)
        payment_method = choice(payment_methods)
        customer_id = choice(customer_ids)
        
        sales.append([transaction_id, date, time, store_id, product_id, quantity_sold, price_per_unit, total_sales, discount, payment_method, customer_id])
    
    return sales

# Function to generate date data
def generate_date_data(date_range):
    date_data = []
    for date in date_range:
        year = date.year
        month = date.month
        day = date.day
        day_of_week = date.strftime('%A')
        quarter = (date.month - 1) // 3 + 1
        week_of_year = date.isocalendar()[1]
        is_weekend = date.weekday() > 4  # 5 and 6 correspond to Saturday and Sunday

        date_data.append([date, year, month, day, day_of_week, quarter, week_of_year, is_weekend])
    
    return date_data

# Column names for the datasets
customer_columns = ['Customer ID', 'Age', 'Gender', 'Name', 'Income Level', 'Location', 'Loyalty Program', 'Purchase Frequency', 'Mail ID']
store_columns = ['Store ID', 'Store Location', 'Store Size', 'Store Manager', 'Opening Date']
product_columns = ['Product ID', 'Product Name', 'Category', 'Subcategory', 'Supplier ID', 'Cost Price', 'Retail Price']
sales_columns = ['Transaction ID', 'Date', 'Time', 'Store ID', 'Product ID', 'Quantity Sold', 'Price per Unit', 'Total Sales', 'Discount', 'Payment Method', 'Customer ID']
date_columns = ['Date', 'Year', 'Month', 'Day', 'Day of Week', 'Quarter', 'Week of Year', 'Is Weekend']

# Generate the datasets
customers = generate_customers(680)
stores = generate_stores()
products = generate_products(300)
sales = generate_sales(num_records)
date_data = generate_date_data(date_range)

# Convert to DataFrames
df_customers = pd.DataFrame(customers, columns=customer_columns)
df_stores = pd.DataFrame(stores, columns=store_columns)
df_products = pd.DataFrame(products, columns=product_columns)
df_sales = pd.DataFrame(sales, columns=sales_columns)
df_date = pd.DataFrame(date_data, columns=date_columns)

# Save the datasets to CSV files
df_customers.to_csv('customers.csv', index=False)
df_stores.to_csv('store_details.csv', index=False)
df_products.to_csv('products_data.csv', index=False)
df_sales.to_csv('retail_sales_data.csv', index=False)
df_date.to_csv('date.csv', index=False)

print(f"Datasets generated and saved to CSV files successfully.")
