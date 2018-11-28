#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

int K;
string S;
int F[1005];
bool possible;
int resp;

int range_sum(int st, int en) {
	int i, res = 0;
	for(i=st;i<en;++i)
		res = (res + F[i]) % 2;
	return res;
}

bool process() {
	resp = 0;
	int i, j, test, sz, st, en, d, last_st = -1, last_en = -1, last_d = -1;
	sz = S.length();
	
	F[0] = (S[0]=='-');
	resp += F[0];
	
	//cout << "Processing... F[0] = " << F[0] << endl;
	
	for(i=1;i<sz;++i) {
		st = max(0, i-K+1); en = min(i, sz-K+1); d = (S[i]=='-');
		//cout << "Now at " << i << "...  Influence range st = " << st << " | en = " << en << " | d = " << d << endl;
		if (st == last_st && en == last_en && d != last_d) {
			//cout << "ERROR: Same equation different expected result" << endl;
			return false; //IMPOSSIBLE
		}
		if (i < sz-K+1) {
			//New info!
			F[i] = (d + range_sum(st, en)) % 2;
			//cout << "F[" << i << "] = " << F[i] << endl;
			resp += F[i];
		} else {
			//Just test it
			//cout << "Cannot flip " << i << ", testing ... ";
			test = 0;
			for(j = st; j < en; ++j) test = (test + F[j]) % 2;
			//cout << "got " << test << " expected " << d << endl;
			if (test != d) return false; //U broke it!
		}
		
		last_st = st; last_en = en; last_d = d;
	}
}

int main() {
	int tc, t;
	cin >> t;
	for(tc=1; tc <= t; ++tc) {
		cin >> S >> K;
		
		possible = process();
		
		if (possible) {
			cout << "Case #" << tc << ": " << resp << endl;
		} else {
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
		}
		memset(F, 0, sizeof(F));
	}
	return 0;
}