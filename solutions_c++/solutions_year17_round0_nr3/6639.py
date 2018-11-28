#include <iostream>
#include <set>
#include <cmath>

using namespace std;

typedef unsigned long long int lint;

void calc_last_free_stall(const lint N, const lint K, 
						  lint & max, lint & min);
lint find_best_loc(const set<lint> & stalls, lint & max, lint & min);

int main() {
	
	int T;
	lint K = 0ULL, N = 0ULL, max = 0ULL, min = 0ULL;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> N >> K;
		cout << "Case #" << i << ": ";
		calc_last_free_stall(N,K,max,min);	
		cout << max << " " << min << endl;
	}
	
	return 1;
}

/*
 * Calculates the last person's min(Ls,Rs), max(Ls,Rs)
 * 
 */
void calc_last_free_stall(const lint N, const lint K, 
						  lint & max, lint & min) {
	set<lint> pos_taken_stalls;
	lint idx = 0;
	pos_taken_stalls.insert(0);
	pos_taken_stalls.insert(N+1);
	// calculate best stall and give it its value
	for (lint i = 0; i < K; i++) {
		// ith person has to make a decision
		// calculate max difference between set entries
		idx = find_best_loc(pos_taken_stalls, max, min);
		pos_taken_stalls.insert(idx);
	}
}

/*
 * Find the maximum seperation between stalls
 * and pick the point in the centre if odd 
 * if even, then pick the one on the left
 */
lint find_best_loc(const set<lint> & stalls, lint & max, lint & min) {
	
	lint ls = 0, rs = 0, diff = 0;
	lint max_diff = 0;
	lint last_val = 0;
	lint last_best_val = 0; // the stall before best location to place
	lint next_stall_loc = 0;
	for (set<lint>::iterator it = stalls.begin(); it!= stalls.end(); ++it) {
		diff = fmax(0,(*it) - 1 - last_val);
		//cout << (*it) << " " << diff << endl;
		last_val = *it;
	    if (diff > max_diff) {
	    	max_diff = diff;
	    	last_best_val = *it - diff - 1;
	    }
	}
	if (max_diff % 2 == 1)
		ls = rs = max_diff/2;
	else {
		ls = rs = max_diff/2;
		ls--;
	}	    		
	next_stall_loc = last_best_val + ls + 1;
	max = fmax(ls,rs);
	min = fmin(ls,rs);
	return next_stall_loc;
}