number_of_tickets = 100
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket

print(total_price)

if total_price >= 1500:
    total_price = total_price * 0.8
    print ("Získáváte slevu 20%")
elif total_price >= 500: 
    total_price = total_price * 0.9
    print ("Získáváte slevu 10%")
else: 
    print("Bohužel nezískáváte slevu")


print (f"Celková cena nákupu je {int(total_price)} Kč.")