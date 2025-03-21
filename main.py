import uvicorn
from fastapi import FastAPI
from BankNoteSchema import BankNote
import pickle

app=FastAPI()

pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.post("/predict")
def get_prediction(data:BankNote):
    data=data.dict()
    variance=data['variance']
    skewness=data['skewness']	
    curtosis=data['curtosis']	
    entropy=data['entropy']
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    
    if prediction[0]==1:
        result="Its a Bank note"
    else:
        result="Its a Fake note"
    return {"prediction":result}

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1")
