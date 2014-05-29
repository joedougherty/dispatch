import readline
import sys

################################################################
# Each function here corresponds to a key in the COMMANDS dict #
################################################################
def help(args):
    CMDS = COMMANDS.keys()
    CMDS.sort()
    for c in CMDS:
        print(c + '  \t\t|  ' + COMMANDS.get(c)['help'])

def disconnect(args):
    if args == []:
        print('Please specify a data source to disconnect from.')
        return False

    source = args[0]
    print('Disconnecting from data source: ' + source + '...')

def joke(args):
    print('I know zero good jokes. Oh no!')

def exit(args):
    print('Goodbye!')
    sys.exit(0)

def go(args):
    valid_directions = ['north', 'south', 'east', 'west']

    if args == []:
        print('Provide a valid direction to move in.')
        return False

    direction = args[0]
    if direction in valid_directions:
        print('You moved ' + direction + '.')    
    else:
        print('Provide a valid direction to move in.')

def two(args):
    if args == []:
        print('Please provide two args to \'two\'.')
        return False

    try:
        arg1 = args[0]
        arg2 = args[1]
        print(arg1, arg2)
    except IndexError:
        print('"two" requires two args.')

COMMANDS = {'disc': 
                {'help': 'Disconnect from a data source',
                 'command': disconnect},
            'joke':
                {'help': 'Tell a joke!',
                 'command': joke},
            'help': 
                {'help': 'Prints a help message',
                 'command': help},
            'exit':
                {'help': 'Exit the shell',
                 'command': exit},
            'go':
                {'help': 'Move in a cardinal direction.',
                 'command': go},
            'two':
                {'help': 'I take two arguments.',
                 'command': two},
           }

def complete(text, state):
    """ 
    This example from: 
    http://stackoverflow.com/questions/5637124/tab-completion-in-pythons-raw-input

    See https://docs.python.org/2/library/readline.html#readline.set_completer 
    for further information.
    """
    cmds = COMMANDS.keys()
    cmds.sort()

    for cmd in cmds:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1

def main():
    readline.parse_and_bind("tab: complete")
    readline.set_completer(complete)

    # Super simple REPL
    # Inspired by http://norvig.com/lis.py (see "def repl(prompt='lis.py> '):")
    while True:
        data = raw_input('> ')

        if data == '': pass

        tokens = data.split(' ')
        user_command = tokens[0]
            
        if user_command in COMMANDS:
            # Call the desired function by its key in COMMANDS
            # Pass the full list of tokens
            # Each function will decide how to handle the additional tokens (if any)
            COMMANDS.get(user_command)['command'](tokens[1:])
        else:
            print('I do not know how to ' + user_command + '.')

def greet():
    print("Hello again!")
    print("'help' to see available commands.")

if __name__ == '__main__':
    greet()
    main()
