from .models import *
from django.db.models import Sum, Q, Count, F


def query_0():
    q = Driver.objects.all()
    return q


def query_1():
    """
    :return: Something like {'income': value }
    """
    q = Payment.objects.aggregate(income=Sum('amount'))
    return q


def query_2(x):
    """
    :return: Something like {'payment_sum': value }
    """
    q = Payment.objects.filter(ride__request__rider__id=x).aggregate(
        payment_sum=Sum('amount'))
    return q


def query_3():
    """
    :return: Just a number
    """
    q = Car.objects.filter(car_type='A').values('owner').distinct().count()
    return q


def query_4():
    q = RideRequest.objects.filter(ride=None)
    return q


def query_5(t):
    q = Rider.objects.annotate(total=Sum('riderequest__ride__payment__amount')).filter(
        total__gte=t
    )
    return q


def query_6():
    """
    :return: Account object
    """
    q = Account.objects.annotate(car_total=Count(
        'drivers__car')).order_by('-car_total', 'last_name')[0]
    return q


def query_7():
    q = Rider.objects.filter(riderequest__ride__car__car_type='A').annotate(
        n=Count('riderequest__ride'))
    return q


def query_8(x):
    q = Driver.objects.filter(
        car__model__gte=x).distinct().values('account__email')
    return q


def query_9():
    q = Driver.objects.annotate(n=Count('car__ride'))
    return q


def query_10():
    i = Account.objects.values('first_name').distinct()
    q = Driver.objects.filter(account__first_name__in=i).values(
        'account__first_name').distinct().annotate(n=Count('car__ride'))
    return q


def query_11(n, c):
    q = Driver.objects.filter(
        Q(car__color=c) & Q(car__model__gte=n)).distinct()
    return q


def query_12(n, c):
    i1 = Car.objects.filter(model__gte=n).values_list(
        'owner', flat=True).distinct()
    i2 = Car.objects.filter(color=c).values_list('owner', flat=True).distinct()

    q = Driver.objects.filter(Q(pk__in=i1) & Q(pk__in=i2))
    return q


def query_13(n, m):
    """
    :return: Something like {'sum_duration': value }
    """
    q = Ride.objects.filter(Q(request__rider__account__first_name=m) & Q(
        car__owner__account__first_name=n)).aggregate(sum_duration=Sum(F('dropoff_time')-F('pickup_time')))
    return q
