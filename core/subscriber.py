class Subscriber:
    """
    Class for the app subscribers

    requirements:
    Individuals registered with the program identify themselves
    with their membership card ID at any place to check out a scooter

    """
    def __init__(self, subscriber_id, card_id):
        self.subscriber_id = subscriber_id
        self.card_id = card_id

    def __str__(self):
        return f"Subscriber {self.subscriber_id} (Card {self.card_id})"