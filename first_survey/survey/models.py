from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Yoseph Ayala Valencia'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name =  models.StringField(
            label = "What is your name?"
    )

    surname = models.StringField(
            label = "What is your surname?"
    )

    id_analyst = models.IntegerField(
            label = "What is your ID?"
    )
