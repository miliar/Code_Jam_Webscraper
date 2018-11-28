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

void DoIt(vector<vector<int>>& a, int lx, int rx, int ly, int ry) {
	int num = 0;
	int min_x = rx;
	int max_x = lx;
	int min_y = ry;
	int max_y = ly;
	for (int i = lx; i < rx; ++i) {
		for (int j = ly; j < ry; ++j) {
			if (a[i][j] != -1) {
				min_x = min(min_x, i);
				max_x = max(max_x, i);
				min_y = min(min_y, j);
				max_y = max(max_y, j);
				++num;
			}
		}
	}

	if (num == 1) {
		for (int i = lx; i < rx; ++i) {
			for (int j = ly; j < ry; ++j) {
				a[i][j] = a[min_x][min_y];
			}
		}
		return;
	}

	if (min_x < max_x) {
		DoIt(a, lx, max_x, ly, ry);
		DoIt(a, max_x, rx, ly, ry);
	} else {
		DoIt(a, lx, rx, ly, max_y);
		DoIt(a, lx, rx, max_y, ry);
	}
}

int main () {
    ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;
	for (int ti = 0; ti < tc; ++ti) {
	    int n, m;
	    cin >> n >> m;
	    
	    vector<vector<int>> a(n, vector<int>(m));
	    for (int i = 0; i < n; ++i) {
	    	for (int j = 0; j < m; ++j) {
	    	     char c;
	    	     cin >> c;
	    	     a[i][j] = (c == '?' ? -1 : c - 'A');
	    	}
	    }


	    DoIt(a, 0, n, 0, m);
		

		cout << "Case #" << ti + 1 << ":" << "\n";
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				cout << (char)(a[i][j] + 'A');
			}
			cout << "\n";
		}
	}
	
	return 0;
}
