#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

typedef long long int lld;

void solve_case() {
	int fi=0;
	string s;
	cin >> s;
	for (int i=0; i<s.size()-1; i++) {
		if (s[i] < s[i+1]) {
			fi = i+1;
		} else if (s[i] > s[i+1]) {
			s[fi]--;
			for (int j=fi+1; j<s.size(); j++) {
				s[j] = '9';
			}
			break;
		}
	}
	if (s[0] == '0') {
		s = s.substr(1);
	}
	cout << s << endl;
}

int main() {
	int te;
	cin >> te;
	for (int tt=1; tt<=te; tt++) {
		cout << "Case #" << tt << ": ";
		solve_case();
	}
}

