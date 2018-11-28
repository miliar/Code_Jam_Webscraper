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

bool was[110][110][110][110];

int solution() {

	int t;
	scanf("%d", &t);
	for(int test = 1; t--; test++) {
		printf("Case #%d: ", test);
		int hd, ad, hk, ak, b, d;
		scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
		int ghd = hd;
		vector<pair<pair<pair<int, int>, pair<int, int> >, int> > vc;
		was[hd][ad][hk][ak] = 1;
		vc.pb(mp(mp(mp(hd, ad), mp(hk, ak)), 1));
		bool answered = 0;
		for(int i = 0; i < (int) vc.size(); i++) {
			int hd = vc[i].fs.fs.fs, ad = vc[i].fs.fs.sc, hk = vc[i].fs.sc.fs, ak = vc[i].fs.sc.sc, x = vc[i].sc;
			int nhd, nad, nhk, nak;
			{
				nhd = hd, nad = ad, nhk = hk, nak = ak;
				nhk -= nad;
				if(nhk <= 0) {
					printf("%d\n", x);
					answered = 1;
					break;
				}
				nhd -= nak;
				if(nhd > 0 && !was[nhd][nad][nhk][nak]) {
					vc.pb(mp(mp(mp(nhd, nad), mp(nhk, nak)), x + 1));
					was[nhd][nad][nhk][nak] = 1;
				}
			}
			{
				nhd = hd, nad = ad, nhk = hk, nak = ak;
				nad += b;
				nad = min(nad, 100);
				if(nhk <= 0) {
					printf("%d\n", x);
					answered = 1;
					break;
				}
				nhd -= nak;
				if(nhd > 0 && !was[nhd][nad][nhk][nak]) {
					vc.pb(mp(mp(mp(nhd, nad), mp(nhk, nak)), x + 1));
					was[nhd][nad][nhk][nak] = 1;
				}
			}
			{
				nhd = hd, nad = ad, nhk = hk, nak = ak;
				nhd = ghd;
				if(nhk <= 0) {
					printf("%d\n", x);
					answered = 1;
					break;
				}
				nhd -= nak;
				if(nhd > 0 && !was[nhd][nad][nhk][nak]) {
					vc.pb(mp(mp(mp(nhd, nad), mp(nhk, nak)), x + 1));
					was[nhd][nad][nhk][nak] = 1;
				}
			}
			{
				nhd = hd, nad = ad, nhk = hk, nak = ak;
				nak -= d;
				nak = max(nak, 0);
				if(nhk <= 0) {
					printf("%d\n", x);
					answered = 1;
					break;
				}
				nhd -= nak;
				if(nhd > 0 && !was[nhd][nad][nhk][nak]) {
					vc.pb(mp(mp(mp(nhd, nad), mp(nhk, nak)), x + 1));
					was[nhd][nad][nhk][nak] = 1;
				}
			}
		}
		if(!answered) {
			printf("IMPOSSIBLE\n");
		}
		memset(was, 0, sizeof(was));
	}

	return (0);
}

inline pair<pair<bool, bool>, pair<string, bool> > useinout() {
	return (mp(mp(1, 1), mp("", 0)));
}

//by Andrey Kim
