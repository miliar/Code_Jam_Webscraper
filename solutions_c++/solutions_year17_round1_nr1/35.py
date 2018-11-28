#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int r, c, t;
char x[30][30];

void doit(int abcd) {
	cout << "Case #" << abcd+1 << ":\n";
	cin >> r >> c;
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
			cin >> x[i][j];

	for (int i = 0; i < r; ++i) {
		bool y = 1;
		for (int j = 0; j < c; ++j)
			if (x[i][j] != '?')
				y = 0;
		if (y)
			continue;
		for (int j = 0; j < c; ++j) {
			if (j == 0)
				continue;
			if (x[i][j] == '?' && x[i][j-1] != '?')
				x[i][j] = x[i][j-1];
		}
		for (int j = c-1; j >= 0; --j) {
			if (j == c-1)
				continue;
			if (x[i][j] == '?' && x[i][j+1] != '?')
				x[i][j] = x[i][j+1];
		}
	}

	for (int i = 0; i < r; ++i) {
		if (i == 0)
			continue;
		if (x[i][0] == '?' && x[i-1][0] != '?')
			for (int j = 0; j < c; ++j)
				x[i][j] = x[i-1][j];
	}

	for (int i = r-1; i >= 0; --i) {
		if (i == r-1)
			continue;
		if (x[i][0] == '?' && x[i+1][0] != '?')
			for (int j = 0; j < c; ++j)
				x[i][j] = x[i+1][j];
	}

	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j)
			cout << x[i][j];
		cout << endl;
	}
}

int main() {
	cin >> t;
	for (int i = 0; i < t; ++i)
		doit(i);
}