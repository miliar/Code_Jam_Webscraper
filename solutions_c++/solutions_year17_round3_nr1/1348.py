#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include<math.h>

using namespace std;

#define forn(i,n) for(int i=0;i<n;++i)
#define frofn(i,n) for(int i=n-1;i>=0;--i)
#define out(a) {cout<<a;return 0;}

#define y1 ggggrrggtheryre
#define y2 fgtbirfbrbrbrge

#define maxn 100006

#define sqr(a) ((a)*(a))
#define AntonZuev  
#define fl fflush(stdout);

#define ll long long



const long double pi = 3.141592653589793238462643383279502884L;

ll d[1003][1003];

ll best[1004];

pair<ll, ll> pin[1003];
//#define _USE_MATH_DEFINES
int solve() {
	int n,k;
	for (int i = 0; i<= 1002;++i)
		best[i] = 0;

	cin >> n >> k;

	for (int i = 1;i <= n;++i)
		cin >> pin[i].first >> pin[i].second;

	sort(pin + 1, pin + n + 1);

	//for (int i = 1;i <= n;++i)
	//	d[1][i] = pin[i].first*pin[i].second;
	ll q;
	for (int i = 1;i <= n;++i) {
		for (int j = 1;j <= k;++j) {
			d[i][j] = best[j - 1];
			

			d[i][j] += pin[i].first*pin[i].second;
			
		}

		for (int j = 1;j <= k;++j)
			best[j] = max(best[j], d[i][j]);
	}

	ll bestres;
	for (int i = 1;i <= n;++i) {
		d[i][k] = (2*d[i][k] + pin[i].first*pin[i].first) * 1;
		bestres = max(bestres, d[i][k]);
	}

	cout << bestres*pi;

	return 0;
}



int main() {
#ifdef DEBUG
	// ifstream cin("input.txt");
	// ofstream cout("output.txt");
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	ios_base::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
#endif
	cout << fixed << setprecision(10);
	int t;
	cin >> t;
	forn(i,t) {
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}


}