# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


@login_required(login_url="/login/")
def index(request):
    context = {
        'segment': 'index',
        'images': [
            '/static/assets/img/slider/Slider_1.png',
            '/static/assets/img/slider/Slider_2.png',
            '/static/assets/img/slider/Slider_3.png',
            '/static/assets/img/slider/Slider_4.png',
            '/static/assets/img/slider/Slider_5.png',
            '/static/assets/img/slider/Slider_6.png',
            '/static/assets/img/slider/Slider_7.png',
            '/static/assets/img/slider/Slider_8.png',
            '/static/assets/img/slider/Slider_9.png',
            # 'https://i.pinimg.com/736x/12/0a/19/120a19f48643da6eb1b731d225940be1.jpg',
            # 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlYoEHlpLK3lpeGZQKma22oig__WZrJbBPqQ&s',
            # 'https://static1.bigstockphoto.com/5/1/8/large1500/8158126.jpg',
            # 'https://img.freepik.com/premium-photo/vector-image-loin_1057389-70778.jpg?w=1060'
        ],
        'categories': [
            {'name': 'WHOLE SALE', 'icon': 'whole-sale'},
            {'name': 'NEW ARRIVALS', 'icon': 'new-arrival', 'subcategories': [
                {'name': 'SHIRTS', 'icon': 'shirt'},
                {'name': 'DUPATTAS', 'icon': 'shawl'},
                {'name': 'TROUSERS', 'icon': 'trouser'}
            ]},
            {'name': 'SALE', 'icon': 'sale', 'subcategories': [
                {'name': 'SHIRTS', 'icon': 'shirt'},
                {'name': 'DUPATTAS', 'icon': 'shawl'},
                {'name': 'TROUSERS', 'icon': 'trouser'}
            ]},
            {'name': 'SUMMER COLLECTION', 'icon': 'summer'},
            {'name': 'WINTER COLLECTION', 'icon': 'winter'},
            {'name': 'SHIRTS', 'icon': 'shirt'},
            {'name': 'DUPATTAS', 'icon': 'shawl'},
            {'name': 'TROUSERS', 'icon': 'trouser'},
        ],
        'socials': [
            {'name': 'Facebook', 'icon_color': 'info', 'color': 'blue', 'icon': 'facebook'},
            {'name': 'Instagram', 'icon_color': 'purple', 'color': 'purple', 'icon': 'instagram'},
            {'name': 'YouTube', 'icon_color': 'danger', 'color': 'red', 'icon': 'youtube'},
            {'name': 'TikTok', 'icon_color': 'primary', 'color': 'black', 'icon': 'tiktok'},
            {'name': 'Twitter', 'icon_color': 'info', 'color': '#00AAEB', 'icon': 'twitter'},
            {'name': 'SnapChat', 'icon_color': 'secondary', 'color': '#f0bc74', 'icon': 'snapchat'},
            {'name': 'Others', 'icon_color': 'primary', 'color': 'black', 'icon': 'social'}
        ]
    }

    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {
        'categories': [
            {'name': 'WHOLE SALE', 'icon': 'whole-sale'},
            {'name': 'NEW ARRIVALS', 'icon': 'new-arrival', 'subcategories': [
                {'name': 'SHIRTS', 'icon': 'shirt'},
                {'name': 'DUPATTAS', 'icon': 'shawl'},
                {'name': 'TROUSERS', 'icon': 'trouser'}
            ]},
            {'name': 'SALE', 'icon': 'sale', 'subcategories': [
                {'name': 'SHIRTS', 'icon': 'shirt'},
                {'name': 'DUPATTAS', 'icon': 'shawl'},
                {'name': 'TROUSERS', 'icon': 'trouser'}
            ]},
            {'name': 'SUMMER COLLECTION', 'icon': 'summer'},
            {'name': 'WINTER COLLECTION', 'icon': 'winter'},
            {'name': 'SHIRTS', 'icon': 'shirt'},
            {'name': 'DUPATTAS', 'icon': 'shawl'},
            {'name': 'TROUSERS', 'icon': 'trouser'},
        ],
        'items': [
            {'name': 'Item 1', 'img': '/static/assets/img/slider/demo-item.png', 'price': '1,000', 'discount': '5', 'actual_price': '1,200', 'short_description': 'Last Campaign Performance'},
            {'name': 'Item 2', 'img': '/static/assets/img/slider/demo-item.png', 'price': '2,500', 'discount': '5', 'actual_price': '2,200', 'short_description': 'Last Campaign Performance'},
            {'name': 'Item 3', 'img': '/static/assets/img/slider/demo-item.png', 'price': '4,500', 'discount': '11', 'actual_price': '21,200', 'short_description': 'Last Campaign Performance'},
            {'name': 'Item 4', 'img': '/static/assets/img/slider/demo-item.png', 'price': '3,300', 'discount': '15', 'actual_price': '41,200', 'short_description': 'Last Campaign Performance'},
            {'name': 'Item 5', 'img': '/static/assets/img/slider/demo-item.png', 'price': '14,000', 'discount': '40', 'actual_price': '15,200', 'short_description': 'Last Campaign Performance'},
        ]
    }
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        # import pdb; pdb.set_trace()

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
