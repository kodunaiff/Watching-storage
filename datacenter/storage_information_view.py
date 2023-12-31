from datacenter.models import Visit
from django.shortcuts import render
from datacenter.functions_visits import get_duration, format_duration


def storage_information_view(request):
    non_closed_visits = []

    active_visits = Visit.objects.filter(leaved_at=None)
    for visit in active_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': formatted_duration,
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
