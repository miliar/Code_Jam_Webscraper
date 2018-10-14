# !/usr/bin/python2.7
# -*- coding:utf-8 -*-

# By: Vasanthi Vuppuluri
# Last modified date: April 12, 2014

import copy

def optimal_war(N, Niaomi, Ken, ken_score, Niaomi_score, Niaomi_scores, war_scores):
	N = N
	Niaomi = Niaomi
	Ken = Ken
	ken_score = ken_score
	Niaomi_score = Niaomi_score
	Niaomi_scores = Niaomi_scores
	war_scores = war_scores

	while (N > 0):
			# WAR
			try:
				if([i for i in Ken if i > Niaomi[0]]):
					ken_2 = sorted([i for i in Ken if i > Niaomi[0]])
					k_chose = ken_2[0]
					Ken.remove(k_chose)
					Niaomi.remove(Niaomi[0])
					ken_score = ken_score + 1
					N = N -1
				
				else:
					ken_2 = sorted(Ken)
					k_chose = ken_2[0]
					Ken.remove(k_chose)
					Niaomi.remove(Niaomi[0])
					Niaomi_score = Niaomi_score + 1
					N = N -1
			
				Niaomi_scores.append(Niaomi_score)
			
				if ( N == 0):
					n = max(Niaomi_scores)
					war_scores.append(n)
			
			except:
				pass
	
	return war_scores

def deceitful_war(N_deceit, Niaomi_deceit, Ken_deceit, Niaomi_score_deceit, ken_score_deceit, Niaomi_scores_deceit, deceit_war_scores):

	N_deceit = N_deceit
	Niaomi_deceit = Niaomi_deceit
	Ken_deceit = Ken_deceit
	Niaomi_scores_deceit = Niaomi_scores_deceit
	ken_score_deceit = ken_score_deceit
	Niaomi_score_deceit = Niaomi_score_deceit
	deceit_war_scores = deceit_war_scores

	# DECEITFUL WAR
	while (N_deceit > 0):
		if ([j for j in Niaomi_deceit if j > max(Ken_deceit)]):
			Niaomi_2 = sorted([j for j in Niaomi_deceit if j > max(Ken_deceit)])
			Ken_deceit.remove(max(Ken_deceit))
			Niaomi_deceit.remove(min(Niaomi_2))
			Niaomi_score_deceit = Niaomi_score_deceit + 1
			N_deceit = N_deceit - 1
			
		elif ([j for j in Niaomi_deceit if j < max(Ken_deceit)]):
			Ken_deceit.remove(max(Ken_deceit))
			Niaomi_deceit.remove(min(Niaomi_deceit))
			ken_score_deceit = ken_score_deceit + 1
			N_deceit = N_deceit - 1
			
		Niaomi_scores_deceit.append(Niaomi_score_deceit)

		if ( N_deceit == 0):
			m = max(Niaomi_scores_deceit)
			deceit_war_scores.append(m)
	
	return	deceit_war_scores

def main():
	T = raw_input()
	T = int(T)

	war_scores = []
	deceit_war_scores = []
	
	for Case in xrange(0,T):
		N = raw_input()
		N = int(N)
		
		N_deceit = copy.deepcopy(N)

		Niaomi = raw_input()
		Niaomi = Niaomi.split()
		Niaomi = [float(i) for i in Niaomi]
		Niaomi_deceit = copy.deepcopy(Niaomi)
		
		Ken = raw_input()
		Ken = Ken.split()
		Ken = [float(i) for i in Ken]
		Ken_deceit = copy.deepcopy(Ken)

		ken_score = 0
		Niaomi_score = 0
		ken_score_deceit = 0
		Niaomi_score_deceit = 0

		Niaomi_scores = []
		Niaomi_scores_deceit = []

		dws = deceitful_war(N_deceit, Niaomi_deceit, Ken_deceit, Niaomi_score_deceit, ken_score_deceit, Niaomi_scores_deceit, deceit_war_scores)
		ws = optimal_war(N, Niaomi, Ken, ken_score, Niaomi_score, Niaomi_scores, war_scores)

	for i in xrange(0, T):
		print 'Case #%d: %d %d' %(i+1, dws[i], ws[i])

if __name__ == "__main__":
    main()