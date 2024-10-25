n = int(input("Enter the number of records"))
x = symbols("x")
Xs = []
Ys = []
for z in range(n):
  x_input = input(f"enter the {z+1}'s input: ")
  y_input = input(f"enter the {z+1}'s output: ")
  Xs.append(simplify(x_input))
  Ys.append(simplify(y_input))

master_equation = 0

helper = 1
for u in range(len(Xs)):
  helper *= (x - Xs[u])
  

for i in range(len(Xs)):
  helper_temp = helper / (x - Xs[i])
  term = Ys[i] * helper_temp / helper_temp.subs(x, Xs[i])
  print(f"the {i+1}'s term: ")
  print(term)
  master_equation += term

print(simplify(master_equation))
