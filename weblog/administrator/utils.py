from django.shortcuts import redirect,render
from django.shortcuts import get_object_or_404

class ObjectCreateMixin:
    template_name = ""
    form = None
    
    def get(self,request):
        return render(request,self.template_name,{'form':self.form()})
    
    def post(self,request):
        new_object = self.form(request.POST)
        if new_object.is_valid():
            new_object = new_object.save()
            return redirect(new_object)
        else:
            return render(request,self.template_name,{'form':new_object})
    
class ObjectupdateMixin:
    template_name= ''
    form = None
    model= ""
    
    def get(self,request,*args, **kwargs):
        for k in self.kwargs.keys():
            if k == 'tagname':
                the_object = self.kwargs['tagname']
                get_object = get_object_or_404(self.model,tag_name=the_object)
                my_context = {'form': self.form(instance=get_object),
                                    'post': get_object}
                return render(request,self.template_name,my_context)
            elif self.kwargs['logtitle'] and self.kwargs['seconds']:
                logtitle = self.kwargs['logtitle']
                seconds = self.kwargs['seconds']
                get_object = get_object_or_404(self.model,userlogtitle__iexact=logtitle,datecreated__second=seconds)
                my_context = {'form': self.form(instance=get_object),
                                    'post': get_object}
                return render(request,self.template_name,my_context)
                
        
    # def get(self,request,*args,**kwargs):
    #     pass
     
    def post(self,request,*args, **kwargs):
        get_object =get_object_or_404(self.model,*args, **kwargs)
        bound_form=self.form(request.POST,instance=get_object) 
        if bound_form.is_valid():
            update_object=bound_form.save()
            return redirect(update_object)
        
        else:
            return render(request,self.model,{'form' : self.form(instance=get_object)})
             
         
         
         
            