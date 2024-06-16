from rich.console import Console
from rich.progress import Progress
import time

console = Console()


second = 1
minute = 1
hour = minute * 60


class pomodoro:

    # TODO: remove the arguments down to the pomodoro timer method
    def __init__(self, sessions, time_per_intervals): 
        self.time_intervals = time_per_intervals
        self.total_time = 0
        self.time_left = sessions * self.time_intervals
        self.session_time = 0
        self.session_tracker = 0

    def user_input(self):
        minutes = console.input('How many minutes per session?')
        sessions = console.input('How many sessions?')

        console.print(f'You selected {sessions} at {minutes} minutes each.')
        console.print('...')
        console.print('Running')
        return  

    def rest(self, rest_time):
        rest = rest_time * 60

        for _ in range(rest):
            rest -= 1

            if rest == 0:
                self.session_time = 0
                break
                

    def pomodoro_timer(self):
        task = Progress.add_task("[cyan]Working...")

        for _ in range(self.time_left):
            self.time_left -= 1            
            self.session_time += 1
            self.session_tracker += 1
            self.session_count = 0
            Progress.update(task)
            
            if self.session_time == self.time_intervals:
               self.session_count -= 1
               self.rest

            if self.session_count == 0:

                print("No more sessions")
                break
        return   


user = pomodoro(minutes, sessions)
user_input()






