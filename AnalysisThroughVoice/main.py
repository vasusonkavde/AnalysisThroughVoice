from flask import Flask, request, jsonify, render_template
import difflib
import pandas as pd

app = Flask(__name__)

method_names = [
    "sales_summary", "total_sales_by_year", "total_profit_by_year", "sales_by_country", "profit_by_country",
    "sales_by_product_category", "profit_by_product_category", "average_order_quantity_by_age_group",
    "average_unit_cost_by_age_group", "average_unit_price_by_age_group", "gender_distribution", "sales_by_state",
    "profit_by_state", "sales_by_age_group", "profit_by_age_group", "average_profit_margin_by_country",
    "total_revenue_by_month_year", "total_profit_by_month_year", "total_revenue_profit_by_product",
    "average_revenue_profit_per_order", "top_performing_products_by_revenue", "top_performing_products_by_profit",
    "customer_age_distribution", "revenue_profit_by_gender", "revenue_profit_by_age_group_gender",
    "profit_margin_by_product_category"
]

class SalesDataAnalysis:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def sales_summary(self):
        summary = self.df.describe()
        return summary.to_string()

    def total_sales_by_year(self):
        total_sales = self.df.groupby('Year')['Revenue'].sum()
        return total_sales.to_string()

    def total_profit_by_year(self):
        total_profit = self.df.groupby('Year')['Profit'].sum()
        return total_profit.to_string()

    def sales_by_country(self):
        sales_country = self.df.groupby('Country')['Revenue'].sum()
        return sales_country.to_string()

    def profit_by_country(self):
        profit_country = self.df.groupby('Country')['Profit'].sum()
        return profit_country.to_string()

    def sales_by_product_category(self):
        sales_product_category = self.df.groupby('Product_Category')['Revenue'].sum()
        return sales_product_category.to_string()

    def profit_by_product_category(self):
        profit_product_category = self.df.groupby('Product_Category')['Profit'].sum()
        return profit_product_category.to_string()

    def average_order_quantity_by_age_group(self):
        avg_order_quantity = self.df.groupby('Age_Group')['Order_Quantity'].mean()
        return avg_order_quantity.to_string()

    def average_unit_cost_by_age_group(self):
        avg_unit_cost = self.df.groupby('Age_Group')['Unit_Cost'].mean()
        return avg_unit_cost.to_string()

    def average_unit_price_by_age_group(self):
        avg_unit_price = self.df.groupby('Age_Group')['Unit_Price'].mean()
        return avg_unit_price.to_string()

    def gender_distribution(self):
        gender_dist = self.df['Customer_Gender'].value_counts()
        return gender_dist.to_string()

    def sales_by_state(self):
        sales_state = self.df.groupby('State')['Revenue'].sum()
        return sales_state.to_string()

    def profit_by_state(self):
        profit_state = self.df.groupby('State')['Profit'].sum()
        return profit_state.to_string()

    def sales_by_age_group(self):
        sales_age_group = self.df.groupby('Age_Group')['Revenue'].sum()
        return sales_age_group.to_string()

    def profit_by_age_group(self):
        profit_age_group = self.df.groupby('Age_Group')['Profit'].sum()
        return profit_age_group.to_string()

    def average_profit_margin_by_country(self):
        self.df['Profit_Margin'] = self.df['Profit'] / self.df['Revenue']
        avg_profit_margin = self.df.groupby('Country')['Profit_Margin'].mean()
        return avg_profit_margin.to_string()

    def total_revenue_by_month_year(self):
        total_revenue = self.df.groupby(['Year', 'Month'])['Revenue'].sum()
        return total_revenue.to_string()

    def total_profit_by_month_year(self):
        total_profit = self.df.groupby(['Year', 'Month'])['Profit'].sum()
        return total_profit.to_string()

    def total_revenue_profit_by_product(self):
        revenue_profit_product = self.df.groupby('Product')[['Revenue', 'Profit']].sum()
        return revenue_profit_product.to_string()

    def average_revenue_profit_per_order(self):
        avg_revenue = self.df['Revenue'].mean()
        avg_profit = self.df['Profit'].mean()
        return f"Average Revenue: {avg_revenue}\nAverage Profit: {avg_profit}"

    def top_performing_products_by_revenue(self, top_n=5):
        top_products = self.df.groupby('Product')['Revenue'].sum().nlargest(top_n)
        return top_products.to_string()

    def top_performing_products_by_profit(self, top_n=5):
        top_products = self.df.groupby('Product')['Profit'].sum().nlargest(top_n)
        return top_products.to_string()

    def customer_age_distribution(self):
        age_distribution = self.df['Customer_Age'].value_counts().sort_index()
        return age_distribution.to_string()

    def revenue_profit_by_gender(self):
        revenue_profit_gender = self.df.groupby('Customer_Gender')[['Revenue', 'Profit']].sum()
        return revenue_profit_gender.to_string()

    def revenue_profit_by_age_group_gender(self):
        revenue_profit_age_gender = self.df.groupby(['Age_Group', 'Customer_Gender'])[['Revenue', 'Profit']].sum()
        return revenue_profit_age_gender.to_string()

    def profit_margin_by_product_category(self):
        self.df['Profit_Margin'] = self.df['Profit'] / self.df['Revenue']
        profit_margin = self.df.groupby('Product_Category')['Profit_Margin'].mean()
        return profit_margin.to_string()

@app.route('/')
def index():
    return render_template('index.html', method_names=method_names)

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.get_json()
    command = data.get('command', '')

    closest_matches = difflib.get_close_matches(command, method_names, n=1, cutoff=0.0)
    if closest_matches:
        method_to_call = closest_matches[0]

        sales_data_analysis = SalesDataAnalysis('sales_data.csv')
        method = getattr(sales_data_analysis, method_to_call)
        result = method()

        return jsonify({'method': method_to_call, 'result': result})
    else:
        return jsonify({'method': 'No match found', 'result': ''})

if __name__ == '__main__':
    app.run(debug=True)
