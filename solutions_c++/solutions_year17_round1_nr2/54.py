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

int a[55][55], b[55], it[55];

int solution() {

	int t;
	scanf("%d", &t);
	for(int test = 1; t--; test++) {
		printf("Case #%d: ", test);
		int n, m;
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; i++) {
				scanf("%d", &b[i]);
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				scanf("%d", &a[i][j]);
			}
			sort(&a[i][0], &a[i][m]);
			it[i] = 0;
		}
		int cnt = 0;
		for(int x = 1; x <= 1000100; x++) {
			bool ok = 1;
			for(int i = 0; i < n; i++) {
				int lw = (b[i] * x * 9 + 9) / 10, gt = (b[i] * x * 11) / 10;
				while(it[i] < m && a[i][it[i]] < lw) {
					it[i]++;
				}
				if(it[i] == m) {
					ok = 0;
				}
				if(a[i][it[i]] > gt) {
					ok = 0;
				}
			}
			if(ok) {
				cnt++;
				for(int i = 0; i < n; i++) {
					it[i]++;
				}
				x--;
			}
		}
		printf("%d\n", cnt);
	}

	return (0);
}

inline pair<pair<bool, bool>, pair<string, bool> > useinout() {
	return (mp(mp(1, 1), mp("", 0)));
}

//by Andrey Kim
