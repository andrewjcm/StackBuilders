from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import get_repos


@api_view(http_method_names=['GET'])
def github_repos_view(request):
    repos = get_repos()
    return Response(repos)
