#include <iostream>
#include <vector>
#include <utility>
#include <iterator>
#include <algorithm>
#include <string>

using namespace std ;

typedef vector<bool>::iterator iter ;

pair<bool, int> count_flip (iter start, iter end, int k) {
	pair<bool, int> res (false, 0);
	iter stop = end - k ;
	while (start != stop) {
		if (!(*start)) {
			iter local_it = start ;
			iter local_stop = start + k ;
			for (local_it ; local_it != local_stop ; local_it++) {
				*local_it = !(*local_it) ;
			}
			res.second ++ ;
			start ++ ;
		}
		else {
			while (*start && start != stop) { start ++ ; }
		}
	}
	if (!(*start)) res.second ++ ;
	bool temp = *start ;
	res.first = *start ;
	for (start ; start != end ; start++) {
		if (*start != temp) {
			res.first = false ;
			return res ;
		}
		else res.first = true ;
	}
	return res ;
}

string display (pair<bool, int> p) {
	if (p.first == false) return "IMPOSSIBLE" ;
	else return to_string(p.second) ;
}

int main (void) {
	int test_nb ;
	cin >> test_nb ;
	for (int i=0 ; i<test_nb ; i++) {
		string list ; const char* p_list ; vector<bool> vect ; int k ; string out ;
		cin >> list >> k ;
		p_list = list.c_str() ; ;
		for (int j=0 ; j<list.size() ; j++) {
			if (*(p_list + j) == '+') vect.push_back(true) ;
			else vect.push_back(false) ;
		}
		out = "Case #" ;
		out += to_string(i+1) ;
		out += ": " ;
		cout << out ;
		cout << display(count_flip(vect.begin(), vect.end(), k)) ;
		cout << endl ;
	}

	return 0 ;
}