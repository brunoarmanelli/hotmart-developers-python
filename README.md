
# Unoffical Hotmart Developers Python Module

Hotmart Developers requests made easy.

### Usage
  
````python
import hotmart

hotmart = hotmart.Hotmart(
    id='YOUR_ID',
    secret='YOUR_SECRET',
    basic='YOUR_KEY'
)
````

and then

````python
response = hotmart.get_sales()
print(response)
````
