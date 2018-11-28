#ifndef __MYLIB_H
#define __MYLIB_H

#include<iostream>
#include<algorithm>
#include<sstream>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<utility>  // pair, make_pair
#include<cstdio>
#include<cmath>
#include<cstring>
#include<climits>
using namespace std;

typedef stringstream sstream;

#define all(vec)    vec.begin(),vec.end()
#define rall(vec)    vec.rbegin(),vec.rend()
#define sz(r)      r.size()
#define rem1(v, i)    (v.erase(v.begin()+i))
#define rem2(v, i, j)  (v.erase(v.begin()+i, v.begin()+j+1))
#define num_bits(num)       __builtin_popcount(num)
#define inf   INT_MAX

#endif 

/* End of my lib */ 

string order(string s) {
	int n = s.size();

	int i = 1;
	while(i < n) {
		if(s[i] < s[i-1]) break;

		i++;
	}

	if(i >= n) {
		return s;
	}
	else {
		int j = i-1;
		while(s[j] == '0') s[j--] = '9';
		s[j]--;

		for(int j = i; j < n; j++) s[j] = '9'; 

		if(s[0] == '0') s = s.substr(1);

		return order(s);
	}
}

int main() {
	cin.sync_with_stdio();

	int T;
	cin >> T;

	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		string s;
		cin >> s;
		
		cout << order(s) << endl;
	}

	
}
















