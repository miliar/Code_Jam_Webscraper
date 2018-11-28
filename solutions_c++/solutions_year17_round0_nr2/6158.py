#include <iostream>
#include <string>
using namespace std;

int t;
string s;

bool check(string pre) {	//is exist [pre]???
	int i;
	
	for (i = pre.length(); i < s.length(); i++) {
		pre += pre[pre.length() - 1];
	}
	
	for (i = 0; i < s.length(); i++) {
		if (pre[i] == s[i]) continue;
		if (pre[i] < s[i]) return true;
		if (pre[i] > s[i]) return false;
	}
	return true;
}

string solve() {
	int i, j;
	string ret;
	
	for (i = 0; i < s.length(); i++) {
		for (j = 9; j >= 0; j--) {
			if (check(ret + (char)('0' + j))) { break; }
		}
		ret += (char)('0' + j);
	}
	
	string ret2;
	for (i = 0; ret[i] == '0'; i++);
	for (; i < ret.length(); i++) ret2 += ret[i];
	return ret2;
}

signed main() {
	cin >> t;
	for (int id = 1; id <= t; id++) {
		cin >> s;
		string res = solve();
		cout << "Case #" << id << ": " << res << endl;
	}
	return 0;
}