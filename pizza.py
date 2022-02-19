# %%
def make_pizza(*toppings,size):
    """makeing pizza with requested topping"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
      print(f"- {topping}")