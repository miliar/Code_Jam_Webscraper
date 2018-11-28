#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>
#include <queue>

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long int64;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const long long inf64 = ((long long)1 << 62) - 1;
const long double pi = acos(-1);

template <class T> T sqr (T x) {return x * x;}
template <class T> T abs (T x) {return x < 0 ? -x : x;}

int main () {
    ios_base::sync_with_stdio(0);
  	freopen("input.txt", "rt", stdin);
  	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;
	for (int ti = 0; ti < tc; ++ti) {
		int n, m;
		cin >> n >> m;
		
		vector<int> w(n);
		for (int i = 0; i < n; ++i) {
			cin >> w[i];
		}

		vector<vector<int>> a(n, vector<int>(m));
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				cin >> a[i][j];
			}
			sort(a[i].begin(), a[i].end());
		}

		vector<int> ind(n, 0);
		int res = 0; 
		while (true) {
			bool key = true;
			for (int i = 0; i < n; ++i) {
				if (ind[i] >= m) {
					key = false;
					break;
				}
			}

			if (!key) {
				break;
			}

			int ind_min = 0;
			int ind_max = 0;
			for (int i = 1; i < n; ++i) {
				if (a[i][ind[i]] * (long long) w[ind_min] < a[ind_min][ind[ind_min]] * (long long) w[i]) {
					ind_min = i;
				}
				if (a[i][ind[i]] * (long long) w[ind_max] > a[ind_max][ind[ind_max]] * (long long) w[i]) {
					ind_max = i;
				}
			}

			int l_min = (10 * a[ind_min][ind[ind_min]] + 11 * w[ind_min] - 1) / (11 * w[ind_min]);
			int r_min = (10 * a[ind_min][ind[ind_min]]) / (9 * w[ind_min]);
			int l_max = (10 * a[ind_max][ind[ind_max]] + 11 * w[ind_max] - 1) / (11 * w[ind_max]);
			int r_max = (10 * a[ind_max][ind[ind_max]]) / (9 * w[ind_max]);

			int l = max(l_min, l_max);
			int r = min(r_min, r_max);
			if (l <= r) {
				++res;
				for (int i = 0; i < n; ++i) {
					++ind[i];
				}
			} else {
				++ind[ind_min];
			}
		}

		cout << "Case #" << ti + 1 << ": " << res << endl;
	}
	
	return 0;
}
