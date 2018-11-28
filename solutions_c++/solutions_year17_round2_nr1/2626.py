/*
  /\     /\
  | ).|.( |
  |  >-<  |
  =========
It's AdilkhanKo miaaaaaau
*/
#include<bits/stdc++.h>

#define ll long long
#define pb push_back
#define endl "\n"
#define foreach(it, S) for(__typeof (S.begin()) it = S.begin(); it != S.end(); it++)
#define mp make_pair
#define f first
#define s second
#define name ""
#define _ ios_base::sync_with_stdio(false);cin.tie(0);

using namespace std;

const int maxn = int (2e6) + 256;
const ll INF = (ll)(1e18);
const int mod = 1e9+7;
const double pi = 3.1415926535897932384626433832795;
const double eps = (1e-15);


int main () {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int test = 1; t--; test++) {
		printf("Case #%d: ", test);
		int d, n;
		scanf("%d%d", &d, &n);
		double mn = 0;
		for(int i = 0; i < n; i++) {
			int k, s;
			scanf("%d%d", &k, &s);
			mn = max(mn, (d - k) * 1. / s);
		}
		printf("%.10lf\n", d / mn);
	}

	return 0;
}
