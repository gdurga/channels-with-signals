import channels.layers
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Item


def core_message(self, event):
    message = event['message']
    # Send message to WebSocket
    self.send(text_data=json.dumps({
        'message': message
    }))


@receiver(post_save, sender=Item, dispatch_uid='send_signal_message')
def send_signal_message(sender, instance, **kwargs):
    message = "Item created by %s at %s" % (instance.autor, instance.create_time.ctime())

    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'core_group',
        {
            'type': 'core_message',
            'message': message
        }
    )
