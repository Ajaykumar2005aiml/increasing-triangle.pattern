R=5
for i in range(1,R+1):
  for j in range(1,i+1):
    if j==i:
      print("*",end="")
    else:
      print("*",end=" ")
  print()
