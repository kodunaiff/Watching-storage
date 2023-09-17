from django.utils import timezone
import time


def get_duration(visit):
  if not visit.leaved_at:
    duration = timezone.now()-visit.entered_at
    return duration.total_seconds()
  duration = visit.leaved_at-visit.entered_at
  return duration.total_seconds()

def format_duration(duration):
  time_format = time.strftime("%H:%M:%S", time.gmtime(duration))
  return time_format
  
def is_visit_long(visit, minutes=60):
  duration = get_duration(visit)//60
  res_suspect = duration > minutes
  return res_suspect
  