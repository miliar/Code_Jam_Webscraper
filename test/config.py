from webscraper.config import *

# used for testing orchestra
PROBLEM_LIST = [('08', 0, 1, SAVE_PATH + 'solutions_year08_round0_nr1'),
                ('08', 1, 1, SAVE_PATH + 'solutions_year08_round1_nr1'),
                ('08', 1, 2, SAVE_PATH + 'solutions_year08_round1_nr2'),
                ('10', 0, 1, SAVE_PATH + 'solutions_year10_round0_nr1'),
                ('17', 0, 1, SAVE_PATH + 'solutions_year17_round0_nr1'),
                ('17', 0, 2, SAVE_PATH + 'solutions_year17_round0_nr2')
                ]
VALID_URL = ('https://www.go-hero.net/jam/08/solutions/0/1/' + LANGUAGE,
             'https://www.go-hero.net/jam/08/solutions/1/1/' + LANGUAGE,
             'https://www.go-hero.net/jam/08/solutions/1/2/' + LANGUAGE,
             'https://www.go-hero.net/jam/10/solutions/0/1/' + LANGUAGE,
             'https://www.go-hero.net/jam/17/solutions/0/1/' + LANGUAGE,
             'https://www.go-hero.net/jam/17/solutions/0/2/' + LANGUAGE,
             )


# used for testing scraper
DOWNLOAD_LINKS = [
    'https://code.google.com/codejam/contest/scoreboard/do?cmd=GetSourceCode&contest=32013&problem=24480&io_set_id=1&username=xyx',
    'https://code.google.com/codejam/contest/scoreboard/do?cmd=GetSourceCode&contest=32013&problem=24480&io_set_id=1&username=Fj.',
    'https://code.google.com/codejam/contest/scoreboard/do?cmd=GetSourceCode&contest=32013&problem=24480&io_set_id=1&username=Shinigami',
    'https://code.google.com/codejam/contest/scoreboard/do?cmd=GetSourceCode&contest=32013&problem=24480&io_set_id=1&username=Galt',
    'https://code.google.com/codejam/contest/scoreboard/do?cmd=GetSourceCode&contest=32013&problem=24480&io_set_id=1&username=Chirono',
    'https://code.google.com/codejam/contest/scoreboard/do?cmd=GetSourceCode&contest=32013&problem=24480&io_set_id=1&username=alexk'
]
DOWNLOAD_LINKS_NR = [0, 50, 99, 100, 110, 199]
OFFLINE_MAIN_PAGE = 'https://www.go-hero.net/jam/08/solutions/0/1/' + LANGUAGE
OFFLINE_SUB_PAGE = f'https://www.go-hero.net/jam/08/solutions/0/1/{LANGUAGE}/partial/1'
