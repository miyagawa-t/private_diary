import logging
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .forms import InquiryFrom

# ロガー
logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryFrom
    success_url = reverse_lazy('diary:inquiry')

    # バリデーション
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
