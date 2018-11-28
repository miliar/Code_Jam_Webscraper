#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cassert>
#include <iostream>

using namespace std;

const double eps = 1e-9;
const int inf = 1e9 + 23;

const int size = 1000 + 23;

const int N = 4;

char color[6];

int stall[size];
vector <pair <int, int> > col;

int first_max;

int find_max () {
	int num_max = first_max;
	for (int i = 0; i < 3; i++) {
		if (col[i].first > col[num_max].first) {
			num_max = i;
		}
	}
	return num_max;
}

// bool good (int a, int b) {
// 	if (a == b)
// 		return false;
// 	if (a > 2) {

// 	}
// }

// void check(int n) {
// 	for (int i = 0; i < n ; i++) {

// 	}
// }

int main (void){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	col.push_back(make_pair(0, 0));
	col.push_back(make_pair(0, 0));
	col.push_back(make_pair(0, 0));
	color[0] = 'R';
	color[3] = 'G';
	color[1] = 'Y';
	color[4] = 'V';
	color[2] = 'B';
	color[5] = 'O';

	int t;
	cin >> t;
	for (int it = 1; it <= t; it++) {
		cout << "Case #" << it << ": ";
		cin >> n;
		int r, o, y, g, b, v;
		cin >> r >> o >> y >> g >> b >> v;
		col[0].first = r;
		col[0].second = g;
		col[1].first = y;
		col[1].second = v;
		col[2].first = b;
		col[2].second = o;
		if (col[0].first > col[1].first) {
			if (col[0].first > col[2].first) {
				first_max = 0;
			} else {
				first_max = 2;
			}
		} else {
			if (col[1].first > col[2].first) {
				first_max = 1;
			} else {
				first_max = 2;
			}
		}
		int k = 0;
		bool ans = true;
		while (k < n) {
			int m = find_max();
			if (k != 0) {
				if (stall[k - 1] == m) {
					if (m == 0) {
						if (col[1].first > col[2].first)
							m = 1;
						else
							m = 2;
					} else {
						if (m == 1) {
							if (col[0].first > col[2].first)
								m = 0;
							else
								m = 2;
						} else {
							if (col[0].first > col[1].first)
								m = 0;
							else
								m = 1;
						}
					}
				}
			}
			stall[k] = m;
			k++;
			col[m].first--;
			if (col[m].first < 0) {
				ans = false;
				cerr << 1 << endl;
				break;
			}
			if (col[m].second > 0) {
				for (int i = 0; i < col[m].second; i++) {
					stall[k] = m + 3;
					k++;
					stall[k] = m;
					k++;
				}
				col[m].first -= col[m].second;
				col[m].second = 0;
				if (col[m].first < 0) {
					if (k == n+1) {
						if (m == first_max) {
							break;
						}
					}
					ans = false;
					cerr << 2 << endl;
					break;
				}
			}
		}
		// for (int i = 0; i < n; i++) {
		// 	cerr << color[stall[i]];
		// }
		// cerr << endl;
		if (k == n) {
			if (stall[n - 1] == stall[0])
				ans = false;
		}
		if (ans) {
			// check(n);
			for (int i = 0; i < n; i++) {
				cout << color[stall[i]];
			}
			cout << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}