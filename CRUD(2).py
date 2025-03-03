from animal_shelter import AnimalShelter
from bson.objectid import ObjectId


class AnimalShelter(object):
    
    def __init__(self, username, password):

        username = 'aacuser'
        password = 'SNHU1234'

        animals = AnimalShelter(username, password)
      
        
        animal = animals.read({"animal_id":animal_id})
        print(animal)

        animal_ = animals.read_all()
        for animal in animals:
            print('{0}: {1}, {2} {3}'.format(animal['animal_id'], 
            animal['name'], animal['breed'], animal['animal_type']))   
    # Recursive call
        

    def create(self, data):
        if data is not None:
            insert  = self.database.animals.insert(data)  # data should be dictionary  
            return True
        else:
            print('Nothing to save, because data parameter is empty')
            return False                     
           
    
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data)
        else:
            print('Nothing to read, because data parameter is empty')
            return False
        
    def update(self, data, change):
        if data is not None: 
            if data:
                result = self.database.animals.update(data,{ "$set": change})  
            return result;
        else:
            print("Nothing to update, because data parameter is empty")
            return False
        
    def delete(self, data):
        if data is not None:
            if data:
                result = self.database.animals.delete_one(data) # data should be dictionary
        else:
            print("Nothing to delete, because data parameter is empty")
            return False