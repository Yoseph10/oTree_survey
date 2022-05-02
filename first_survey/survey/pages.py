from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):
    form_model = 'player'
    form_fields = [
        'name',
        'surname',
        'id_analyst'
    ]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Survey , ResultsWaitPage, Results]
