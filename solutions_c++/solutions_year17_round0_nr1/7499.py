#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include <cstdio>

using namespace std;
#pragma warning (disable : 4996)

void solve() {
	int n, x, sol, sz, tmp; string s; bool valid;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		valid = true;
		//printf("i : %d\n", i);
		cin >> s >> x;
		sol = 0, sz = s.size() - x;
		for (int j = 0; j <= sz; j++) {
			//printf("j : %d\n", j);
			if (s[j] == '-') {
				tmp = 0;
				for (int k = j; tmp < x; k++, tmp++) {
					(s[k] == '-') ? s[k] = '+' : s[k] = '-';
				}
				if (tmp == x) sol++;
			}
			//cout << "minor modifi : " << s << endl;
		}
		sz = s.size();
		for (int j = 0; j < sz; j++) {
			if (s[j] == '-') {
				valid = false;
				break;
			}
		}
		//cout << "final string " << s << endl;
		//(valid) ? cout << "Case #" << i << ": " << sol << endl : cout << "Case #" << i << ": IMPOSSIBLE\n";
		(valid) ? printf("Case #%d: %d\n", i, sol) : printf("Case #%d: IMPOSSIBLE\n", i);
	}
}


int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("output.out", "wt", stdout);

	solve();
	
	return 0;
}