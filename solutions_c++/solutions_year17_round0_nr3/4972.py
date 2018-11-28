
//be naame khodaa

#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cassert>
#include <iomanip>
#include <cstring>
#include <sstream>
#define fi first
#define se second
#define rep(i, x, n) for (int i = x; i < n; i++)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
using namespace std;
typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> VI;

struct A{
	int L, R, p;
	A (int L, int R, int p) : L(L), R(R), p(p) {}
	bool operator < (A r) const {
		int x = min (L, R), y = max(L, R),
			xr = min (r.L, r.R), yr = max (r.L, r.R);
		if (x != xr) return x > xr;
		if (y != yr) return y > yr;
		return p < r.p;
	}
};

int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int it = 1; it <= t; it++){
		int n, k;
		cin >> n >> k;
		set <A> s;
		s.insert (A((n-1)/2, n/2, (n+1)/2));
		cout << "Case #" << it << ": ";
		for (int i = 0; i < k; i++){
			A bst = (*s.begin());
			s.erase(bst);
			if (i == k-1){
				cout << max(bst.L, bst.R) << ' ' << min(bst.L, bst.R) << '\n';
				break;
			}
			int L = bst.L, R = bst.R, p = bst.p;
			s.insert ( A((L-1)/2, L/2, p - (L/2+1)) );
			s.insert ( A((R-1)/2, R/2, p + (R+1)/2) );
		}
	}
	return 0;
}
