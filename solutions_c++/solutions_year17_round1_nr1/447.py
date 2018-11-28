#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <climits>

#include <sstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <utility>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

#define fast_cin() ios_base::sync_with_stdio(false)

typedef long double ld;
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int max_R = 30;
char grid[max_R][max_R];;
char curr[max_R];

int main()
{
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		int R, C;
		cin >> R >> C;
		for (int i = 0; i < R; ++i) {
			cin >> grid[i];
		}

		memset(curr, '?', sizeof(curr));

		for (int j = 0; j < C; ++j) {
			for (int i = 0; i < R; ++i) {
				if (grid[i][j] != '?') {
					curr[j] = grid[i][j];
					break;
				}
			}
		}

//		char prev = '?';
//		for (int j = 0; j < C; ++j) {
//			if (curr[j] == '?') {
//				curr[j] = prev;
//			} else {
//				prev = curr[j];
//			}
//		}
//		assert(prev != '?');
//		for (int j = C - 1; j >= 0; --j) {
//			if (curr[j] == '?') {
//				curr[j] = prev;
//			} else {
//				prev = curr[j];
//			}
//		}

		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				if (grid[i][j] != '?') {
					curr[j] = grid[i][j];
				} else {
					grid[i][j] = curr[j];
				}
			}
		}

		int prev = 0;
		for (int j = 0; j < C; ++j) {
			if (curr[j] == '?') {
				for (int i = 0; i < R; ++i) {
					grid[i][j] = grid[i][prev];
				}
			} else {
				prev = j;
			}
		}
		prev = C - 1;
		for (int j = C - 1; j >= 0; --j) {
			if (curr[j] == '?') {
				for (int i = 0; i < R; ++i) {
					grid[i][j] = grid[i][prev];
				}
			} else {
				prev = j;
			}
		}

		printf("Case #%d:\n", tc);
		for (int i = 0; i < R; ++i) {
			cout << grid[i] << endl;
		}
	}
}
