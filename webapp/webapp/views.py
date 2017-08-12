from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated():
        return render(request, 'home.html', {})
    return render(request, 'index.html', {})


def bad_request(request):
    # HTTP Error 400
    return render(request, '400.html', status=400)


def permission_denied(request):
    # HTTP Error 403
    return render(request, '403.html', status=403)


def page_not_found(request):
    # HTTP Error 404
    return render(request, '404.html', status=404)


def server_error(request):
    # HTTP Error 500
    return render(request, '500.html', status=500)
