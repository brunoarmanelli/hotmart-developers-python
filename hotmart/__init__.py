import requests

class Hotmart:
	def __init__(self, id, secret, basic):
		self.id = id
		self.secret = secret
		self.basic = basic

	def get_token(self):
		method_url = 'https://api-sec-vlc.hotmart.com/security/oauth/token'
		headers = {'Authorization': 'Basic ' + self.basic}
		payload = {'grant_type': 'client_credentials', 'client_id' : self.id, 'client_secret': self.secret}

		try:
			r = requests.post(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data['access_token']
		except:
			return None
		
	def get_sales_history(self, max_results=None, page_token=None, product_id=None, start_date=None, 
			end_date=None, sales_source=None, transaction=None, buyer_name=None, 
			transaction_status=None, payment_type=None, offer_code=None):

		method_url = 'https://developers.hotmart.com/payments/api/v1/sales/history'
		headers = {'Authorization': 'Bearer ' + self.get_token()}
		payload = {}
		
		if product_id:
			payload['product_id'] = product_id
		if start_date:
			payload['start_date'] = start_date
		if end_date:
			payload['end_date'] = end_date
		if sales_source:
			payload['sales_source'] = sales_source
		if transaction:
			payload['transaction'] = transaction
		if transaction_status:
			payload['transaction_status'] = transaction_status
		if buyer_name:
			payload['buyer_name'] = buyer_name
		if payment_type:
			payload['payment_type'] = payment_type
		if offer_code:
			payload['offer_code'] = offer_code
		if page_token:
			payload['page_token'] = page_token
		if max_results:
			payload['max_results'] = max_results
		
		try:
			r = requests.get(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None

	def get_sales_summary(self, max_results=None, page_token=None, product_id=None, start_date=None, 
			end_date=None, sales_source=None, transaction=None, affiliate_name=None, 
			payment_type=None, offer_code=None):

		method_url = 'https://developers.hotmart.com/payments/api/v1/sales/summary'
		headers = {'Authorization': 'Bearer ' + self.get_token()}
		payload = {}
		
		if product_id:
			payload['product_id'] = product_id
		if start_date:
			payload['start_date'] = start_date
		if end_date:
			payload['end_date'] = end_date
		if sales_source:
			payload['sales_source'] = sales_source
		if transaction:
			payload['transaction'] = transaction
		if affiliate_name:
			payload['affiliate_name'] = affiliate_name
		if payment_type:
			payload['payment_type'] = payment_type
		if offer_code:
			payload['offer_code'] = offer_code
		if page_token:
			payload['page_token'] = page_token
		if max_results:
			payload['max_results'] = max_results
		
		try:
			r = requests.get(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None

	def get_sales_users(self, max_results=None, page_token=None, product_id=None, start_date=None, 
			end_date=None, sales_source=None, transaction=None, buyer_email=None, buyer_name=None, 
			affiliate_name=None, commission_as=None):

		method_url = 'https://developers.hotmart.com/payments/api/v1/sales/users'
		headers = {'Authorization': 'Bearer ' + self.get_token()}
		payload = {}
		
		if product_id:
			payload['product_id'] = product_id
		if start_date:
			payload['start_date'] = start_date
		if end_date:
			payload['end_date'] = end_date
		if sales_source:
			payload['sales_source'] = sales_source
		if transaction:
			payload['transaction'] = transaction
		if buyer_email:
			payload['buyer_email'] = buyer_email
		if buyer_name:
			payload['buyer_name'] = buyer_name
		if affiliate_name:
			payload['affiliate_name'] = affiliate_name
		if commission_as:
			payload['commission_as'] = commission_as
		if page_token:
			payload['page_token'] = page_token
		if max_results:
			payload['max_results'] = max_results
		
		try:
			r = requests.get(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None

	def get_sales_comissions(self, max_results=None, page_token=None, product_id=None, start_date=None, 
			end_date=None, transaction=None, commission_as=None):

		method_url = 'https://developers.hotmart.com/payments/api/v1/sales/commissions'
		headers = {'Authorization': 'Bearer ' + self.get_token()}
		payload = {}
		
		if product_id:
			payload['product_id'] = product_id
		if start_date:
			payload['start_date'] = start_date
		if end_date:
			payload['end_date'] = end_date
		if transaction:
			payload['transaction'] = transaction
		if commission_as:
			payload['commission_as'] = commission_as
		if page_token:
			payload['page_token'] = page_token
		if max_results:
			payload['max_results'] = max_results
		
		try:
			r = requests.get(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None

	def get_sales_price_details(self, max_results=None, page_token=None, product_id=None, start_date=None, 
			end_date=None, transaction=None, transaction_status=None, payment_type=None):

		method_url = 'https://developers.hotmart.com/payments/api/v1/sales/price/details'
		headers = {'Authorization': 'Bearer ' + self.get_token()}
		payload = {}
		
		if product_id:
			payload['product_id'] = product_id
		if start_date:
			payload['start_date'] = start_date
		if end_date:
			payload['end_date'] = end_date
		if transaction:
			payload['transaction'] = transaction
		if transaction_status:
			payload['transaction_status'] = transaction_status
		if payment_type:
			payload['payment_type'] = payment_type
		if page_token:
			payload['page_token'] = page_token
		if max_results:
			payload['max_results'] = max_results
		
		try:
			r = requests.get(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None