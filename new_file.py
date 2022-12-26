# Импортируйте datetime. 
import datetime 
# Импортируйте time.
import time

class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = start_time = None
        self.end_time = end_time = None
        # Допишите два свойства класса.
    
    # Напишите методы приема и сдачи квеста.
    def accept_quest(self):
        self.start_time = datetime.datetime.utcnow():
        return ('Начало "{self.name}" положено.')
            if self.end_time is not None:
            return ('С этим испытанием вы уже справились.')
        
            
    
    
    def pass_quest(self):
        self.end_time = datetime.datetime.now()
        if self.start_time is not None:
            completion_time = self.end_time - self.start_time
            return (f'Квест {self.name} окончен.'
                   f'Время выполнения квеста:'
                   f'{completion_time}')
        elif self.start_time == None:
            return ('Нельзя завершить то, что не имеет начала!')
    
    
quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

new_quest = Quest(quest_name, quest_description, quest_goal) 

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())