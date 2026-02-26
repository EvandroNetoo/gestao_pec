from django.shortcuts import render
from django_htmx.http import HttpResponseClientRedirect


class NoRequiredAttrFormMixin:
    """Remove o atributo HTML5 'required' de todos os campos do formulário."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('use_required_attribute', False)
        super().__init__(*args, **kwargs)


class HtmxFormViewMixin:
    """Mixin para CBVs que retorna apenas o formulário re-renderizado via HTMX."""

    def form_invalid(self, form):
        return render(
            self.request,
            'components/django_form/index.html',
            {'form': form},
        )

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponseClientRedirect(self.get_success_url())
