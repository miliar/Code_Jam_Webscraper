#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <unordered_map>
#include <string>
#include <iomanip>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <unordered_set>
#include <stack> 
#include <algorithm>
#include <math.h>
#include <sstream>
#include <functional>
#include <bitset>
using namespace std;
#define mems(A, val) memset(A, val, sizeof(A))
#define mp(a, b) make_pair(a, b)
#define all(B) (B).begin(), (B).end()
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define forit (it, coll) for(auto it = coll.begin(); it != coll.end(); ++it)
#define sz(a) (int)a.size()
#define pb push_back
const int MAXN = 2 * 1000 * 100 + 10;
const double EPS = 1e-9;
typedef long long LL;
const LL MOD = 1000 * 1000 * 1000 + 7;

int main(int argc, char* argv[]) {

#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("data.in", "r", stdin); freopen("data.out", "w", stdout);
#endif
	ios::sync_with_stdio(0);
	cin.tie();

	int ttt;
	cin >> ttt;
	forn(tt, 0, ttt) {
		int n, q;
		cin >> n >> q;

		vector<LL> s(n), e(n);
		forn(i, 0, n)cin >> e[i] >> s[i];
		int tmp;
		vector<vector<LL> > D(n, vector<LL>(n));

		forn(i, 0, n*n) {
			cin >> D[i / n][i%n];
			if (D[i / n][i%n] == -1) {
				D[i / n][i%n] = (LL)1000000000000000;
			}
		}


		for (int k = 0; k<n; ++k)
			for (int i = 0; i<n; ++i)
				for (int j = 0; j<n; ++j)
					D[i][j] = min(D[i][j], D[i][k] + D[k][j]);

		vector<LL> distances(n);
		for (int i = 0; i < n - 1; ++i) {
			distances[i + 1] = distances[i] + D[i][i + 1];
		}

		int cur = n - 1;

		vector<int> h;

		vector<vector<double> > g(n,vector<double>(n));
	
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (i == j) {
					g[i][j] = 0.0;
					continue;
				}
				if (D[i][j] <= e[i]) {
					g[i][j] = (double)(D[i][j]) / s[i];
				}
				else {
					g[i][j] = 1e20;
				}
			}
		}

		for (int k = 0; k<n; ++k)
			for (int i = 0; i<n; ++i)
				for (int j = 0; j < n; ++j)
				{
					if (g[i][k] + g[k][j] < g[i][j] - EPS)
						g[i][j] = g[i][k] + g[k][j];
				}
					

		cout << "Case #" << tt + 1 << ": " << fixed << setprecision(10);
		for (int i = 0; i < q; ++i) {
			int f, t;
			cin >> f >> t;
			f--;
			t--;
			cout << g[f][t] << " ";
		}

		cout<<endl;;
	}


	return 0;
}