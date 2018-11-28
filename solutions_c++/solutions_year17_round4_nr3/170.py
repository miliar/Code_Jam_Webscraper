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

char c[55][55];
int pm[55][55];
bool fix[55][55];

int solution() {

	int t;
	scanf("%d", &t);
	for(int test = 1; t--; test++) {

		printf("Case #%d: ", test);

		vector<pair<int, int> > pos;
		int n, m;
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; i++) {
			scanf("\n");
			for(int j = 0; j < m; j++) {
				scanf("%c", &c[i][j]);
			}
		}
		bool bad = 0;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(c[i][j] == '-' || c[i][j] == '|') {
					bool ok1 = 1, ok2 = 1;
					{
						for(int k = 1; k < 55; k++) {
							if(j + k >= m || c[i][j + k] == '#')
								break;
							if(c[i][j + k] != '.')
								ok1 = 0;
						}
						for(int k = 1; k < 55; k++) {
							if(j - k < 0 || c[i][j - k] == '#')
								break;
							if(c[i][j - k] != '.')
								ok1 = 0;
						}
					}
					{
						for(int k = 1; k < 55; k++) {
							if(i + k >= n || c[i + k][j] == '#')
								break;
							if(c[i + k][j] != '.')
								ok2 = 0;
						}
						for(int k = 1; k < 55; k++) {
							if(i - k < 0 || c[i - k][j] == '#')
								break;
							if(c[i - k][j] != '.')
								ok2 = 0;
						}
					}
					if(ok1 && ok2) {
						pos.pb(mp(i, j));
						c[i][j] = '-';
						{
							for(int k = 1; k < 55; k++) {
								if(j + k >= m || c[i][j + k] == '#')
									break;
								if(!pm[i][j + k])
									pm[i][j + k] = 1;
							}
							for(int k = 1; k < 55; k++) {
								if(j - k < 0 || c[i][j - k] == '#')
									break;
								if(!pm[i][j - k])
									pm[i][j - k] = 1;
							}
						}
					} else
					if(ok1) {
						fix[i][j] = 1;
						c[i][j] = '-';
						{
							for(int k = 1; k < 55; k++) {
								if(j + k >= m || c[i][j + k] == '#')
									break;
								if(!pm[i][j + k])
									pm[i][j + k] = 1;
							}
							for(int k = 1; k < 55; k++) {
								if(j - k < 0 || c[i][j - k] == '#')
									break;
								if(!pm[i][j - k])
									pm[i][j - k] = 1;
							}
						}
					} else
					if(ok2) {
						fix[i][j] = 1;
						c[i][j] = '|';
						{
							for(int k = 1; k < 55; k++) {
								if(i + k >= n || c[i + k][j] == '#')
									break;
								if(!pm[i + k][j])
									pm[i + k][j] = 1;
							}
							for(int k = 1; k < 55; k++) {
								if(i - k < 0 || c[i - k][j] == '#')
									break;
								if(!pm[i - k][j])
									pm[i - k][j] = 1;
							}
						}
					} else
					if(!ok1 && !ok2) {
						bad = 1;
					}
				}
			}
		}




		for(int iter = 0; iter <= 100; iter++) {

			for(int i = 0; i < n; i++) {
				for(int j = 0; j < m; j++) {
					pm[i][j] = 0;
				}
			}
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < m; j++) {
					if(c[i][j] == '-') {
						{
							for(int k = 1; k < 55; k++) {
								if(j + k >= m || c[i][j + k] == '#')
									break;
								if(!pm[i][j + k])
									pm[i][j + k] = 1;
							}
							for(int k = 1; k < 55; k++) {
								if(j - k < 0 || c[i][j - k] == '#')
									break;
								if(!pm[i][j - k])
									pm[i][j - k] = 1;
							}
						}
					}
					if(c[i][j] == '|') {
						{
							for(int k = 1; k < 55; k++) {
								if(i + k >= n || c[i + k][j] == '#')
									break;
								if(!pm[i + k][j])
									pm[i + k][j] = 1;
							}
							for(int k = 1; k < 55; k++) {
								if(i - k < 0 || c[i - k][j] == '#')
									break;
								if(!pm[i - k][j])
									pm[i - k][j] = 1;
							}
						}
					}
				}
			}



			for(int i = 0; i < n; i++) {
				for(int j = 0; j < m; j++) {
					if(!pm[i][j] && c[i][j] == '.') {
						bool ok = 0;
						{
							for(int k = 1; k < 55; k++) {
								if(i + k >= n || c[i + k][j] == '#')
									break;
								pm[i + k][j] = 1;
								if(c[i + k][j] == '-') {
									fix[i - k][j] = 1;
									c[i + k][j] = '|';
									ok = 1;
								}
							}
							for(int k = 1; k < 55; k++) {
								if(i - k < 0 || c[i - k][j] == '#')
									break;
								pm[i - k][j] = 1;
								if(c[i - k][j] == '-') {
									fix[i - k][j] = 1;
									c[i - k][j] = '|';
									ok = 1;
								}
							}
						}
						if(!ok) {
							// cout << i << " " << j << endl;
							bad = 1;
						}
					}
				}
			}
		}
		if(bad) {
			printf("IMPOSSIBLE\n");
			continue;
		}

		printf("POSSIBLE\n");
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				printf("%c", c[i][j]);
			}
			printf("\n");
		}

		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				pm[i][j] = 0;
				fix[i][j] = 0;
			}
		}

	}

	return (0);
}

inline pair<pair<bool, bool>, pair<string, bool> > useinout() {
	return (mp(mp(1, 1), mp("", 0)));
}

//by Andrey Kim
