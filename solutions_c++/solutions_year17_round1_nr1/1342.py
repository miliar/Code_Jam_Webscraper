#include <bits/stdc++.h>

using namespace std;

void solve (int current_case) {
	cout << "Case #" << current_case << ":\n";
	int r, c;
	cin >> r >> c;

	vector<string> mt(r);
	for (auto &x : mt) cin >> x;

	vector<int> first(r, -1);
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j) {
			if (mt[i][j] != '?') {
				first[i] = j;
				break;
			}
		}

	for (int i = 0; i < r; ++i) {
		if (first[i] == -1) continue;
		char current = mt[i][first[i]];
		for (int j = 0; j < c; ++j) {
			if (mt[i][j] != '?') current = mt[i][j];
			mt[i][j] = current;
		}
	}

	first = vector<int>(c, -1);
	for (int j = 0; j < c; ++j)
		for (int i = 0; i < r; ++i) {
			if (mt[i][j] != '?') {
				first[j] = i;
				break;
			}
		}

	for (int j = 0; j < c; ++j) {
		if (first[j] == -1) continue;
		char current = mt[first[j]][j];
		for (int i = 0; i < r; ++i) {
			if (mt[i][j] != '?') current = mt[i][j];
			mt[i][j] = current;
		}
	}

	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j)
			cout << mt[i][j];
		cout << '\n';
	}
}

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    #ifdef FSOCIETY
		freopen("A-large.in", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
       
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    	solve(i);
}