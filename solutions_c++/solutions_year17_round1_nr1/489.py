#include <iostream>

using namespace std;

int r,c,T;
string g[30];

void fix_row(string& s) {
	int first = -1;
	for(int i = 0; i < c; ++i) {
		if(s[i] != '?') {
			first = i;
			break;
		}
	}
	if(first == -1) return;
	for(int i = 0; i < first; ++i)
		s[i] = s[first];
	for(int i = first+1; i < c; ++i) {
		if(s[i] == '?') s[i] = s[first];
		else first = i;
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		cin >> r >> c;
		for(int i = 0; i < r; ++i) {
			cin >> g[i];
			fix_row(g[i]);
		}
		int fn = -1;
		for(int i = 0; i < r; ++i) {
			if(g[i][0] != '?') {
				fn = i;
				break;
			}
		}
		for(int i = 0; i < fn; ++i)
			g[i] = g[fn];
		for(int i = fn+1; i < r; ++i) {
			if(g[i][0] == '?')
				g[i] = g[fn];
			else fn = i;
		}
		cout << "Case #" << t << ":\n";
		for(int i = 0; i < r; ++i)
			cout << g[i] << "\n";
	}

	return 0;
}