from django.shortcuts import render
from CRUDOperation.models import EmpModel, Patient
from django.contrib import messages
from CRUDOperation.forms import Empforms, PatientForms



    

def showemp(request):
    showall = EmpModel.objects.all()
    showallpatients = Patient.objects.all()
    return render(request,'index.html',{"data":showall,"patdata":showallpatients})

def insertemp(request):
    if request.method == "POST":
        if request.POST.get('empname') and request.POST.get('dateofbirth') and request.POST.get('iin') and request.POST.get('contact') and request.POST.get('departmentid') and request.POST.get('specializationid') and request.POST.get('experience') and request.POST.get('photo') and request.POST.get('category') and request.POST.get('price') and request.POST.get('schedule') and request.POST.get('education') and request.POST.get('rating') and request.POST.get('address'):
            saverecord = EmpModel()
            saverecord.empname = request.POST.get('empname') 
            saverecord.dateofbirth = request.POST.get('dateofbirth')
            saverecord.iin = request.POST.get('iin')
            saverecord.contact = request.POST.get('contact')
            saverecord.departmentid = request.POST.get('departmentid')
            saverecord.specializationid = request.POST.get('specializationid')
            saverecord.experience = request.POST.get('experience')
            saverecord.photo = request.POST.get('photo')
            saverecord.category = request.POST.get('category')
            saverecord.price = request.POST.get('price')
            saverecord.schedule = request.POST.get('schedule')
            saverecord.education = request.POST.get('education')
            saverecord.rating = request.POST.get('rating')
            saverecord.address = request.POST.get('address')
            saverecord.save()
            messages.success(request, "Employee " + saverecord.empname + " has been added successfully")
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')

def editemp(request,id):
    editempobj = EmpModel.objects.get(id=id)
    return render(request, 'edit.html', {"EmpModel":editempobj})


def updateemp(request,id):
    Updateemp = EmpModel.objects.get(id=id)
    form = Empforms(request.POST,instance=Updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,"Record is updated successfully")
        return render(request, 'edit.html', {"EmpModel":Updateemp})

def delemp(request,id):
    delemployee = EmpModel.objects.get(id=id)
    delemployee.delete()
    showdata = EmpModel.objects.all()
    return render(request, "delete.html", {"data":showdata})