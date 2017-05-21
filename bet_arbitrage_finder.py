import time
import sys
from selenium import webdriver

##basic calculations of how the odds stack up
def arb(info):
	arbs = []
	for x in info[1::2]:
		arb = ((1.0/x)*100.0)
		arbs.append(arb)
	total = sum(arbs)
	if total == 0:
		return
	profit = (10.0/(total/100.0))-10.0
	bets = list(map(lambda x: (10*x)/total, arbs))
	#ignore anything that we can't arbitrage
	if total < 99:
		print("\n info:")
		print info 
		print("\n arbs:")
		print arbs 
		print("\n bets:") 
		print bets 
		print("\n profit: \n" + str(profit) + "\n")

#allow command line arguments if you want to quickly check a specific sport	
if len(sys.argv) > 1:
	sports = sys.argv[1:]
#otherwise use default list of sports to check
else: 
	sports = ['https://www.oddschecker.com/baseball/mlb','https://www.oddschecker.com/football','https://www.oddschecker.com/tennis/atp-rome',
	'https://www.oddschecker.com/basketball/nba', 'https://www.oddschecker.com/football/english/premier-league', 'https://www.oddschecker.com/football/english/championship',
	'https://www.oddschecker.com/football/english/league-1', 'https://www.oddschecker.com/football/english/league-2', 'https://www.oddschecker.com/football/english/fa-cup',
	'https://www.oddschecker.com/football/elite-coupon', 'https://www.oddschecker.com/football/france/ligue-2', 'https://www.oddschecker.com/football/champions-league',
	'https://www.oddschecker.com/football/europa-league', 'https://www.oddschecker.com/football/womens-coupon','https://www.oddschecker.com/american-football/nfl',
	'https://www.oddschecker.com/australian-rules/afl', 'https://www.oddschecker.com/badminton', 'https://www.oddschecker.com/boxing', 'https://www.oddschecker.com/ufc-mma',
	'https://www.oddschecker.com/gaelic-games/gaelic-football','https://www.oddschecker.com/handball/handball-coupon', 'https://www.oddschecker.com/hockey/all-matches',
	'https://www.oddschecker.com/rugby-league/match-coupon','https://www.oddschecker.com/rugby-league/handicaps-coupon','https://www.oddschecker.com/rugby-union/match-coupon',
	'https://www.oddschecker.com/rugby-union/handicaps-coupon', 'https://www.oddschecker.com/rugby-union/european-champions-cup', 'https://www.oddschecker.com/rugby-union/lions-tour',
	'https://www.oddschecker.com/cricket/ipl','https://www.oddschecker.com/ice-hockey/nhl','https://www.oddschecker.com/tennis/itf-futures',
	'https://www.oddschecker.com/tennis/challenger-tour','https://www.oddschecker.com/tennis/wta-rome','https://www.oddschecker.com/football/football-coupons/over-under-2.5',
	'https://www.oddschecker.com/football/football-coupons/over-under-1.5', 'https://www.oddschecker.com/football/football-coupons/over-under-0.5', 
	'https://www.oddschecker.com/football/football-coupons/both-teams-to-score']

driver = webdriver.Chrome('')  # Optional argument, if not specified will search path.

for sport in sports: 
	driver.get(sport)
	markets = driver.find_elements_by_class_name('match-on') 
	print "\n----------------------------\n" + sport + "\n----------------------------\n"
	for m in markets:
		match_data = []
		infos = m.find_elements_by_tag_name('td')
		for i in infos:
			if i.get_attribute('data-best-odds'):
				match_data.append((i.find_element_by_class_name('fixtures-bet-name').get_attribute('innerHTML')))
				match_data.append(float(i.get_attribute('data-best-odds')))
		arb(match_data)		

print "finished!"
driver.quit()
