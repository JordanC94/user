# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_memeber = False
        self.gold_card_points = 0
    def displayInfo(self):
        print(self.first_name, self.last_name, self.email, self.age, self.is_rewards_memeber, self.gold_card_points)
    def enroll(self):
      self.is_rewards_memeber = True
      self.gold_card_points = 200
    def spend_points(self, amount):
      self.gold_card_points -= amount

        
jordan = User("Jordan","Carlson","jordan@codingdojo.com", 27)
jordan.enroll()
jordan.spend_points(50)
print(jordan.gold_card_points)


# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.