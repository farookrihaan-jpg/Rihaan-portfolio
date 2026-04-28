from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage, Project

def home(request):
    # Fetch projects from database
    projects = Project.objects.filter(is_active=True)
    
    # Convert projects to the format needed by template
    projects_data = []
    for project in projects:
        projects_data.append({
            'title': project.title,
            'description': project.description,
            'technologies': project.get_technologies_list(),
        })
    
    context = {
        'name': 'Mohammed Rihaan M',
        'role': 'Python Full Stack Developer',
        'skills': [
            {'name': 'HTML', 'level': 90},
            {'name': 'CSS', 'level': 85},
            {'name': 'JavaScript', 'level': 80},
            {'name': 'React', 'level': 85},
            {'name': 'Python', 'level': 95},
            {'name': 'Django', 'level': 90},
            {'name': 'SQL', 'level': 85},
        ],
        'projects': projects_data,
        'education': [
            {
                'degree': 'B.E Mechanical and Automation Engineering',
                'institution': 'Sri Sairam Engineering College, Chennai',
                'year': 'Graduated',
            },
            {
                'degree': 'Python Full Stack Developer Certification',
                'institution': 'SLA Institute',
                'year': 'Certified',
            },
        ],
        'contact': {
            'phone': '8610087062',
            'email': 'farookrihaan@gmail.com',
            'linkedin': 'https://www.linkedin.com/in/mohammed-rihaan-m-901316251',
            'github': 'https://github.com/farookrihaan-jpg',
        }
    }
    return render(request, 'portfolio/home.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('portfolio:home')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})
