#include <stdio.h>
#include <bits/stdc++.h>
#include <x86intrin.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
// tree<key, mapped = null_type, cmp = less<key>, rb_tree_tag, tree_order_statistics_node_update> name; order_of_key find_by_order

using namespace std;

#define pb push_back
#define ppb pop_back
#define mp make_pair
#define fs first
#define sc second
#define abs(a) ((a) < 0 ? -(a) : (a))
#define sqr(a) ((a) * (a))

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

inline pair<pair<bool, bool>, pair<string, bool> > useinout();

#ifdef SOL
double starttime;
#endif

void initialization() {
#ifdef SOL
	starttime = 1000. * clock() / CLOCKS_PER_SEC;
	if (useinout().fs.fs)
		freopen("input.txt", "r", stdin);
	if (useinout().fs.sc)
		freopen("output.txt", "w", stdout);
#else
	srand(__rdtsc());
	const string file = useinout().sc.fs;
	if (!file.empty()) {
		freopen((file + ".in").c_str(), "r", stdin);
		freopen((file + ".out").c_str(), "w", stdout);
	} else
	if(useinout().sc.sc) {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
#endif
}

int solution();

void finish(int exitval) {
	fflush(stdout);
#ifdef SOL
	fprintf(stderr, "\n-----------------\nexit value: %d\ntime: %.3lf ms\n-----------------\n", exitval, 1000. * clock() / CLOCKS_PER_SEC - starttime);
#endif
}

int main() {
	initialization();
	finish(solution());
	return (0);
}

const double eps = 1e-9;
const int mod = (int) 1e+9 + 7;
const double pi = acos(-1.);
const int maxn = 100100;

int a[maxn], c[maxn];

int solution() {

	int t;
	scanf("%d", &t);
	for(int test = 1; t--; test++) {
		printf("Case #%d: ", test);

		c[0] = c[1] = c[2] = c[3] = 0;

		int n, p;
		scanf("%d%d", &n, &p);
		for(int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			c[a[i] % p]++;
		}

		int ans = 0, ost = 0;
		if(p == 2) {
			ans += c[0];
			while(c[1]) {
				ans += ost == 0;
				c[1]--;
				ost += 1;
				ost %= p;
			}
		}
		if(p == 3) {
			ans += c[0];
			while(c[1] && c[2]) {
				ans += ost == 0;
				c[1]--;
				c[2]--;
				ost += 0;
				ost %= p;
			}
			while(c[1]) {
				ans += ost == 0;
				c[1]--;
				ost += 1;
				ost %= p;
			}
			while(c[2]) {
				ans += ost == 0;
				c[2]--;
				ost += 2;
				ost %= p;
			}
		}
		if(p == 4) {
			ans += c[0];
			while(c[1] && c[3]) {
				ans += ost == 0;
				c[1]--;
				c[3]--;
				ost += 0;
				ost %= p;
			}
			while(c[2]) {
				ans += ost == 0;
				c[2]--;
				ost += 2;
				ost %= p;
			}
			while(c[1]) {
				ans += ost == 0;
				c[1]--;
				ost += 1;
				ost %= p;
			}
			while(c[3]) {
				ans += ost == 0;
				c[3]--;
				ost += 3;
				ost %= p;
			}
		}
		printf("%d\n", ans);
	}

	return (0);
}

inline pair<pair<bool, bool>, pair<string, bool> > useinout() {
	return (mp(mp(1, 1), mp("", 0)));
}

//by Andrey Kim
