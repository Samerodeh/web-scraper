from web_scraper import __version__
from web_scraper.scraper import *
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_get_citations_needed_count():
    assert get_citations_needed_count

def test_get_citations_needed_report():
    assert test_get_citations_needed_report