#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)
#define EPS 1E-9
#define INF 2000000000
#define ll long long
#define ld long double
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define MAXN 100001

int n, q;
int e[123], s[123], d[123][123], f[123][123], u[123], v[123];

int used[123];

ld dist[123];

void main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;
	forn(ttt, tc) {
		printf("Case #%d:", ttt + 1);
		cin >> n >> q;
		forn(i, n)
			cin >> e[i] >> s[i];
		forn(i, n)
			forn(j, n) {
				cin >> d[i][j];
				f[i][j] = d[i][j];
		}

	
			forn(i, n) {
				forn(j, n) {
						forn(k, n) {
					if (f[i][k] >= 0 && f[k][j] >= 0 && (f[i][j] > f[i][k] + f[k][j] || f[i][j] < 0))
						f[i][j] = f[i][k] + f[k][j];
				}
			}
		}
		forn(i, n) {
			forn(j, n) {
				//cerr << f[i][j] << " ";
			}
			//cerr << endl;
		}
		forn(ii, q) {
			//cerr << "test #" << (ttt + 1) << ": " << ii << endl;
			cin >> u[ii] >> v[ii];
			--u[ii], --v[ii];
			memset(used, 0, sizeof used);
			forn(i, n)
				dist[i] = 1e40;
			dist[u[ii]] = 0;
			while (!used[v[ii]]) {
				int vv = -1;
				forn(i, n) {
					if (!used[i] && (vv < 0 || (dist[i] < dist[vv])))
						vv = i;
				}
				if (vv == -1)
					break;
				//cerr << vv << endl;
				used[vv] = 1;
				forn(i, n) {
					if (f[vv][i] >= 0 && e[vv] >= f[vv][i]) {
						ld get = dist[vv] + f[vv][i] * 1. / s[vv];
						if (get < dist[i])
							dist[i] = get;
					}
				}
			}
			printf(" %.9llf", dist[v[ii]]);
		}
		puts("");
	}
}