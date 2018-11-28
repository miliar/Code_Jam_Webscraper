#include <bits/stdc++.h>
using namespace std;

#define IOS std::ios_base::sync_with_stdio(false);std:cin.tie(0);std::cout.tie(0);
typedef long long ll;

string s;
string ans;
string t;
bool found = false;
void rec(int pos, bool all) {
	if(pos == s.size()) {
		ans = t;
		found = true;
	}

	for(int i = (all ? '9' : s[pos]); i >= max(pos == 0 ? '1' : '0', pos == 0 ? '0' : t[pos-1]); i--) {
		if(found)
			return;
		t[pos] = i;
		rec(pos + 1, all || i < s[pos]);
	}
}

int main() {
	int casos;
	cin >> casos;

	for(int caso = 1; caso <= casos; caso++) {
		cin >> s;
		ans = string(s.size() - 1, '9');
		t = string(s.size(), '0');
		found = false;

		rec(0, false);

		cout << "Case #" << caso << ": ";
		cout << ans;
		cout << endl;
	}

	return 0;
}
