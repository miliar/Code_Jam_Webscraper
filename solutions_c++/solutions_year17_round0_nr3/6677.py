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

pair<int, int> solve(int n) {
	return mp((n-1)/2, n/2);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int t;
	cin >> t;
	rep(tc, t) {
		int n, k;
		cin >> n >> k;
		cout << "Case #" << tc + 1 << ": ";
		
		priority_queue<int> pq;
		pq.push(n);
		pair<int, int> sol;
		
		repd(d, k) {
			int sn = pq.top(); pq.pop();
			sol = solve(sn);
			pq.push(sn/2);
			pq.push((sn-1)/2);
		}
		
		int a = sol.first, b = sol.second;
		cout << max(a,b) << " " << min(a, b)<< endl;
	}
	
	return 0;
}
