#!/usr/bin/python3
"""The Console"""

import cmd
from models import storage

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, line):
        return True


    def emptyline(self):
        pass

    def do_EOF(self, line):
        print()
        return True

    def do_create(self, line):
        pass

    def do_show(self):
        pass

    def do_destroy(self, line):
        pass

    def do_all(self, line):
        pass

    def do_update(self, line):
        storage.save()



if __name__ == "__main__":
    HBNBCommand().cmdloop()
