from django.shortcuts import render
from . models import *
from django.views.generic import View

# Create your views here.

class HomeView(View):
     def get(self,request,*args,**kwargs):
    #     obj=Person.objects.get(id=1) #1 fetch all the interest of the person
    #     print(obj.name)
    #     for i in obj.interest.all():
    #         print(i)
    #     adr=obj.personaddress
    #     print(adr.city,adr.street_address,"++++++++++")
     #   context={'data':obj}

        c=City.objects.get(id=3)  #2 fetch all the person in city
        print(c)
        #all_person_addr=c.personaddress_set.all()  #reverse relationship, note:->if you dont want to use _set.all method then can use related_name 
        all_person_addr=c.personcity.all()
        for adr in all_person_addr:
            print(adr.person)
        # print( all_person_addr)                
        context={'c':c}

        # int=Interest.objects.get(id=4)  #3 fetch all the person related to interest
        # per=int.person_set.all() #reverse relationship,lower case of model class
        # print(int)
        # for i in per:
        #     print(i)
        #     # print(per)
        
        # context={'int':int}
        return render(request,"home.html",context)
