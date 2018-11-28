#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;

typedef long long ll;

int t;

int main() {
	cin >> t;
	int r, c;
	char cake[30][30], first[30], last[30];
	for (int ti = 1; ti <= t; ti++) {
		cout << "Case #" << ti << ":";
		cout << endl;
		cin >> r >> c;
		memset(first, '?', sizeof(first));
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cin >> cake[i][j];
				if (first[i] == '?')
					first[i] = cake[i][j];
			}
		}
		for (int i = 0; i < r; i++) {
			char cc = first[i];
			for (int j = 0; j < c; j++) {
				if (cake[i][j] == '?')
					cake[i][j] = cc;
				else
					cc = cake[i][j];
				if (cake[i][j] != '?')
					last[j] = cake[i][j];
			}
		}
		for (int j = c-1; j >= 0; j--) {
			char cc = last[j];
			for (int i = r-1; i >= 0; i--) {
				if (cake[i][j] == '?')
					cake[i][j] = cc;
				else
					cc = cake[i][j];
			}
		}
		for (int i=0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cout << cake[i][j];
			}
			cout << endl;
		}
	}
}
