#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>

using namespace std;

typedef unsigned uint;
//typedef long long ll;
typedef unsigned long long ll;

const int INF = 1001001001;
const ll INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }
double fin() { double x; scanf("%lf", &x); return x; }
ll lin() { ll x; scanf("%lld", &x); return x; }
struct point {
	int r;
	int h;
	ll rh;
};
point a[1005];
point b[1005];
const double pi = 3.14159265358979323846264; 
bool cmp(point x, point y) {
	return x.rh > y.rh;
}
bool cmp2(point x, point y) {
	return x.r > y.r;
}
void solve() {
	int n = in();
	int k = in();
	int r, h;
	for (int i= 0;i <n;i++) {
		a[i].r = in();
		a[i].h = in();
		a[i].rh = (ll)2 * a[i].r * a[i].h;
		
		/*b[i].r = in();
		b[i].h = in();
		b[i].rh = b[i].r * b[i].h;*/
		b[i].r = a[i].r;
		b[i].h = a[i].h;
		b[i].rh = (ll)2 * b[i].r * b[i].h;
	}
	sort(a, a + n, cmp);
	sort(b, b + n, cmp2);
	double ans = 0;
	for (int i = 0; i <= n - k; i++) {
		ll s = (ll)b[i].r * b[i].r + b[i].rh;
		int j = 0;
		bool used = true;
		int cnt = 0;
		while (cnt < k - 1 && j < n) {
			if (a[j].r == b[i].r) {
				if (used) {
					used = false;
				} else {
					s += a[j].rh;
					cnt++;
					//printf("%d = %d\n", i ,a[j]);
				}
			} else if (a[j].r < b[i].r) {
				s += a[j].rh;
				cnt++;
				//printf("%d %d\n", i, a[j]);
			}
			j++;
		}
		if (s > ans) {
			ans = s;
		}
	}
	printf("%.9f\n", ans * pi);
}

int main() {
  freopen("A-large.in","r", stdin);
  freopen("2","w", stdout);
  int T = in();

  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
