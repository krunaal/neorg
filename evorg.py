import sys

#"hello how are you.1"
# just checking how to eddit in github
# Just editing
# 2nd commit from git CLI

class NewEvent:
    def __init__(self, date, starttime, venue, serial_n=1, endtime=None):
        self.date = date
        self.starttime = starttime
        if endtime == None:
            self.endtime = 'TillWeDepart'
        else:
            self.endtime = endtime
        self.venue = venue
        self.serial_n = serial_n
        self._participants = set()f
        self._key_participants = set()
        self._locked = 0

    # def check_locked(self, item, value):
    #     if self._locked == 1:
    #         print("Instance commited. Please unlock it to make changes..")
    #     else:
    #         item = value

    def info(self):
        _max_length = max(len(self.date), len(self.starttime), len(self.endtime), len(self.venue))
        _banner = "+" + "-" * (_max_length + 11) + "+"
        print(_banner)
        print("|" + "Date     : {:>12}".format(self.date) + "|")
        print("|" + "StartTime: {:>12}".format(self.starttime) + "|")
        print("|" + "EndTime  : {:>12}".format(self.endtime) + "|")
        print("|" + "Venue    : {:>12}".format(self.venue) + "|")
        print(_banner)

    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, participants_set):
        """
        list of participant as a set
        """
        self._participants = participants_set

    @property
    def key_participants(self):
        return self._key_participants

    @key_participants.setter
    def key_participants(self, key_people):
        if self._locked == 1:
            print("Instance commited. Please unlock it to make changes..")
        else:
            self._key_participants = key_people
        # let's refractor above code later to use it like this ..
        #self.check_locked(self.key_participants = key_people)

    def commit(self):
        self._locked = 1

    # needs some work!
    def unlock(self):
        try:
            key = int(input("Please provide key to unlock").strip())
            if key == 1234:
                self._locked = 0
                print("Your instance is unlocked now. You can make changes. Do not forget to commit after changes "
                      "are done.")
            else:
                print("You provided {} key which doesn't match our records".format(key))
                new_key = input("press 'e' to exit or any other key to try to unlock again..")
                if new_key == 'e':
                    print("You exited. Instance is still locked")
                else:
                    self.unlock()
        except ValueError as e:
            print("Input Error: {}".format(str(e)), file=sys.stderr)
            #print("You provided key which is not valid set of numbers")
            new_key = input("press 'e' to exit or any other key to try to try unlocking again..")
            if new_key == 'e':
                print("You exited. Instance is still locked")
            else:
                self.unlock()

# class NewSession(NewEvent):
#     """
#     this is to define new sessions/options that we are going to create from the main event. To give options to
#     all participants. Based on all the instances of NewSessions, participants would have chance to select and
#     use one of the instance or more instances. And from which we are going to get a timeslot which has max participation
#     as well as key members involvement.
#     """
#     def __init__(self, *args):
#         #NewEvent.__init__(*args)
#         self.serial_n += 1
#         # self.date = date
#         # self.starttime = starttime
#         # if endtime == None:
#         #     self.endtime = 'TillWeDepart'
#         # else:
#         #     self.endtime = endtime
#         # self.venue = venue
#         # self._participants = NewEvent.participants
        # self._key_participants = NewEvent.key_participants


if __name__ == '__main__':
    NE1 = NewEvent('04/28/2018', '6:00pm', 'MyHome')
    p = {'Amit', 'Pratik', 'Piyush', 'Sandipan', 'Saourabh', 'Susheel', 'Ashok', 'Ajit', 'Shankar', 'Maruti'}
    NE1.participants = p
    NE1.key_participants = {'Amit', 'Pratik', 'Piyush', 'Sandipan', 'Saourabh'}
    NE1.commit()
