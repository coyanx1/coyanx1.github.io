print("What plants are right for you?")
x = input("Do you live in a wet or dry climate?")
if x == "dry": #dry 
  y = input("Do you want to be able to eat the plant?") 
  if y == "yes": #edible
    e = input("Do you want the plant to have medicinal purposes?")
    if e == "yes":
      print("You should grow Turmeric")
    elif e == "no":
      q = input("Do you want the plant to be a Tree, Shrub, or Root?")
      if q == "tree":
        print("You should grow Mountain Apple, or Guava")
      elif q == "shrub":
        print("You should grow Lilikoi, Tabasco Pepper, or Pineapple")
      elif q == "root":
        print("You should grow Eggplant")
  elif y == "no": #inedible
    e = input("Do you want the plant to have medicinal purposes?")
    if e == "yes":
      q = input("Do you want the plant to be a tree, or root?")
      if q == "tree":
        print("You should grow Plumeria")
      elif q == "root":
        print("You should grow Aloe Vera")
    elif e == "no":
      q = input("Do you want the plant to be a tree, or shrub?")
      if q == "tree":
        print("You should grow Crown Flower")
      elif q == "shrub":
        print("You should grow Arabian Jasmine, Tahitian Gardenia, ")

if x == "wet": #wet
  y = input("Do you want to be able to eat the plant?") 
  if y == "yes": #edible
    e = input("Do you want the plant to have medicinal purposes?")
    if e == "yes":
      print("You should grow Red Ginger, Bitter Ginger")
    elif e == "no":
      q = input("Do you want the plant to be a tree, or root?")
      if q == "tree":
        print("You should grow Breadfruit, Ti-Leaf, Banana, or Papaya")
      elif q == "root":
        print("You should grow Green Onions, or Taro")
  elif y == "no": #inedible
    q = input("Do you want the plant to be a tree, or root?")
    if q == "tree":
      print("You should grow Hibiscus, or Pua-kenikeni")
    elif q == "root":
      print("You should grow White Ginger, Laceleaf, Heliconias, or Bird of Paradise")
