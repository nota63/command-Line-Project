import pyautogui
from PIL import Image
import random
import string
import pandas as pd
from colorama import Fore, Style
import time
from plyer import notification
import datetime

stocks = [350, 566, 680]
amount_won = [5000, 100, 2000, 3000, 4000, 400, 300, 200, 101, 50]


# INITIALIZE GAME

class Game:
    def __init__(self):
        self.balance = 5000
        self.bank = 0
        self.history = []
        self.shopped_items = []

    # GAME FUNCTION
    def play_game(self):
        input('are you sure!: press enter to proceed!')
        info = 'there are stocks and you have to put price of stocks to trade!'
        print(info.upper())

        try:
            data = {"STOCKS": ['NIFTY 50', 'PYTHON', 'JAVA'],
                    'PRICE': [350, 566, 680, ]
                    }
            ui = pd.DataFrame(data)
            print(ui)
            if self.balance >= 100:
                user = int(input('Enter stock price to trade that stock:'))
                upipin = int(input('Enter Upi Pin To make payment:'))
                if upipin == 1234:

                    print(f"you have purchased a stock of INR:'{user}':{data}")
                    input('press enter to trade:')
                    stock = random.choice(stocks)
                    win_amount = random.choice(amount_won)
                    if user == stock:
                        self.balance += win_amount
                        self.balance += self.bank
                        self.history.append(user)
                        print('trading started... you will be notified soon..')
                        time.sleep(5)
                        notification.notify(
                            title='Your Trade-{}'.format(datetime.date.today()),
                            message='Trading accomplished check your terminal for results',
                            timeout=5
                        )
                        print(f"Congratulations!\n your trade was up and you have won rupees {win_amount}")
                    else:
                        self.balance -= stock
                        print(f'sorry your trade was gone down and you lost INR:"{stock}"')
                else:
                    print('wrong upi p9in entered!')

            else:
                print('can not start! insufficient balance')
        except ValueError:
            print('valueError')
        except IndexError:
            print('indexError')
        finally:
            print('thanks for playing with us.')

    # FOR GET TRENDING STOCKS
    def get_trending_stocks_info(self):
        t = time.localtime(time.time())
        localtime = time.asctime(t)
        view = time.asctime(t)
        print(f'Getting Info from stockmarket as On: "{view}".... ')
        time.sleep(5)
        print(Fore.LIGHTBLUE_EX + 'Done✅')
        print('<<<<trending Stocks>>>>')
        trending_stocks = [
            {'Symbol': 'AAPL', 'Company': 'Apple Inc.', 'Price': 150.00},
            {'Symbol': 'TSLA', 'Company': 'Tesla Inc.', 'Price': 700.00},
            {'Symbol': 'AMZN', 'Company': 'Amazon.com Inc.', 'Price': 3300.00},
            {'Symbol': 'GOOGL', 'Company': 'Alphabet Inc.', 'Price': 2800.00},
            {'Symbol': 'MSFT', 'Company': 'Microsoft Corporation', 'Price': 290.00},
            {'Symbol': 'FB', 'Company': 'Meta Platforms Inc.', 'Price': 340.00},
            {'Symbol': 'NFLX', 'Company': 'Netflix Inc.', 'Price': 590.00},
            {'Symbol': 'NVDA', 'Company': 'NVIDIA Corporation', 'Price': 220.00},
            {'Symbol': 'PYPL', 'Company': 'PayPal Holdings Inc.', 'Price': 190.00},
            {'Symbol': 'INTC', 'Company': 'Intel Corporation', 'Price': 50.00}
        ]
        print(trending_stocks)

    # CHECK BALANCE
    def check_balance_table_ac(self):
        # while True:
        try:
            password = int(input('enter your upi pin:'))
            if password == 1234:
                print('fetching bank balance...')
                time.sleep(5)
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 'bank Balance fetched successfully!')
                print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f' Available Balance:{self.balance}')
                input('press enter to take screenshot:')
                shot = pyautogui.screenshot()
                shot.save('balance.png')
                image = Image.open('balance.png')
                image.show()
            else:
                print('wrong upi pin entered!')
        except ValueError:
            print('valueError')
        except IndexError:
            print('indexError')

    # FOR PRIMARY BANK ACCOUNT
    def check_balance_bank_ac(self):
        # while True:
        try:
            password = int(input('enter your upi pin:'))
            if password == 1234:
                print('fetching bank balance...')
                time.sleep(5)
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 'bank Balance fetched successfully!')
                print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f' Available Balance:{self.bank}')
                input('press enter to take screenshot:')
                shot = pyautogui.screenshot()
                shot.save('balance.png')
                image = Image.open('balance.png')
                image.show()
            else:
                print('wrong upi pin entered!')
        except ValueError:
            print('valueError')
        except IndexError:
            print('indexError')

    # FOR VIEW TRANSACTION HISTORY
    def view_history(self):
        print('your transaction history of that game will appear here>>')
        passw = int(input('enter your password:'))
        if passw == 1234:
            print('preparing for balance')
            time.sleep(5)
            for index, money in enumerate(self.history):
                print("your transaction history/ amount invested")
                print(Fore.LIGHTGREEN_EX + f"{index + 1}: '{money}' ")
                print('want o take screenshot press enter:')
                shot = pyautogui.screenshot()
                shot.save('ss.png')
                image = Image.open('ss.png')
                image.show()
        else:
            print('wrong password entered:')

    #     money deposit into account - table
    def deposit_money_table(self):
        money = int(input('enter amount to deposit:'))
        upi = int(input('enter upi pin :'))
        if upi == 1234:
            print(Fore.LIGHTGREEN_EX + f'Initiating Transaction For Rupees: "{money}"... ')
            time.sleep(5)
            self.balance += money
            print('Transaction Completed')
            notification.notify(
                title='Transaction-{}'.format(datetime.date.today()),
                message=f'Transaction Of Rupees :"{money}" Has Benn completed\n And Your Current Balance is : "{self.balance}"',
                timeout=5

            )
        else:
            print('Wrong UPI pin entered!')

    # FOR SHOPPING
    def shopping(self):
        while True:
            try:
                if self.balance >= 500:
                    print('Our Inventory')
                    items = {
                        'Phones': ['Redmi', 'realme', 'infinix', 'oppo', 'vivo', 'techno'],
                        'Laptops': ['lenovo', 'acer', 'infinix', 'ultimus', 'Dell'],
                        'Price': [10000, 12000, 15000, 8000, 29000, 19000, 45000, 20000, 23000, 10000, 28000]
                    }
                    uv = pd.DataFrame(items)
                    print(uv)

                    price_index = int(input('Enter the index of the item to purchase: '))
                    if price_index < 0 or price_index >= len(items['Price']):
                        print('Invalid item index. Please select a valid item.')
                        continue

                    item_name = items['Phones'][price_index] if price_index < 6 else items['Laptops'][price_index - 6]
                    item_price = items['Price'][price_index]

                    if item_price > self.balance:
                        print('Insufficient funds! Please refill your account and try again.')
                    else:
                        self.balance -= item_price
                        upi_pin = int(input('Enter UPI pin to pay: '))
                        if upi_pin == 1234:
                            print(Fore.LIGHTMAGENTA_EX + f'Purchasing {item_name} for {item_price} rupees.')
                            time.sleep(5)
                            self.shopped_items.append(item_name)
                            notification.notify(
                                title='Shopping-{}'.format(datetime.date.today()),
                                message=f'Congratulations!\n{item_name} purchased successfully for {item_price} rupees.\nYour current balance is: INR {self.balance}',
                                timeout=5
                            )
                            input('Press enter to take a screenshot: ')
                            shot1 = pyautogui.screenshot()
                            shot1.save('shop.png')
                            image = Image.open('shop.png')
                            image.show()
                        else:
                            print('Wrong UPI pin entered!')
                else:
                    print('Insufficient funds!')
            except ValueError:
                print('ValueError occurred. Please enter a valid input.')
            except IndexError:
                print('IndexError occurred. Please enter a valid index.')

    # FOR VIEW CART
    def view_shopped_items(self):
        if self.shopped_items:
            input('Press Enter To view:')
            print('Fetching your Details.....(it may take 5 seconds)')
            time.sleep(5)
            for index, item1 in enumerate(self.shopped_items):
                print('Your Cart.')
                print(f"{index + 1}\n {item1}")
        else:
            print('your Cart Is An Empty')

    # FOR SET ALARM
    def set_alarm(self):
        print('you can set alarm in form of seconds!')
        alarm = int(input('Enter Seconds..:'))
        t = time.localtime(time.time())
        localtime = time.asctime(t)
        set = time.asctime(t)
        print(f'Alarm set as on>> :"{set}" for :"{alarm}"')
        time.sleep(alarm)
        notification.notify(
            title='alarm-{}'.format(datetime.date.today()),
            message='Wake Up Please......',
            timeout=5
        )

    # FOR GENERATE PASSWORD
    import random
    import string
    import time

    def generate_password(self, length=8):  # Added self parameter for instance method
        print('Generating password. Please wait...')
        time.sleep(1)  # Reduced sleep time for quicker feedback
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated password: '{password}'")
        print(password)

    # instance


def main():
    game = Game()
    while True:
        try:
            print(' MENU.....\n 1.play_game\n'
                  '2.view_table Ac_ balance\n'
                  '3.view_primary bank balance\n'
                  '4.view_transaction_history\n'
                  '5.get_trending_stocks_info\n'
                  '6.deposit_money_table_ac\n'
                  '7.shopping\n'
                  '8.view_shopped_items\n'
                  '9.set_alarm\n'
                  '10.generate_password\n'
                  '11.Game Documentation\n'
                  '12.Quite'
                  )
            me = int(input('Fill An Index From Menu To Start:'))

            if me == 1:
                game.play_game()

            elif me == 2:
                game.check_balance_table_ac()

            elif me == 3:
                game.check_balance_bank_ac()

            elif me == 4:
                game.view_history()

            elif me == 5:
                game.get_trending_stocks_info()

            elif me == 6:
                game.deposit_money_table()

            elif me == 7:
                game.shopping()

            elif me == 8:
                game.view_shopped_items()

            elif me == 9:
                game.set_alarm()

            elif me == 10:
                game.generate_password()

            elif me == 11:
                print(help(Game))


            elif me == 12:
                print('Quiting.....')
                time.sleep(3)
                print('Exited From The Game!')
                break

        # except ValueError:
        #     print('ValueError')

        except IndexError:
            print('IndexError')

        except RecursionError:
            print('Recursion Error')

        except UnicodeEncodeError:
            print('Unicode Error!')

        except ConnectionError:
            print('Connection Error!')

        except ChildProcessError:
            print('ChildProcess Error!')

        except DeprecationWarning:
            print('depreciation Warning!')

        except NotADirectoryError:
            print('notDirectoryError!')

        except WindowsError:
            print('WindowsError!')


# Start the app

if __name__ == '__main__':
    main()
