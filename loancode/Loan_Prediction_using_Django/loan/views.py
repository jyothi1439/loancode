from django.shortcuts import render
from .loan import prediction
# Create your views here.




def Index(request):
	return render(request,'index.html')


def Prediction(request):
	if request.method == "POST":
		Gender = (request.POST['Gender'])
		Married = (request.POST['Married'])
		Dependents = request.POST['Dependents']
		Education = request.POST['Education']
		Self_Employed = request.POST['Self_Employed']
		ApplicantIncome = request.POST['ApplicantIncome']
		CoapplicantIncome = request.POST['CoapplicantIncome']
		LoanAmount = request.POST['LoanAmount']
		Loan_Amount_Term = request.POST['Loan_Amount_Term']
		Credit_History = request.POST['Credit_History']
		Property_Area = request.POST['Property_Area']

		loan = prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
                 Loan_Amount_Term, Credit_History, Property_Area)
		numb =10
		num = float(ApplicantIncome) * float(numb)

		value=float(Loan_Amount_Term)*12
		if(value>=float(LoanAmount)):
			loan='Y'
		if(value<float(LoanAmount)):
			loan='N'
			
		if(loan=='Y'):
			return render(request,'predictions.html', {'loan':num})
		else:
			return render(request,'prediction.html',{'loan':loan})
	return render('request','prediction.html')

def Visualization(request):
	return render(request,'visualization.html')

def Firstpage(request):
	return render(request,'firstpage.html')





























































