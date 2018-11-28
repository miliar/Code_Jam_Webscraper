#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string s[100];
int r, c;

bool one(int strn) {
	for (int i = 0; i < c; ++i)
		if (s[strn][i] != '?') return 1;
	return 0;
}

void resolve(int strn) {
	//cout << "res" << strn << "\n";
	char fill = s[strn][0];
	for (int i = 1; i < c; ++i)
		if (s[strn][i] == '?') s[strn][i] = fill;
		else fill = s[strn][i];
	for (int i = c - 1; i >= 0; --i)
		if (s[strn][i] == '?') s[strn][i] = fill;
		else fill = s[strn][i];
}

void cp(int to, int from) {
	if (from < 0 || from >= r) return;
	s[to] = s[from];
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output", "w", stdout);

	int t, testnum = 1;
	cin >> t;
	while (t--) {
		cin >> r >> c;
		for (int i = 0; i < r; ++i)
			cin >> s[i];
		cout << "Case #" << testnum++ << ":\n";
		for (int i = 0; i < r; ++i)
			if (one(i)) resolve(i);
			else cp(i, i - 1);
		for (int i = r - 1; i >= 0; --i)
			if (!one(i)) cp(i, i + 1);
		for (int i = 0; i < r; ++i)
			cout << s[i] << "\n";
	}

	return 0;
}