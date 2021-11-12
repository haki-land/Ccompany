from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, TemplateView

from estimateapp.forms import ImageCreationForm
from estimateapp.models import EstimateModel, Output
from estimateapp.process import Process

def CreateEstimateView(request):
    # print("FILES : ", request.FILES)
    견적서폼 = ImageCreationForm()
    if request.method == "POST":
    # print("----------------------------------------------------------------------------")
        print("FILES : ", request.FILES['input_estimateimage'])
        print("----------------------------------------------------------------------------")
    # print("FILES : ", d['InMemoryUploadedFile'])
    # print("POST : ", request.POST)
    # print("----------------------------------------------------------------------------")
        out_11 = Output()
        견적서폼_post = ImageCreationForm(request.POST, request.FILES)
        if 견적서폼_post.is_valid():
            input_1 = request.FILES['input_estimateimage']
            print(input_1)
            process_1 = Process(input_1)
            out_11.list_11 = process_1.df()
            out_11.list_22 = process_1.construction()
            out_11.list_33 = process_1.detail()
            out_11.save()
        # return redirect("/estimate/test/")
    context = {
        "form": 견적서폼
    }
    return render(request, "estimateapp/create.html", context)

# class CreateEstimateView(CreateView):
#     model = EstimateModel
#     form_class = ImageCreationForm
#     template_name = 'estimateapp/create.html'
#     def get_success_url(self):
#         obj = EstimateModel.objects.get(pk=self.object.pk)
#         out_11 = Output()
#         input_1 = str(obj.input_estimateimage)
#         process_1 = Process(input_1)
#         # try:
#         out_11.list_11 = process_1.df()
#         out_11.list_22 = process_1.construction()
#         out_11.list_33 = process_1.detail()
#         out_11.save()
#         # except:
#         #     obj.delete()
#         # self.gitrequestfiles(self, request)
#         return reverse('estimateapp:detail', kwargs={'pk': self.object.pk})

class OutputImageView(DetailView):
   # model = EstimateModel
   model = Output
   context_object_name = 'target_image'
   template_name = 'estimateapp/detail.html'

def testview(request):
    return render(request, 'estimateapp/test.html')