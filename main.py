from discord_webhook import DiscordWebhook

webhookLink = input("Enter in your Discord Webhook Link:\n")
webhookName = input("Enter in the name that you would like the bot to be:\n")

print("When a colon shows up, you can start messaging")

while True:
    webhookContent = input(":")
    webhook = DiscordWebhook(url=webhookLink, username=webhookName, content=webhookContent)
    if webhookContent:
        response = webhook.execute()

