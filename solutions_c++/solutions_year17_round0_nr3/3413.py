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

struct stall {
	int i, j;
	int c;
	stall(){}
	stall(int i, int j, int c) {
		this->i = i;
		this->j = j;
		this->c = c;
	}
};

bool operator < (const stall& s1, const stall& s2) {
	if(s1.c < s2.c) return true;
	else if(s1.c > s2.c) return false;
	else if(s1.i > s2.i) return true;
	else if(s1.i < s2.i) return false;

	return false;
}

void answer(stall s, int mid) {
	int r = s.j-mid;
	int l = mid-s.i;

	cout << max(l, r) << " " << min(l, r) << endl;
}

int main() {
	cin.sync_with_stdio();

	int T;
	cin >> T;

	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		int n, k;
		cin >> n >> k;

		priority_queue<stall> st;
		st.push(stall(1, n, n));

		while(k > 0) {
			stall ss = st.top();
			st.pop();

		//	cout << ss.i << " " << ss.j << " " << ss.c << endl;

			int mid = (ss.i+ss.j)/2;

			if(k == 1) {
				answer(ss, mid);
				break;
			}

			stall s1(ss.i, mid-1, (mid-ss.i));
			stall s2(mid+1, ss.j, ss.j-mid);

			if(s1.i <= s1.j) st.push(s1);
			if(s2.i <= s2.j) st.push(s2);

			k--; 
		}
	}

	
}
















