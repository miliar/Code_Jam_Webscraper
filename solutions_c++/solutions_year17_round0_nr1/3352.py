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

int main() {
	cin.sync_with_stdio();

	int T;
	cin >> T;

	for(int t = 1; t <= T; t++) {

		int k;
		string s;
		cin >> s >> k;

		int n = s.size();

		long long cnt = 0;
		vector<int> nxt;

		for(int i = 0; i < n; i++) {

			int a = lower_bound(nxt.begin(), nxt.end(), i)-nxt.begin();

			//cout << "-> ";
			//for(int x = 0; x < nxt.size(); x++) cout << nxt[x] << " ";
			//cout << endl;
			//cout << i << " " << a << " " << nxt.size() << endl;

			if(nxt.size() == 0) a = -1;
			else a = nxt.size()-a;

			if(a > 0 && a%2 != 0) {
				s[i] = (s[i] == '-') ? '+' : '-';
			}

			if(s[i] == '-' && (i+k) <= n) {
				s[i] = '+';
				nxt.push_back(i+k-1);
				cnt++;
			}
		}

		for(int i = 0; i < n; i++) {
			if(s[i] == '-') cnt = -1;
		}

		cout << "Case #" << t << ": ";
		if(cnt == -1) cout << "Impossible" << endl;
		else cout << cnt << endl;
	}
}
















