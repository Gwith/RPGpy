#!/usr/bin/env python

'''
5 Room -- w/Random Generation
Store -- Buy Items
Weapons -- Dual-Wield, Shield, etc.
Inventory -- (e.g. pick up, drop, sell, etc.)
3 Monsters
1 Hero
'''

class Hero:
  def __init__(self, name)
  	self.name = name
    self.hp = 100
    self.maxhealth = self.hp
    self.currentweapon = None
    self.armour = None
    self.backpack = Backpack()
    
class Backpack:
  def __init__(self, capacity=5):
    self.items = []
    self.capacity = capacity
    
  def isFull(self):
    return len(self.items) >= self.capacity
  
  def store(self, item):
    if not self.isFull():
      self.items.append(item)
      
def store():
  print('Welcome to the store')
  #sell
  #leave
  pass

def inventory():
  #equip
  #list inventory
  #leave
  pass

Gwith = BasicHero('Gwith')


    

class BasicHero(Hero):
  def __init__(self, name):
		super(Hero, self).__init__()
    self.currentweapon = 'Dagger'
    self.armour = 'Leather Vest'
    
if __name__ == '__main__':
  
  
  
  
  
  
  
  
  
  
  
  
  
  