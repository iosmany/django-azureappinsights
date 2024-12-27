

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import logging  


# Create a logger for the 'django' module
logger = logging.getLogger(__name__)

def home(request: HttpRequest) -> HttpResponse:
    logger.info('Home page request')
    logger.debug('Home page request')
    logger.warning('Home page request')

    try:
        raise ValueError('This is a test error')
    except ValueError as e:
        logger.exception(e)

    return render(request, 'home.html')