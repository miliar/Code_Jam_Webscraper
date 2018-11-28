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

const int N = 1000 + 5;
char s[N];
int k;
int a[N];
void solve() {
	int T;
	scanf("%d", &T);
	for1(iter, T){
		printf("Case #%d: ", iter);

		scanf("%s%d", s, &k);
		int n = strlen(s);
		forn(i, n){
			if (s[i] == '+')
				a[i] = 1;
			else
				a[i] = 0;
		}
		int res = 0;
		forn(i, n){
			if (!a[i]){
				if (i + k <= n){
					for (int j = i; j < i + k; ++j)
						a[j] = 1 - a[j];
					++res;
				}
			}
		}
		bool ok = true;
		forn(i, n){
			if (!a[i])
				ok = false;
		}
		if (!ok){
			puts("IMPOSSIBLE");
		}
		else{
			printf("%d\n", res);
		}
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
	assert(freopen("A-large.in", "r", stdin));
	assert(freopen("A-large.out", "w", stdout));
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