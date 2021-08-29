# Put you code here
from django import template

register = template.Library()

@register.filter(name='persianalize')
def persian(value):
    nums = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
    }
    
    val = list(value)
    for i in range(len(val)):
        if val[i] in nums.keys():
            val[i] = nums[val[i]]
    return ''.join(val)
