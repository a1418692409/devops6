# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def Index(request):
    return render(request, 'dashboard/index.html')
