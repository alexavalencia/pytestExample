
import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckSearchPage

@pytest.mark.parametrize('phrase',['panda','python','polar bear'])
def test_basic_duckduckgo_search(browser,phrase):
    search_page=DuckDuckSearchPage(browser)
    result_page=DuckDuckGoResultPage(browser)
    PHRASE="panda"
    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"

    search_page.search(phrase)

    # Then the search result title contains "panda"
    assert  phrase in result_page.title()

    # And the search result query is "panda"
    assert  phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    title=result_page.result_link_title()
    matcher= [t for t in title if phrase.lower() in t.lower()]
    assert len(matcher) >0

    #raise  Exception("Incomplete test")