#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <set>
#include <deque>
#include <algorithm>

using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define sqr(x) (x) * (x)
#define forn(i, l, r) for(int i = l; i < r; i ++)
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it ++)
#define y1 salnk
#define N 200100              
#define sz(a) (int)a.size()
#define ll long long
const int inf = (int)1e9;
const double pi = acos(-1.0);
const double eps = 1e-9;


int t, n;
double D, l, r, k[N], s[N];
int main () {
    //freopen("in", "r", stdin);
     cin >> t;
     int cs = 0;
     while (t--) {
      	cin >> D >> n;
      	double m = 0;

      	for (int i= 1; i <= n; i++) { 
      		cin >> k[i] >> s[i];
      	}
      	l = 0;
      	r = 1e16;
      	for (int it = 1; it <= 100; it++) {
      	 	double mid = (l + r) / 2;
      	 	bool bad = 0;
      	 	for (int i = 1; i <= n; i++) {
      	 	 	if (mid > s[i]) {
      	 	 	 	double t = k[i]/(mid - s[i]);
      	 	 	 	if ((mid * t) < D - eps) {
      	 	 	 		bad = true;
      	 	 	 		break;
      	 	 	 	}
      	 	 	}
               }
               if (!bad)
               	l = mid;
               else
               	r = mid;
      	}
      	cs++;
      	printf("Case #%d: %.7f\n",cs, l);
     }
     return 0;
}