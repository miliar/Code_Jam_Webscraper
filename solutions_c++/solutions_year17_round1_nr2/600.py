#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>

using namespace std;

void solve() {
	int n,p;
	cin >> n >> p;
	vector<int> r(n);
	for(int i = 0; i < n; i++) cin >> r[i];
	vector<vector<int> > q(n,vector<int>(p)),x,y;
	vector<vector<pair<int,int> > > xy(n);
	x = y = q;
	for(int i = 0; i < n; i++) 
	for(int j = 0; j < p; j++) {
		cin >> q[i][j];
	}
	for(int i = 0; i < n; i++) {
		sort(q[i].begin(),q[i].end());
		for(int j = 0; j < p; j++) {
			int u = q[i][j]*10;
			int v = r[i]*9;
			y[i][j] = u/v;
			v = r[i]*11;
			x[i][j] = u/v;
			if(u%v) x[i][j]++;
			if(x[i][j]==0) x[i][j]=1;
			xy[i].push_back(make_pair(x[i][j],y[i][j]));
			// cout << q[i][j] << " " << r[i] << " " <<  x[i][j] << " " << y[i][j] << ","; 
		}
		// cout << endl;
	}

	int res = 0;
	vector<int> id(n,0);
	for(;;) {
		bool flag = false;
		for(int i = 0; i < n; i++) {
			if(id[i]==p) flag = true;
		}
		if(flag) break;

		int mx,my;
		mx = xy[0][id[0]].first;
		my = xy[0][id[0]].second;
		for(int i = 0; i < n; i++) {
			mx = max(mx,xy[i][id[i]].first);
			my = min(my,xy[i][id[i]].second);
		}
		// cout << mx << " " << my << endl;
		if(mx<=my) {
			res++;
			for(int i = 0; i < n; i++) id[i]++;
		} else {
			int mi = 0;
			for(int i = 1; i < n; i++) if(xy[i][id[i]] < xy[mi][id[mi]]) mi = i;
			id[mi]++;
		}
	}

	cout << res << endl;
	

	
	
}

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		cout << "Case #" << t+1 << ": ";
		solve();
	}
}

