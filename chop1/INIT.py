# So the user typed something in the INIT state.
# Bot should present with first level menu choices.
# Here's today's menu:
# Sandwiches, Espresso Drinks, Iced Coffee, Other Drinks, Other Food.

# config in this bot is the menu items
state = 'INIT' # Start State
items = []
for item in config['items']:
    #items.append(list(item)[0])
    title = list(item)[0]
    payload = title.upper().replace(' ','_')
    items.append(create_button(title, payload))

cards = [create_card('Welcome to Chop Shop' , '' , 'Check out our menu:' , items)]
msg = create_card_message(sender_id, cards)
send_card_message(msg)

state = 'WAIT_FOR_CAT' # End State
