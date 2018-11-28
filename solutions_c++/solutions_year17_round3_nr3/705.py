#include <bits/stdc++.h>

#define sz(z) (int)z.size()
#define fo(i,a,b) for (auto (i) = (a); (i) < (b); (i)++)
#define mp make_pair
#define pb push_back

using namespace std;

#define DEBUG

#ifdef DEBUG
#define D(x...) printf(x)
#else
#define D(x...) 
#endif

typedef long long ll;
typedef pair<int,int> ii;

int main() {
	int t;
	scanf("%d\n", &t);
	for (int _ = 1; _ <= t; _++) {
		printf("Case #%d: ", _);
		long double U;
		int n, k;
		cin >> n >> k;
		cin >> U;
		vector <long double> v(123456);
		fo(i,0,n) {

			cin >> v[i];
		}
		long double lo, hi;
		lo = 0;
		hi = 1;
		while (hi - lo > 1e-9) {
			long double mi = lo + hi;
			mi /= 2;
			auto kek = U;
			fo(i,0,n) {
				if (v[i] < mi) {
					kek -= (mi-v[i]);
				}
			}
			if (kek >= 0) {
				lo = mi;
			} else {
				hi = mi;
			}
		}
		lo = 1;
		fo(i,0,n) {
			lo *= max(v[i], hi);;
		}
		printf("%.12Lf\n",lo);
	}

	
	return 0;
}
