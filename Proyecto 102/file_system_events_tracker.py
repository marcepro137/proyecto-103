import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from  watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/homer/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} ha sido creado!!")

    def on_deleted(self, event):
        print(f"Se a eliminado {event.src_path}")

    def on_modified(self, event):
        print(f"Se a modificado {event.src_path}")

    def on_moved(self, event):
        print(f"Se a movido {event.src_path}")

Event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive = True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("¿detenido!")
    observer.stop()
