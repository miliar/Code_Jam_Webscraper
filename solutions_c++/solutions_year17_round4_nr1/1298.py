#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <iomanip>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <list>
#include <cmath>

using namespace std;

const int P = 4;

typedef long long ll;
typedef pair<int, int> ii;

vector<vector<int>> c2 = { {1, 0}, {0, 2} };
vector<vector<int>> c3 = { {1, 0, 0}, {0, 1, 1}, {0, 3, 0}, { 0, 0, 3 }, {0, 2, 2}, {0, 4, 1} };
vector<vector<int>> c4 = { 
	{1, 0, 0, 0}, 
	{0, 1, 0, 1}, {0, 0, 2, 0},  
	{0, 2, 1, 0}, {0, 0, 1, 2}, 
	{ 0, 0, 0, 4 },{ 0, 0, 4, 0 },{ 0, 1, 2, 1 },{ 0, 2, 0, 2 },{ 0, 4, 0, 0 },
	{ 0, 0, 3, 2 },{ 0, 1, 1, 3 },{ 0, 2, 3, 0 },{ 0, 3, 1, 1 },
	{ 0, 0, 2, 4 },{ 0, 1, 4, 1 },{ 0, 2, 2, 2 },{ 0, 3, 0, 3 },{ 0, 4, 2, 0 },
	{ 0, 1, 3, 3 },{ 0, 2, 1, 4 },{ 0, 3, 3, 1 },{ 0, 4, 1, 2 },
	{ 0, 0, 4, 4 },{ 0, 2, 4, 2 },{ 0, 3, 2, 3 },{ 0, 4, 0, 4 },{ 0, 4, 4, 0 },
	{ 0, 2, 3, 4 },{ 0, 4, 3, 2 },
	{ 0, 3, 4, 3 },{ 0, 4, 2, 4 } };

int main() {
#ifdef _DEBUG
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	
	/*for (int f = 0; f < 20; f++) {
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				for (int k = 0; k < 5; k++) {
					if ((i + 2 * j + 3 * k) % 4 == 0 && (i + j + k == f)) {
						cout << "{0, " << i << ", " << j << ", " << k << "}, ";
					}
				}
			}
		}
		cout << endl;
	}*/

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		int n, p;
		cin >> n >> p;
		int r[P];
		fill(r, r + P, 0);
		for (int i = 0; i < n; i++) {
			int g;
			cin >> g;
			r[g % p]++;
		}


		vector<vector<int>> z;

		if (p == 2) {
			z = c2;
		}
		else if (p == 3) {
			z = c3;
		}
		else {
			z = c4;
		}

		int c = 0;
		for (int i = 0; i < z.size(); i++) {
			int mn = 100000000;
			for (int j = 0; j < p; j++) {
				if (z[i][j] > 0) {
					mn = min(mn, r[j] / z[i][j]);
				}
			}

			c += mn;
			for (int j = 0; j < p; j++) {
				r[j] -= mn  * z[i][j];
			}
		}

		for (int i = 0; i < p; i++) {
			if (r[i] > 0) {
				c++;
				break;
			}
		}

		cout << c << endl;
	}

	return 0;
}