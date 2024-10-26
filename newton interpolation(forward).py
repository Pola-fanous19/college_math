x = symbols("x")
x0 = int(input("Enter X0: "))
h = int(input("Enter the difference between inputs: "))
n = int(input("Enter the number of records: "))
dYs = {"Ys0": []}
for z in range(n):
  y_input = input(f"enter the {z+1}'s output: ")
  dYs["Ys0"].append(simplify(y_input))


for i in range(1, n):
  dYs[f"Ys{i}"] = [dYs[f"Ys{i-1}"][x+1] - dYs[f"Ys{i-1}"][x] for x in range(n-i)]

p = symbols("p")
master_equation = dYs[f"Ys{0}"][0]

for i in range(1, n):

  term = dYs[f"Ys{i}"][0]
  for t in range(0, i):
     term *= (p-t)
  term /= factorial(i)
  print(term)
  master_equation += term

print(simplify(master_equation))
print(master_equation)
