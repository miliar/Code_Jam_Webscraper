#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;

int cb[1005]={0},n,c,m,r;
int amt[1005];

int get_amt(int k) {
	if(k < r) return -1;
	int ex = 0;
	int mn = 0;
	for(int i = n-1; i >= 0; --i) {
		int a = amt[i];
		if(a <= k) {
			ex -= min(ex,k-a);
		} else {
			ex += a-k;
			mn += a-k;
		}
	}
	if(ex != 0) return -1;
	return mn;
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		cin >> n >> c >> m;
		fill(cb,cb+c,0);
		fill(amt,amt+1005,0);
		for(int i = 0; i < m; ++i) {
			int b,p;
			cin >> p >> b;
			--b;--p;
			++cb[b];
			++amt[p];
		}
		r=0;
		for(int i = 0; i < c; ++i)
			r = max(r,cb[i]);

		int lo=r-1,hi=m+1;
		while(lo+1<hi) {
			int md = (lo+hi)/2;
			if(get_amt(md) == -1) lo = md;
			else hi = md;
		}
		cout << "Case #" << t << ": " << hi << " " << get_amt(hi) << "\n";
	}
	return 0;
}