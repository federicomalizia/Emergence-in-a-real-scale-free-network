# -*- coding: utf-8 -*-
"""
@author: Federico Malizia
"""
import numpy as np
import random 

class User():
    def __init__(self,name,age,district,party,unique_id,shyness):
        self.name = name
        self.age = age
        self.district = district
        self.party = party
        self.unique_id = unique_id
        self.shyness = shyness
        self.friends_count = 0
        self.friends_dict = {}
        self.sympaties_dict = {} 
        self.state = "seg" #segregated
        
        
    def features(self,features_vec):
        self.features = features_vec
        
     
    def who_are_u(self):
        return(self.name,self.age,self.district,self.party)
    
    
    def get_id(self):
        return(self.unique_id)
    
    
    def get_features(self):
        return(self.features)     
    
        
    def get_user_state(self):
        return(self.state)
    
    
    def look_around(self,N):
        if self.friends_count <= 2:
            randomsteps = [i for i in range(int(-N/10),int(N/10))] 
            self.step = np.random.choice(randomsteps)
        if self.friends_count > 2 and self.friends_count <=5:
            randomsteps = [i for i in range(int(-N/5),int(N/5))] 
            self.step = np.random.choice(randomsteps)
        if self.friends_count > 5:
            randomsteps = [i for i in range(-N,N)]
            self.step = np.random.choice(randomsteps)
        return(self.step)
   

    def make_your_decision(self):
        
        if random.random() >= self.shyness:
            decision = True
        else:
            decision = False
        return(decision)
   

    def sympathy(self,friend):       
        v_1 = np.array(self.features, dtype = "int")
        v_2 = np.array(friend.features, dtype = "int")
        sympathy_degree = np.linalg.norm(v_1 - v_2)
        self.sympaties_dict[friend.get_id()] = sympathy_degree
        return(sympathy_degree)
    
    
    def approach(self,friend,threshold,decision):
        success = False
        if friend.get_id() not in self.friends_dict.keys() and friend.get_id() != self.get_id():
            if decision == True:
                if self.sympathy(friend) <= (threshold*100):
                    success = True
                    self.add_friend(friend,success)
                    
        return (success)


    def got_approached(self,friend,success):              
                return(self.add_friend(friend,success))
        
    
    def add_friend(self,friend, success):
        if success == True :
            self.friends_count += 1
            self.friends_dict[friend.get_id()] = friend
        else:
            pass
        return(success)
    
        

    def mood(self,N,k_25,average_k, k_75):
        if self.friends_count > 0 and self.friends_count <= k_25:           
            self.state = "a" #asocial
        if self.friends_count > k_25 and self.friends_count <= average_k:
            self.state = "s" #sociable
        if self.friends_count > average_k and self.friends_count < k_75:      
            self.state ="c" #cool
        if self.friends_count != 0 and self.friends_count >= k_75:           
            self.state = "i" #influencer
        return(self.state)