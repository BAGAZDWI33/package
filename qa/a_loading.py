import itertools
import threading
import time
import sys



class load:

    def loading(self):
        done = False

        def bagas_dwi():
            for bagas in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rMemperoses data ' + bagas)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=bagas_dwi)
        t.start()

        time.sleep(3)
        done = True