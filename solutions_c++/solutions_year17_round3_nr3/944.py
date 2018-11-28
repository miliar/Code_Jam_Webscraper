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
typedef long long ll;
typedef unsigned long long UInt;

const int INF = 1001001001;
const ll INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }
double fin() { double x; scanf("%lf", &x); return x; }
ll lin() { ll x; scanf("%lld", &x); return x; }

double a[55];
bool cmp (double x, double y) {
	return x > y;
}
void solve() {
	int n = in();
	int k =in();
	double ans = fin();
	for (int i = 0; i < n;i++) {
		a[i] = fin();
		ans += a[i];
	}
	sort(a, a + n, cmp);
	int cnt = n;
	int i = 0;
	double temp = ans;
	while ( i < n) {
		temp = temp / (n - i);
		if (temp >= a[i]) {
			break;
		}
		temp = temp * (n - i) - a[i];
		i++;
	}
	double res = 1;
	for (int j = 0; j < i; j++) {
		res *= a[j];
	}
	printf("%.8f\n", res * pow(temp, n - i));
}

int main() {
  freopen("C-small-1-attempt1.in","r", stdin);
  freopen("2","w", stdout);
  //printf("%.100f\n", pow(0.3333, 50));
  int T = in();
  for (int CN = 1; CN <= T; ++CN) {
    printf("Case #%d: ", CN);
    solve();
  }

  return 0;
}
