#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;
typedef vector<char> VI;
typedef vector<VI> VVI;
void TestAlphabetCake() {
	int t;
	freopen("Input.txt", "r", stdin);
	freopen("Output.txt", "w", stdout);
	cin >> t;
	for (int qq = 1; qq <= t; ++qq) {
		int r, c;
		cin >> r >> c;
		VVI v(r, VI(c, '0'));
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j) {
				char tc;
				cin >> tc;
				if (tc != '?') { 
					v[i][j] = tc; 
				}
			}
		for (int i = 0; i < r; ++i){
			for (int j = 0; j < c; ++j) {
				if (v[i][j] == '0') {
					int ir;
					for (ir = i; ir < r; ++ir) {
						if (v[ir][j] != '0') {
							break;
						}
					}
					if (ir >= r) { ir = r - 1; }
					for (; ir >= 0; --ir) {
						if (v[ir][j] != '0') {
							break;
						}
					}
					if(ir >= 0 && ir < r) v[i][j] = v[ir][j];
				}
			}
		}
		for (int i = 0; i < c; ++i) {
			if (v[0][i] == '0') {
				int ic = 0;
				for (ic = i; ic < c; ++ic) {
					if (v[0][ic] != '0') {
						break;
					}
				}
				if (ic >= c) { ic = c - 1; }
				for (; ic >= 0; --ic) {
					if (v[0][ic] != '0') {
						break;
					}
				}
				for (int j = 0; j < r; ++j) {
					v[j][i] = v[j][ic];
				}
			}
		}
		cout << "Case #" << qq << ":\n";
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				cout << v[i][j];
			}
			cout << "\n";
		}
	}
	fflush(stdout);
}