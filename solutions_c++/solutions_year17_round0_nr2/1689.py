#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

string s;

bool isOK() {
	for(int i=1; i<s.size(); i++) if(s[i] < s[i-1]) return false;
	return true;
}

inline long long get(int idx) {
	string foo = s;
	foo[idx] = (s[idx] - 1);
	for(int i=idx+1; i<s.size(); i++) foo[i] = '9';
	if(foo[0] == '0') foo = foo.substr(1, foo.size()-1);
	long long bar = 0, tmp = 1;
	for(int i=foo.size()-1; i>=0; i--) {
		bar += ((long long) (foo[i] - '0')) * tmp;
		tmp *= 10;
	}
	return bar;
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int NumberOfTestCases;
	cin >> NumberOfTestCases;
	for(int TC = 1; TC <= NumberOfTestCases; TC++) {
		cout << "Case #" << TC << ": ";
		cin >> s;
		if(isOK()) {
			cout << s << endl;
			continue;
		}
		char pre = '0';
		set <long long> st;
		for(int i=0; i<s.size(); i++) {
			if(s[i] >= pre) {
				if(s[i] > pre) st.insert(get(i));
				pre = s[i];
			}
			else break;
		}
		cout << *(st.rbegin()) << endl;
	}
	return 0;
}