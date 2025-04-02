# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Course, Enrollment
from .forms import StudentForm, CourseForm, EnrollmentForm

def dashboard(request):
    context = {
        'total_students':  Student.objects.count(),
        'total_courses': Course.objects.count(),
        'total_enrollments': Enrollment.objects.count(),
        'recent_students': Student.objects.order_by('-enrollment_date')[:5],
    }
    return render(request, 'dashboard.html', context)

# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'
    # ordering = ['last_name', 'first_name']

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enrollments'] = Enrollment.objects.filter(student=self.object)
        return context

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy
    

# Course Views
class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    ordering = ['course_code']

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enrollments'] = Enrollment.objects.filter(course=self.object)
        return context

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course-list')

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course-list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course-list')

# Enrollment Views
class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'enrollments/enrollment_list.html'
    context_object_name = 'enrollments'

class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/enrollment_form.html'
    success_url = reverse_lazy('enrollment-list')

class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/enrollment_form.html'
    success_url = reverse_lazy('enrollment-list')

class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'enrollments/enrollment_confirm_delete.html'
    success_url = reverse_lazy('enrollment-list')

