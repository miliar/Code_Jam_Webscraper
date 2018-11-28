#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

map<pair<vector<int>, int>, int> was;


int solve(vector<int> a, int p) {
	if (a.size() == 0) return 0;
	sort(a.begin(), a.end());
	if (was.find(mp(a, p)) != was.end()) return was[mp(a, p)];
	int sum = 0;
	for (int i = 0; i < a.size(); i++) sum = (sum + a[i]) % p;

	int be = 0;
	for (int i = 0; i < a.size(); i++) {
		if (i > 0 && a[i] == a[i - 1]) continue;
		vector<int> b = a;
		b.erase(b.begin() + i);
		int ret = solve(b, p);
		if ((sum - a[i] + p) % p == 0) ret++;
		be = max(be, ret);
	}
	return was[mp(a, p)] = be;
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		vector<int> r;
		int n, p;
		cin >> n >> p;
		for (int i = 0; i < n; i++) {
			int x;
			cin >> x;
			r.pb(x % p);
		}
		cout << "Case #" << tt << ": " << solve(r, p) << endl;
		cerr << tt << endl;

	}
	return 0;
}