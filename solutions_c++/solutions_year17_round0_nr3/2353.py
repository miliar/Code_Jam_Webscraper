#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cassert>
#include <map>
#include <string>
#include <iomanip>
#include <set>
#include <ctime>
#include <unordered_set>
#include <stack>
#include <complex>
using namespace std;

#define FOR(i, n) for (int i = 0; i < (int)(n); ++i)
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford1(i, n) for (int i = (int)(n); i >= 1; --i)
#define ford(i, n) for (int i = (int)(n)-1; i >= 0; --i)
#define pb push_back
#define sz(v) (int)(v).size()
#define mp make_pair
#define all(v) (v).begin(), (v).end()
typedef vector<int> vi;
typedef long double LD;//
typedef long long LL;
typedef pair<int, int> pii;
typedef vector<pii> vpi;


pair<LL, LL> get(LL n, LL k){
	if (k == 1)
		return mp((n - 1) / 2, n - 1 - (n - 1) / 2);
	if (n % 2 == 1){
		--k;
		return get(n / 2, (k + 1) / 2);
	}
	--k;
	if (k % 2 == 1){
		return get(n / 2, (k + 1) / 2 );
	}
	else{
		return get( (n-1) / 2, (k + 1) / 2);
	}
}
void solve() {
	int T = 0;
	scanf("%d", &T);
	for1(iter, T){
		LL n, k;
		scanf("%lld%lld", &n, &k);
		pair<LL, LL> u = get(n, k);
		printf("Case #%d: %lld %lld\n", iter, u.second, u.first);
	}
}

void testgen() {
	FILE *f = fopen("input.txt", "w");
//	srand(time(0));
	fclose(f);
}

int main() {
#ifdef ysu
	//    testgen();
//	assert(freopen("input.txt", "r", stdin));
	assert(freopen("C-large.in", "r", stdin));
	assert(freopen("C-large.out", "w", stdout));
	//freopen("output.txt", "w", stdout);
#else
#define task "kids"
	//freopen(task".in", "r", stdin);
	//freopen(task".out", "w", stdout);
#endif
	cout << fixed;
	cout.precision(23);
	solve();

#ifdef ysu
	cerr << "\ntime = " << fixed << setprecision(3) << clock() / (double)CLOCKS_PER_SEC << "s\n";
#endif
	return 0;
}