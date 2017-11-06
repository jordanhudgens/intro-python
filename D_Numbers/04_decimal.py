from decimal import Decimal
import decimal

total = Decimal(5010.42)
sale_commission = Decimal(0.3) * total
penny = Decimal('0.01')

print("Standard Decimal Computation")
print(sale_commission)

print("--------")

print("Quantize Decimal Computation")
print(sale_commission.quantize(penny))

print("--------")

print("Quantize Decimal Computation Rounded Up")
print(sale_commission.quantize(penny, decimal.ROUND_UP))

print("--------")

print("Quantize Decimal Computation Rounded Down")
print(sale_commission.quantize(penny, decimal.ROUND_DOWN))
