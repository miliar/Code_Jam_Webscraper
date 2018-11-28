#include<iostream>
#include<sstream>
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
	freopen("B-large.in", "rt", stdin);
	freopen("output.out", "wt", stdout);

	long long t;
	int n;
	string res;
	cin >> n;
	for (int k = 1; k <= n; k++) {
		cin >> t;
		stringstream ss;
		ss << t; ss >> res;
		int sz = res.size();
		for (int i = 1; i < sz; i++) {
			if (res[i] < res[i - 1]) {
				for (int j = i; j < sz; j++) res[j] = '9';
				res[i - 1] --;
				for (int j = i - 1; j > 0; j--) {
					if (res[j] < res[j - 1]) {
						res[j] = '9';
						res[j - 1] --;
					}
				}
				break;
			}
		}
		if (res[0] == '0') res.erase(res.begin());
		cout << "Case #" << k <<": " << res << endl;
	}
	
	//solve();
	
	return 0;
}

/*stringstream ss;
			ss << i; ss >> tmp;
			sz = tmp.size();
			if (tmp[sz - 1] == '0') continue;
			for (int j = sz - 1; j > 0; j--) {
				if ((tmp[j] - '0') < (tmp[j - 1] - '0')) {
					valid = false;
					break;
				}
			}
			if (valid) {
				cout << "Case #" << k << ": " << tmp << endl;
				break;
				}*/