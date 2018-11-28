#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <bitset>
#include <memory.h>

using namespace std;

char field[33][33];
char initial[33][33];

struct rect {
	int t, b, l, r;
};

bool isfree(int i, int j, int l, int r) {
	for (int we = i; we <= j; we++) {
		for (int re = l; re <= r; re++) {
			if (field[we][re] != '?') {
				return false;
			}
		}
	}
	return true;
}

void SET(int i, int j, int l, int r, char ch) {
	for (int we = i; we <= j; we++) {
		for (int re = l; re <= r; re++) {
			field[we][re] = ch;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		set<char> st;
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> field[i][j];
				initial[i][j] = field[i][j];
				if (field[i][j] != '?') {
					st.insert(field[i][j]);
				}
			}
		}

		vector<rect> rects;

		for (auto ch : st) {
			int miL = INT_MAX;
			int maR = INT_MIN;
			int miT = INT_MAX;
			int maB = INT_MIN;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					if (field[i][j] == ch) {
						miL = min(miL, j);
						maR = max(maR, j);
						miT = min(miT, i);
						maB = max(maB, i);
					}
				}
			}
			rects.push_back({ miT, maB, miL, maR });
			for (int i = miT; i <= maB; i++) {
				for (int j = miL; j <= maR; j++) {
					field[i][j] = ch;
				}
			}
		}

		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (field[i][j] == '?') {
					cnt++;
				}
			}
		}

		while (cnt > 0) {
			int prevCnt = cnt;
			for (int k = 0; k < rects.size(); k++) {
				rect &r = rects[k];
				char ch = field[r.t][r.l];
				while (r.t != 0 && isfree(r.t - 1, r.t - 1, r.l, r.r)) {
					r.t--;
					cnt -= (r.r - r.l + 1);
					SET(r.t, r.b, r.l, r.r, ch);
				}
			}
			for (int k = 0; k < rects.size(); k++) {
				rect &r = rects[k];
				char ch = field[r.t][r.l];
				while (r.l != 0 && isfree(r.t, r.b, r.l - 1, r.l - 1)) {
					r.l--;
					cnt -= (r.b - r.t + 1);
					SET(r.t, r.b, r.l, r.r, ch);
				}
			}
			for (int k = 0; k < rects.size(); k++) {
				rect &r = rects[k];
				char ch = field[r.t][r.l];
				while (r.b != n - 1 && isfree(r.b + 1, r.b + 1, r.l, r.r)) {
					r.b++;
					cnt -= (r.r - r.l + 1);
					SET(r.t, r.b, r.l, r.r, ch);
				}
			}
			for (int k = 0; k < rects.size(); k++) {
				rect &r = rects[k];
				char ch = field[r.t][r.l];
				while (r.r != m - 1 && isfree(r.t, r.b, r.r + 1, r.r + 1)) {
					r.r++;
					cnt -= (r.b - r.t + 1);
					SET(r.t, r.b, r.l, r.r, ch);
				}
			}
			if (prevCnt == cnt) {
				cerr << "FUCK";
			}
		}


		cout << "Case #" << test << ": " << endl;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cout << field[i][j];
			}
			cout << endl;
		}
	}


	//system("pause");
	return 0;
}