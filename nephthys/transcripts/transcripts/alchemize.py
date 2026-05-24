from nephthys.transcripts.transcript import Transcript

class Alchemize(Transcript):
    """Transcript for Alchemize"""

    program_name: str = "Alchemize"
    program_owner: str = "U096RMRG03G"

    help_channel: str = "C0ASVK0HHEX"
    ticket_channel: str = "C0B22UW9FLG"
    team_channel: str = "C0AU2U67G0P"

    faq_link: str = ""
    first_ticket_create: str = """
    Heya! I'm The Alchemist who assigns helpers to your question! First off, have you read the faq, it answers a lot of common questions!
    if your question has been answered, please hit the button below to mark it as resolved!
    """
    ticket_create: str = "Someone should be along to help you soon. But in the meantime i suggest you read the faq to make sure your question hasn't already been answered. if it has been, please hit the button below to mark it as resolved :D"
    resolve_ticket_button: str = "Mark As Resolved"
    ticket_resolve: str = f"<@{{user_id}}> has marked this as resolved. Fell free to make a new post in <#{help_channel}>, if you have more questions."

    not_allowed_channel: str = f"Heya, it looks like you're not supposed to be in that channel, pls talk to <@{program_owner}> If that's wrong."
