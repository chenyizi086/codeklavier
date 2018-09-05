"""Mapping.py

Contains the classes ``Mapping_HelloWorld``, ``Mapping_HelloWorld_NKK`` and
``Mapping_Motippets``. These class deal with the mapping of the (midi) keys to
chars, strings and commands.

TODO: make a single base class and subclass the different versions from that
class.
"""
import time
from pynput.keyboard import Key, Controller
import socket
from pythonosc import udp_client
import configparser

display1 = 1111
display2 = 2222
display3 = 3333
display4 = 4444
display5 = 5555


class Mapping_Motippets:
    """Mapping for the Motippets prototype.

       Includes Hello World mappings for the Hybrid prototype
    """
    def __init__(self, debug=True):
        if debug:
            print("## Using the Motippets mapping ##")

        #Read config and settings
        config = configparser.ConfigParser(delimiters=(':'), comment_prefixes=('#'))
        config.read('default_setup.ini')

        try:
            self.__snippet1 = config['snippets'].get('snippet1')
            self.__snippet2 = config['snippets'].get('snippet2')

            self.__mini_snippet_hi_1 = config['snippets'].get('mini_snippet_hi_1')
            self.__mini_unmap_hi_2 = config['snippets'].get('mini_unmap_hi_2')

            self.__mini_snippet_hi_2 = config['snippets'].get('mini_snippet_hi_2')
            self.__mini_unmap_hi_1 = config['snippets'].get('mini_unmap_hi_1')

            self.__mini_snippet_mid_1 = config['snippets'].get('mini_snippet_mid_1')
            self.__mini_unmap_mid_2 = config['snippets'].get('mini_unmap_mid_2')

            self.__mini_snippet_mid_2 = config['snippets'].get('mini_snippet_mid_2')
            self.__mini_snippet_mid_2b = config['snippets'].get('mini_snippet_mid_2') # check?
            self.__mini_unmap_mid_1 = config['snippets'].get('mini_unmap_mid_1')

            self.__mini_snippet_low_1 = config['snippets'].get('mini_snippet_low_1')
            self.__mini_snippet_low_1_amp = config['snippets'].get('mini_snippet_low_1_amp')
            self.__mini_unmap_low_1 = config['snippets'].get('mini_unmap_low_1')
            self.__mini_unmap_low_2 = config['snippets'].get('mini_unmap_low_2')
            self.__mini_unmap_low_3 = config['snippets'].get('mini_unmap_low_3')

            self.__mini_snippet_low_2 = config['snippets'].get('mini_snippet_low_2')
            self.__mini_snippet_low_1_amp = config['snippets'].get('mini_snippet_low_1_amp')
            self.__mini_unmap_low_1 = config['snippets'].get('mini_unmap_low_1')
            self.__mini_unmap_low_2 = config['snippets'].get('mini_unmap_low_2')
            self.__mini_unmap_low_3 = config['snippets'].get('mini_unmap_low_3')

        except KeyError:
            raise LookupError('Missing snippets in the config file.')

        self.__keyboard = Controller()
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._osc = udp_client.SimpleUDPClient('127.0.0.1', 57120) #standard supercollider OSC listening port

    def evaluateSC(self, what):
        """Evaluate the SuperCollider command 'what'

        :param string what: the command that should be evaluated
        """
        if what == 'play':
            with self.__keyboard.pressed(Key.cmd):
                self.__keyboard.press(Key.right)
                self.__keyboard.release(Key.right)
            time.sleep(0.01)
            self.__keyboard.type('.play')
            with self.__keyboard.pressed(Key.shift):
                self.__keyboard.press(Key.enter)
                self.__keyboard.release(Key.enter)
            time.sleep(0.01)
            self.__keyboard.press(Key.enter)
            self.__keyboard.release(Key.enter)
        elif what == 'stop':
            with self.__keyboard.pressed(Key.cmd):
                self.__keyboard.press(Key.right)
                self.__keyboard.release(Key.right)
            time.sleep(0.01)
            self.__keyboard.type('.stop')
            with self.__keyboard.pressed(Key.shift):
                self.__keyboard.press(Key.enter)
                self.__keyboard.release(Key.enter)
            time.sleep(0.01)
            self.__keyboard.press(Key.enter)
            self.__keyboard.release(Key.enter)
        elif what == 'alt_eval':
            with self.__keyboard.pressed(Key.cmd):
                self.__keyboard.type('e')
                self.__keyboard.release(Key.cmd)
        elif what == 'eval':
            with self.__keyboard.pressed(Key.shift):
                self.__keyboard.press(Key.enter)
                self.__keyboard.release(Key.enter)
            time.sleep(0.2)
            self.__keyboard.press(Key.enter)
            self.__keyboard.release(Key.enter)

    def goDown(self):
        """Press command-arrow down and enter.
        """
        with self.__keyboard.pressed(Key.cmd):
            self.__keyboard.press(Key.down)
            self.__keyboard.release(Key.down)
        time.sleep(0.2)
        self.__keyboard.press(Key.enter)
        self.__keyboard.release(Key.enter)

    def enter(self):
        """Press the enter key.
        """
        self.__keyboard.press(Key.enter)
        self.__keyboard.release(Key.enter)

    def delete(self):
        """Press the backspace key.
        """
        self.__keyboard.press(Key.backspace)
        self.__keyboard.release(Key.backspace)


    def mapping(self, midinumber, prototype='Hello World'):
        """Type a letter that is coupled to this midi note.

        :param int midinumber: the midinumber that is played
        """
        # chars and nums
        if midinumber == 58:
            self.__keyboard.type(' /// Het CodeKlavier: Muziek ontmoet Computertechniek \\\ '.upper())
            self.formatAndSend('/// Het CodeKlavier: Muziek ontmoet Computertechniek \\\ ', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 59:
            self.__keyboard.type('sentences ')
            self.formatAndSend('sentences ', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 60:
            self.__keyboard.type('or ')
            self.formatAndSend('or', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 61:
            self.__keyboard.type('words ')
            self.formatAndSend('words ', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 62:
            self.__keyboard.type('whole ')
            self.formatAndSend('whole ', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 63:
            self.__keyboard.type('in ')
            self.formatAndSend('in ', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 64:
            self.__keyboard.type('type ')
            self.formatAndSend('type ', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 65:
            self.__keyboard.type('also ')
            self.formatAndSend('also ', display=5, syntax_color='hello:', spacing=False)
        elif midinumber ==66:
            self.__keyboard.type('can ')
            self.formatAndSend('can ', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 67:
            self.__keyboard.type('piano ')
            self.formatAndSend('piano ', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 68:
            self.__keyboard.type('on ')
            self.formatAndSend('on ', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 69:
            self.__keyboard.type('however ')
            self.formatAndSend('however ', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 70:
            self.__keyboard.type('.')
            self.formatAndSend('.', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 71:
            self.__keyboard.type('~')
            self.formatAndSend('~', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 72:
            self.__keyboard.type('b')
            self.formatAndSend('b', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 73:
            self.__keyboard.type('a')
            self.formatAndSend('a', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 74:
            self.__keyboard.type('c')
            self.formatAndSend('c', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 75:
            self.__keyboard.type('e')
            self.formatAndSend('e', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 76:
            self.__keyboard.type('d')
            self.formatAndSend('d', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 77:
            self.__keyboard.type('f')
            self.formatAndSend('f', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 78:
            self.__keyboard.type('i')
            self.formatAndSend('i', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 79:
            self.__keyboard.type('g')
            self.formatAndSend('g', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 80:
            self.__keyboard.type('o')
            self.formatAndSend('o', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 81:
            self.__keyboard.press(Key.space)
            self.__keyboard.release(Key.space)
            self.formatAndSend('\n', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 82:
            self.__keyboard.type('u')
            self.formatAndSend('u', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 83:
            self.__keyboard.type('h')
            self.formatAndSend('h', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 84:
            self.__keyboard.type('j')
            self.formatAndSend('j', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 85:
            self.__keyboard.type('a')
            self.formatAndSend('a', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 86:
            self.__keyboard.type('k')
            self.formatAndSend('k', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 87:
            self.__keyboard.type('e')
            self.formatAndSend('e', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 88:
            self.__keyboard.type('l')
            self.formatAndSend('l', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 89:
            self.__keyboard.type('m')
            self.formatAndSend('m', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 90:
            self.__keyboard.type('i')
            self.formatAndSend('i', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 91:
            self.__keyboard.type('n')
            self.formatAndSend('n', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 92:
            self.__keyboard.type('o')
            self.formatAndSend('o', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 93:
            self.__keyboard.press(Key.space)
            self.__keyboard.release(Key.space)
            self.formatAndSend('\n', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 94:
            self.__keyboard.type('u')
            self.formatAndSend('u', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 95:
            self.__keyboard.type('p')
            self.formatAndSend('p', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 96:
            self.__keyboard.type('r')
            self.formatAndSend('r', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 97:
            self.__keyboard.type('0')
            self.formatAndSend('0', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 98:
            self.__keyboard.type('s')
            self.formatAndSend('s', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 99:
            self.__keyboard.type('1')
            self.formatAndSend('1', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 100:
            self.__keyboard.type('t')
            self.formatAndSend('t', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 101:
            self.__keyboard.type('v')
            self.formatAndSend('v', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 102:
            self.__keyboard.type('2')
            self.formatAndSend('2', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 103:
            self.__keyboard.type('w')
            self.formatAndSend('w', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 104:
            self.__keyboard.type('3')
            self.formatAndSend('3', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 105:
            self.__keyboard.type('y')
            self.formatAndSend('y', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 107:
            self.__keyboard.type('!')
            self.formatAndSend('!', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 108:
            self.__keyboard.press(Key.enter)
            self.__keyboard.release(Key.enter)
            self.formatAndSend('\n', display=5, syntax_color='hello:', spacing=False)
       # special keys

        elif midinumber == 95:
            self.__keyboard.press(Key.backspace)
            self.__keyboard.release(Key.backspace)
      # supercollider commands:
        elif midinumber == 21:
            self.evaluateSC('eval')
            self.formatAndSend('\n', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 22:
            self.__keyboard.press(Key.backspace)
        elif midinumber == 23:
            self.__keyboard.type('.load')
            self.formatAndSend('.load', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 102:
            self.__keyboard.type('TempoClock.default')
            self.formatAndSend('TempoClock.default', display=5, syntax_color='hello:', spacing=False)
        elif midinumber == 108:
            self.goDown()
    # motippets only commands:
        elif prototype == 'Motippets':
            if midinumber == 66:
                self.evaluateSC('eval')

    def formatAndSend(self, msg='', encoding='utf-8', host='localhost', display=1, syntax_color='', spacing=True):
        """format and prepare a string for sending it over UDP socket

        :param str msg: the string to be sent
        :param str encoding: the character encoding
        :param str host: the UDP server hostname
        :param int display: the UDP destination port
        :param str syntax_color: the tag to use for syntax coloring (loop, primitive, mid, low, hi, snippet)
        :param boolean spacing: wheather to put a \n (new line) before the msg
        """

        if display == 1:
            port = 1111
        elif display == 2:
            port = 2222
        elif display == 3:
            port = 3333
        elif display == 4:
            port = 4444
        elif display == 5:
            port = 5555

        if spacing:
            newline = '\n'
        else:
            newline = ''

        return self.__socket.sendto(bytes(syntax_color+newline+msg, encoding), (host, port))

    def snippets(self, num, configfile='default_setup.ini'):
        """Type code snippets

        :param int num: the id of the code snippet to play
        :param str configfile: the name of the config file to parse
        """

        if num == 1:
            self.__keyboard.type(self.__snippet1)
            self.formatAndSend(self.__snippet1, display=1, syntax_color='snippet:')
            self.evaluateSC('eval')
        elif num == 2:
            self.__keyboard.type(self.__snippet2)
            self.formatAndSend(self.__snippet2, display=2, syntax_color='snippet:')
            self.evaluateSC('eval')

    def miniSnippets(self, snippet_num, pianosection):
        """Type a mini snippet for specific pianosections'utf-8'

        :param int snippet_num: the id of the mini snippet to play
        :param string pianosections: the pianosection that is used ('hi', 'mid', 'low')
        """
        if snippet_num == 1 and pianosection == 'hi':
            self.__keyboard.type(self.__mini_snippet_hi_1)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_hi_1, display=snippet_num, syntax_color='snippet:')
        if snippet_num == 1 and pianosection == 'hi with unmap':
            self.__keyboard.type(self.__mini_snippet_hi_1)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_hi_1, display=snippet_num, syntax_color='snippet:')
            #unmap other motif
            self.__keyboard.type(self.__mini_unmap_hi_2)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_unmap_hi_2, display=snippet_num, syntax_color='snippet:')
        if snippet_num == 1 and pianosection == 'mid':
            self.__keyboard.type(self.__mini_snippet_mid_1)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_mid_1, display=snippet_num, syntax_color='snippet:')
        if snippet_num == 1 and pianosection == 'mid with unmap':
            self.__keyboard.type(self.__mini_snippet_mid_1)
            self.evaluateSC('eval')
            #unmap
            self.__keyboard.type(self.__mini_unmap_mid_2)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_unmap_mid_2, display=snippet_num, syntax_color='snippet:')

            ## LOW SECTION
        if snippet_num == 1 and pianosection == 'low':
            self.__keyboard.type(self.__mini_snippet_low_1)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_low_1, display=snippet_num, syntax_color='low:')
        if snippet_num == 1 and pianosection == 'low amp':
            self.__keyboard.type(self.__mini_snippet_low_1_amp)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_low_1_amp, display=snippet_num, syntax_color='low:')
        if snippet_num == 1 and pianosection == 'low with unmap 2':
            self.__keyboard.type(self.__mini_snippet_low_1)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_low_1, display=snippet_num, syntax_color='low:')
            #unmap 2:
            self.__keyboard.type(self.__mini_unmap_low_2)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_unmap_low_2, display=snippet_num, syntax_color='low:')
        if snippet_num == 1 and pianosection == 'low with unmap 3':
            self.__keyboard.type(self.__mini_snippet_low_1)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_low_1, display=snippet_num, syntax_color='low:')
            #unmap 3:
            self.__keyboard.type(self.__mini_unmap_low_3)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_unmap_low_3, display=snippet_num, syntax_color='low:')
        if snippet_num == 1 and pianosection == 'low amp with unmap 1':
            self.__keyboard.type(self.__mini_snippet_low_1_amp)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_low_1_amp, display=snippet_num, syntax_color='low:')
            #unmap 1:
            self.__keyboard.type(self.__mini_unmap_low_1)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_unmap_low_1, display=snippet_num, syntax_color='low:')
        if snippet_num == 1 and pianosection == 'low amp with unmap 2':
            self.__keyboard.type(self.__mini_snippet_low_1_amp)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_low_1, display=snippet_num, syntax_color='low:')
            #unmap 2:
            self.__keyboard.type(self.__mini_unmap_low_2)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_unmap_low_2, display=snippet_num, syntax_color='low:')

        # for snippet 2:
        if snippet_num == 2 and pianosection == 'hi':
            self.__keyboard.type(self.__mini_snippet_hi_2)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_hi_2, display=snippet_num, syntax_color='hi:')
        if snippet_num == 2 and pianosection == 'hi with unmap':
            self.__keyboard.type(self.__mini_snippet_hi_2)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_hi_2, display=snippet_num, syntax_color='hi:')
            #unmap other motif
            self.__keyboard.type(self.__mini_unmap_hi_1)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_unmap_hi_1, display=snippet_num, syntax_color='hi:')
        if snippet_num == 2 and pianosection == 'mid':
            self.__keyboard.type(self.__mini_snippet_mid_2)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_mid_2, display=snippet_num, syntax_color='mid:')
        if snippet_num == 2 and pianosection == 'mid with unmap':
            self.__keyboard.type(self.__mini_snippet_mid_2b)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_mid_2b, display=snippet_num, syntax_color='mid:')
            #unmap
            self.__keyboard.type(self.__mini_unmap_mid_1)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_unmap_mid_1, display=snippet_num, syntax_color='mid:')

            ## LOW SECTION
        if snippet_num == 2 and pianosection == 'low':
            self.__keyboard.type(self.__mini_snippet_low_2)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_low_2, display=snippet_num, syntax_color='low:')
        if snippet_num == 2 and pianosection == 'low with unmap 1':
            self.__keyboard.type(self.__mini_snippet_low_2)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_low_2, display=snippet_num, syntax_color='low:')
            #unmap 1:
            self.__keyboard.type(self.__mini_unmap_low_1)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_unmap_low_1, display=snippet_num, syntax_color='low:')
        if snippet_num == 2 and pianosection == 'low with unmap 3':
            self.__keyboard.type(self.__mini_snippet_low_2)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_snippet_low_2, display=snippet_num, syntax_color='low:')
            #unmap 3:
            self.__keyboard.type(self.__mini_unmap_low_3)
            self.evaluateSC('eval')
            self.formatAndSend(self.__mini_unmap_low_3, display=snippet_num, syntax_color='low:')


    def tremolo(self, pianoregister, value):
        """Type the tremolo command + the tremolo-value

        :param string pianoregister: the pianoregister the tremolo is played in. Values are: 'hi_1', 'hi_2', 'mid_1', 'mid_2', 'low_1', 'low_2', 'low_3'.
        :param int value: the tremolo value as distance between the notes
        """
        if pianoregister == 'hi_1':
            self.__keyboard.type('~tremoloH1 = ' + str(value))
            self.formatAndSend('~tremoloH1 = ' + str(value), display=1, syntax_color='hi:')
        elif pianoregister == 'hi_2':
            self.__keyboard.type('~tremoloH2 = ' + str(value))
            self.formatAndSend('~tremoloH2 = ' + str(value), display=2, syntax_color='hi:')
        elif pianoregister == 'mid_1':
            self.__keyboard.type('~tremoloM1 = ' + str(value))
            self.formatAndSend('~tremoloM1 = ' + str(value), display=1, syntax_color='mid:')
        elif pianoregister == 'mid_2':
            self.__keyboard.type('~tremoloM2 = ' + str(value))
            self.formatAndSend('~tremoloM2 = ' + str(value), display=2, syntax_color='mid:')
        elif pianoregister == 'low_1':
            self.__keyboard.type('~tremoloL1 = ' + str(value))
            self.formatAndSend('~tremoloL1 = ' + str(value), display=1, syntax_color='low:')
        elif pianoregister == 'low_2':
            self.__keyboard.type('~tremoloL2 = ' + str(value))
            self.formatAndSend('~tremoloL2 = ' + str(value), display=2, syntax_color='low:')
        elif pianoregister == 'low_3':
            self.__keyboard.type('~tremoloL1amp = ' + str(value))
            self.formatAndSend('~tremoloL1amp = ' + str(value), display=1, syntax_color='low:')
        self.evaluateSC('eval')

    def conditional(self, conditional_num):
        """Setup a conditional

        There are three options: settimg up a conditional if number of notes
        played is more than 100 in ... (option 1), setting up a conditional if
        range is more than ... (option 2), and setting up a conditional if range
        is less than ... (option 3).

        :param int conditional_num: the selection for the type of conditional
        """
        if conditional_num == 1:
            self.__keyboard.type('// setting up a conditional: IF number of\
            notes played is more than 100 in...')
            self.enter()
            self.formatAndSend('setting up a conditional: \nIF number of notes played is more than 100 in...', display=3, syntax_color='primitive:')
        elif conditional_num == 2:
            self.__keyboard.type('// setting up an ONGOING conditional: IF range is more than...')
            self.enter()
            self.formatAndSend('setting up an ONGOING conditional: \nIF range is more than...', display=3, syntax_color='primitive:')
        elif conditional_num == 3:
            self.__keyboard.type('// setting up an ONGOING conditional: IF range is less than...')
            self.enter()
            self.formatAndSend('setting up an ONGOING conditional: \nIF range is less than...', display=3, syntax_color='primitive:')

    def result(self, result_num, text, mod=0): #how to make optional params?
        """TOOD: document function

        :param int result_num: type of result?
        :param string text: indication of the type of message
        :param mod: some function
        :type mod: int or None
        """
        if result_num == 1:
            if text == 'comment':
                self.__keyboard.type('// if true -> print encouragement')
                self.enter()                
                self.formatAndSend('if true -> print encouragement', display=3, syntax_color='snippet:')
            elif text == 'code':
                self._osc.send_message("/ck_pp", "text1")
                self.formatAndSend('if true -> print encouragement;', display=3, syntax_color='snippet:')
            elif text == 'less than':
                self.__keyboard.type('//less than an 8ve. Nothing happens :(')
                self.evaluateSC('eval')
                self.formatAndSend('if false -> Nothing happens BUUUUU!', display=3, syntax_color='primitive:')

        elif result_num == 2:
            if text == 'comment':
                self.__keyboard.type('// if true -> stop ~snippet1')
                self.enter()
                self.formatAndSend('if true -> stop ~snippet1', display=3, syntax_color='primitive:')
            elif text == 'code':
                self.__keyboard.type('~snippet1.stop(10);')
                self.evaluateSC('eval')
                self.formatAndSend('~snippet1.stop;', display=3)
            elif text == 'less than':
                self.__keyboard.type('//less than an 8ve. Nothing happens :(')
                self.evaluateSC('eval')
                self.formatAndSend('if false -> Nothing happens BUUUUU!', display=3, syntax_color='primitive:')

        elif result_num == 3:
            if text == 'comment':
                self.__keyboard.type('// if true -> print quote')
                self.enter()
                self.formatAndSend('if true -> print quote', display=3, syntax_color='primitive:')
            elif text == 'code':
                #self.__keyboard.type('~gong.play(' + str(mod) + ');')
                #self.evaluateSC('eval')
                self._osc.send_message("/gong", str(mod))
                self._osc.send_message("/ck_pp", "quote")
                self.formatAndSend('~gong.play(' + str(mod) + ');', display=3, syntax_color='snippet:')
            elif text == 'less than':
                #self.__keyboard.type('~gong.play(' + str(mod) + ');');
                #self.evaluateSC('eval')
                self._osc.send_message("/gong", str(mod))
                self.formatAndSend('~gong.play(' + str(mod) + ');', display=3, syntax_color='snippet:')


        elif result_num == 4:
            if text == 'comment':
                self.__keyboard.type('HUYGENS! //is activating...')
                self.evaluateSC('eval')
                self.formatAndSend('HUYGENS', display=1, syntax_color='warning:')
                self.formatAndSend('IS', display=2, syntax_color='warning:')
                self.formatAndSend('ACTIVATING...', display=3, syntax_color='warning:')
            elif text == 'start':
                self.__keyboard.type('// HUYGENS countdown started!')
                self.evaluateSC('eval')
                self.formatAndSend('HUYGENS', display=1, syntax_color='warning:')
                self.formatAndSend('COUNTDOWN', display=2, syntax_color='warning:')
                self.formatAndSend('STARTED!', display=3, syntax_color='warning:')
            elif text == 'code':
                self.__keyboard.type("")
                self.enter()
                self.__keyboard.type("  ____   ____   ____  __  __ _ ")
                self.enter()
                self.formatAndSend("  ____   ____   ____  __  __ _ ", display=1, syntax_color='primitive:')
                self.formatAndSend("  ____   ____   ____  __  __ _ ", display=2, syntax_color='primitive:')
                self.formatAndSend("  ____   ____   ____  __  __ _ ", display=3, syntax_color='primitive:')
                self.__keyboard.type(" |  _ \ / __ \ / __ \|  \/  | |")
                self.enter()
                self.formatAndSend(" |  _ \ / __ \ / __ \|  \/  | |", display=1, syntax_color='primitive:')
                self.formatAndSend(" |  _ \ / __ \ / __ \|  \/  | |", display=2, syntax_color='primitive:')
                self.formatAndSend(" |  _ \ / __ \ / __ \|  \/  | |", display=3, syntax_color='primitive:')
                self.__keyboard.type(" | |_) | |  | | |  | | \  / | |")
                self.enter()
                self.formatAndSend(" | |_) | |  | | |  | | \  / | |", display=1, syntax_color='primitive:')
                self.formatAndSend(" | |_) | |  | | |  | | \  / | |", display=2, syntax_color='primitive:')
                self.formatAndSend(" | |_) | |  | | |  | | \  / | |", display=3, syntax_color='primitive:')
                self.__keyboard.type(" |  _ <| |  | | |  | | |\/| | |")
                self.enter()
                self.formatAndSend(" |  _ <| |  | | |  | | |\/| | |", display=1, syntax_color='primitive:')
                self.formatAndSend(" |  _ <| |  | | |  | | |\/| | |", display=2, syntax_color='primitive:')
                self.formatAndSend(" |  _ <| |  | | |  | | |\/| | |", display=3, syntax_color='primitive:')
                self.__keyboard.type(" | |_) | |__| | |__| | |  | |_|")
                self.enter()
                self.formatAndSend(" | |_) | |__| | |__| | |  | |_|", display=1, syntax_color='primitive:')
                self.formatAndSend(" | |_) | |__| | |__| | |  | |_|", display=2, syntax_color='primitive:')
                self.formatAndSend(" | |_) | |__| | |__| | |  | |_|", display=3, syntax_color='primitive:')
                self.__keyboard.type(" |____/ \____/ \____/|_|  |_(_)   (^0^)//¯  AIR DE COUR  THE END ¯\('…')/¯ ")
                self.enter()
                self.formatAndSend(" |____/ \____/ \____/|_|  |_(_)   (^0^)//¯  AIR DE COUR  THE END ¯\('…')/¯ ", display=1, syntax_color='primitive:')
                self.formatAndSend(" |____/ \____/ \____/|_|  |_(_)   (^0^)//¯  AIR DE COUR  THE END ¯\('…')/¯ ", display=2, syntax_color='primitive:')
                self.formatAndSend(" |____/ \____/ \____/|_|  |_(_)   (^0^)//¯  AIR DE COUR  THE END ¯\('…')/¯ ", display=3, syntax_color='primitive:')
                self.__keyboard.type("")
                self.enter()
            elif text == 'huygens':
                self.__keyboard.type('~huygens.end;')
                self.evaluateSC('eval')

        elif result_num == 5:
            if text == 'comment':
                self.__keyboard.type('// if true -> play Huyg')
                self.enter()
                self.formatAndSend('if true -> play Huyg', display=3, syntax_color='primitive:')
            elif text == 'code':
                #self.__keyboard.type('~huygens.stuk('+ str(mod) +');')
                #self.evaluateSC('eval')
                self._osc.send_message("/huygens", str(mod))
                self.formatAndSend('~huygens.stuk(' + str(mod) + ');', display=3, syntax_color='snippet:')
            elif text == 'less than':
                #self.__keyboard.type('~huygens.stuk('+ str(mod) +');')
                #self.evaluateSC('eval')
                self._osc.send_message("/huygens", str(mod))
                self.formatAndSend('~huygens.stuk(' + str(mod) + ');', display=3, syntax_color='snippet:')

        elif result_num == 6:
            if text == 'comment':
                self.__keyboard.type('HUYGENS! //is activating...')
                self.evaluateSC('eval')
            elif text == 'start':
                self.__keyboard.type('// HUYGENS countdown started!')
                self.evaluateSC('eval')
            elif text == 'code':
                self.__keyboard.type("")
                self.enter()
                self.__keyboard.type("  ____   ____   ____  __  __ _ ")
                self.enter()
                self.__keyboard.type(" |  _ \ / __ \ / __ \|  \/  | |")
                self.enter()
                self.__keyboard.type(" | |_) | |  | | |  | | \  / | |")
                self.enter()
                self.__keyboard.type(" |  _ <| |  | | |  | | |\/| | |")
                self.enter()
                self.__keyboard.type(" | |_) | |__| | |__| | |  | |_|")
                self.enter()
                self.__keyboard.type(" |____/ \____/ \____/|_|  |_(_)   (^0^)//¯  AIR DE COUR  ¯\\(^0^) ")
                self.enter()
                self.__keyboard.type("")
                self.enter()
            elif text == 'huygens':
                self.__keyboard.type('~huygens.eind')
                self.evaluateSC('eval')

    def customPass(self, name, content):
        """
        post custom string message on codespace and display

        :param string name: a label to print in front of the string
        :param string content: the message or content
        """
        self.__keyboard.type(name + " " + content)
        self.enter()
        self.formatAndSend(name + " " + content, display=3, syntax_color='comment:')

    def onlyDisplay(self, content, tag=1, warning=False):
        """
        print a custom string on the UDP display only!

        :param string content: the message or content
        :param int tag: the reference to a color tag
        :param warning: wether to print the message with the warning color tag (i.e. red)

        """
        if warning:
            self.formatAndSend(content, display=4, syntax_color='warning:')
        else:
            if tag == 2:
                self.formatAndSend(content, display=4, syntax_color='loop2:')
            elif tag == 3:
                self.formatAndSend(content, display=4, syntax_color='loop3:')
            else:
                self.formatAndSend(content, display=4, syntax_color='loop:')

class Mapping_Ckalculator:
    """Mapping for the Ckalculator prototype.
    """
    def __init__(self, use_display=False, debug=True):
        if debug:
            print("## Using the Ckalculator mapping ##")

        self.__keyboard = Controller()

        if use_display:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self._osc = udp_client.SimpleUDPClient('127.0.0.1', 57120)


    def formatAndSend(self, msg='', encoding='utf-8', host='localhost', display=1, syntax_color='', spacing=True):
        """format and prepare a string for sending it over UDP socket

        :param str msg: the string to be sent
        :param str encoding: the character encoding
        :param str host: the UDP server hostname
        :param int display: the UDP destination port
        :param str syntax_color: the tag to use for syntax coloring (loop, primitive, mid, low, hi, snippet)
        :param boolean spacing: wheather to put a \n (new line) before the msg
        """

        if display == 1:
            port = 1111
        elif display == 2:
            port = 2222
        elif display == 3:
            port = 3333

        if spacing:
            newline = '\n'
        else:
            newline = ' -> '

        return self.__socket.sendto(bytes(syntax_color+msg+newline, encoding), (host, port))

    def newLine(self, display=1):
        """
        send a new line to the code display
        """
        if display == 1:
            port = 1111
        elif display == 2:
            port = 2222
        elif display == 3:
            port = 3333

        return self.__socket.sendto(bytes('line:\n', 'utf-8'), ('localhost', port))
