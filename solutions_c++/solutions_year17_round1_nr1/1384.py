#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>

using namespace std;

int main(int argc, char *argv) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int R, C;
		cin >> R >> C;
		vector<char> deco(R * C);
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				cin >> deco[C * r + c];
			}
		}

		for (int r = 0; r < R; r++) {
			int is_decorated = 0;
			for (int c = 0; c < C; c++) {
				if (deco[C * r + c] != '?') {
					is_decorated = 1;
				}
			}
			if (is_decorated) {
				for (int c = 1; c < C; c++) {
					if (deco[C * r + c] == '?') {
						deco[C * r + c] = deco[C * r + c - 1];
					}
				}
				for (int c = C - 2; c >= 0; c--) {
					if (deco[C * r + c] == '?') {
						deco[C * r + c] = deco[C * r + c + 1];
					}
				}
			}
		}

		for (int r = 1; r < R; r++) {
			int is_decorated = 0;
			for (int c = 0; c < C; c++) {
				if (deco[C * r + c] != '?') {
					is_decorated = 1;
				}
			}
			if (!is_decorated) {
				for (int c = 0; c < C; c++) {
					deco[C * r + c] = deco[C * (r - 1) + c];
				}
			}
		}
		for (int r = R - 2; r >= 0; r--) {
			int is_decorated = 0;
			for (int c = 0; c < C; c++) {
				if (deco[C * r + c] != '?') {
					is_decorated = 1;
				}
			}
			if (!is_decorated) {
				for (int c = 0; c < C; c++) {
					deco[C * r + c] = deco[C * (r + 1) + c];
				}
			}
		}

		cout << "Case #" << t + 1 << ":" << endl;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				cout << deco[C * r + c];
			}
			cout << endl;
		}
	}
}