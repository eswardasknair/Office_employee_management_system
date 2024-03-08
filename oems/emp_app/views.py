from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])


        new_emp = Employee(first_name=first_name, last_name=last_name, dept_id=dept, role_id=role, salary=salary, bonus=bonus, phone = phone, hire_date=datetime.now())
        new_emp.save()
        return render(request,'emp_added.html')

    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('An Exception occured! Employee has not been added')

    return render(request,'add_emp.html')

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            delete_Emp = Employee.objects.get(id=emp_id)
            delete_Emp.delete()
            return render(request,'emp_deleted.html')
        except:
            return HttpResponse('Enter a valid Employee id')
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html', context)

def filter_emp(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if first_name:
            emps = emps.filter(first_name__icontains = first_name)
        if last_name:
            emps = emps.filter(last_name__icontains = last_name)
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps' : emps
        }

        return render(request,'all_emp.html',context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('Invalid parameters')