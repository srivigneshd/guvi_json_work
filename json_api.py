import requests


class sriv:
    #url="https://dummyjson.com/test"
    url='https://dummyjson.com/products'
    #fetching all the data from the API server
    def fetchData(self):
        response=requests.get(self.url)
        return response.json()
    #count the number of JSON DATA present in the API server
    def CountJSONdata(self):
        datas=self.fetchData()
        count=0
        for data in datas:
            count+=1
            print(data)
        return count
    # Fetch all the details individually from API serever
    def GetAllData(self):
        data=self.fetchData()
        print(data)
        print(data["total"])
        for key, value in data.items():
            print(key, ':', value)
    
    #fetch data based on id
    def FetchById(self,id):
        id=str(id)
        for data in self.fetchData():
            if data["id"]==id:
                print(data['id'])
                print(data['name'])
                print(data['location'])


        
        

s=sriv()
print(s.fetchData())
print(s.CountJSONdata())
s.GetAllData()
