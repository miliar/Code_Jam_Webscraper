#include <bits/stdc++.h>
using namespace std;

int TC;

int testcase(int tc) {
	cout << "Case #" << tc << ": ";
}

int main() {
	cin >> TC;
	for(int tc = 1; tc <= TC; ++tc) {
		string s;
		cin >> s;
		int n = s.size();
		vector<int> v(n), vr(n);
		for(int i = 0; i < n; ++i) {
			v[i] = vr[n-i-1] = s[i] - '0';
		}
		while(true) {
			if(is_sorted(vr.begin(), vr.end(), greater<int>())) break;
			int j;
 			for(j = 1; j < n; ++j) {
 				if(vr[j-1] > vr[j]) break;
			}
			for(int k = 0; k < j-1; ++k) vr[k] = 9;
			vr[j-1]--;
		}
		testcase(tc);
		if(vr[n-1] != 0) cout << vr[n-1];
		for(int i = n-2; i >= 0; --i) cout << vr[i];
		cout << endl;
	}
}