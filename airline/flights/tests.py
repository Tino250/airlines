from django.test import TestCase

# Create your tests here.
from .models import Airport,Flight,Passenger


class FlightTestCase(TestCase):
  

  def setUp(self):
    #create airports
    a1=Airport.objects.create(code="AAA",city="city A")
    a2=Airport.objects.create(code="BBB",city="city B")

    #create flights

    Flight.objects.create(origin=a1,destination=a2,duration=450)
    Flight.objects.create(origin=a1,destination=a1,duration=400)
    Flight.objects.create(origin=a1,destination=a2,duration=-100)
    