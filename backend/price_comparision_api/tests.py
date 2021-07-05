from django.test import TestCase
import pandas as pd
import requests

# Create your tests here.




def test():
    df = pd.read_csv(r"G:\\Gautam_projects\\Gautam_pycharm\scrapper\\Price_comparision\\new_price_comparision\\price_comparision.csv")
    df.at[:, 'category'] = 'Electronics | Phones'
    data = df.iloc[0]
    data = data.to_dict()
    payload = {
        'category': data['category'],
        'title': data['product_title'],
        'brand': data['product_brand'],
        'model': data['product_model'],
        'rom': data['ROM'],
        'ram': data['RAM'],
        'color': data['product_color'],
        'description': data['description'],
        'specifications': str(data['specifications']),
        'images': data['image_url'],
        'product_link': data['product_link'],
        'primary_matched_links': str(data['primary_match_data']),
        'secondary_matched_links': str(data['secondary_match_data'])
    }
    
    print('payload :', payload)

    # res = requests.post('http://localhost:8000/view-product-list/', data=payload)
    # print('res :', res.content)

test()

