#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <cmath>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cstring>
using namespace std;

#define rep(i,a) for(int i=0; i<a;i++)
#define repd(i,a) for(int i=a - 1; i>= 0;i--)
#define forn(i,a,b) for(int i=a;i<b;i++)
#define ford(i,a,b) for(int i=a; i>=b; i--)
#define repl(i,a) for(long long unsigned i=0; i<((long long unsigned) a);i++)
#define repdl(i,a) for(long long unsigned i=((long long unsigned) a) - 1; i >= 0;i--)
#define fornl(i,a,b) for(int i=((long long unsigned) a);i<((long long unsigned) b);i++)
#define fornld(i,a,b) for(int i=((long long unsigned) a);i>= ((long long unsigned) b);i--)
#define mp make_pair
#define ll long long unsigned
#define sz(x) (x).size()
#define pb push_back
#define endl '\n'
#define vi vector<int>
#define ii pair<int, int>

template <typename T>
  string NumberToString ( T Number ) {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }

ll ex(ll a, ll b) {
	if (b == 0) return 1;
	if (b % 2) return a * ex(a, b - 1);
	ll c = ex(a, b / 2);
	return c * c;
}

int data[1024];
int d;

int solve_rec(int s, int k, int c, int l) {
	//cout << bitset<10>(s) << " " << dec << k << " " << c << " " << d << " " << l << endl;
	if (data[s] < c) return 1000;
	data[s] = c;
	
	if ((s&(s+1)) == 0 && (s & (1<<(d-1)))) return c;
	
	if (c > 10) return 1000;
	
	int res = 1000;
	rep(i, d-k+1) {
		if (i == l) continue;
		int bs = s;
		forn(j, i, i+k) bs ^= (1<<(d-j-1));
		res = min(res, solve_rec(bs, k, c + 1, i));
	}
	//cout << bitset<10>(s) << " " << res << endl;
	return res;
}

int solve(int s, int k) {
	if ((s&(s+1)) == 0 && (s & (1<<(d-1)))) return 0;
	//cout << (s&(s+1)) << endl;
	int res = 1000;
	rep(i, d-k+1) {
		int bs = s;
		forn(j, i, i+k) bs = bs ^ (1<<(d-j-1));
		res = min(res, solve_rec(bs, k, 1, i));
	}
	return res;
}

int main() {
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	
	int t;
	cin >> t;
	rep(tc, t) {
		int k;
		string s;
		cin >> s >> k;
		d = sz(s);
		cout << "Case #" << tc + 1 << ": ";
		
		rep(i, 1024) data[i] = 1000;
		
		int bm = 0;
		rep(i, sz(s)) if (s[i] == '+') bm |= (1<<(sz(s)-i-1));
		
		int res = solve(bm, k);
		//cout << res << endl;
		if (res < 1000) cout << res << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	
	return 0;
}
