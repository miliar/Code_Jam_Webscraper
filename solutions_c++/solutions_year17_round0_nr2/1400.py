#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;
typedef long long ll;

string solve(const string& s) {
	string a = s;
	for (int i=a.length()-1; i>=1; i--) {
		if (a[i] < a[i-1]) {
			for (int j=i; j<a.length(); j++) {
				a[j] = '9';
			}

			a[i-1]--;
		}
	}
	int idx = -1;
	for (int i=0; i<a.length(); i++) {
		if (a[i] != '0') {
			idx  = i;
			break;
		}
	}
	return a.substr(idx);
}
int main(void) {
	int T; scanf("%d", &T);
	for (int tc=1; tc<=T; tc++) {
		string s; cin >> s;
		printf("Case #%d: ", tc);
		cout << solve(s) << "\n";
	}
}
