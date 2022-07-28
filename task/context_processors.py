from .models import TaskSettings

def settings(request):
    return {'settings': TaskSettings.load()}
