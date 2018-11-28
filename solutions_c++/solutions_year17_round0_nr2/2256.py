#include <bits/stdc++.h>

using namespace std;

void ans(string s) {
	static int n = 1;
	cout << "Case #" << n++ << ": " << s << '\n';
}

bool tidy(string s) {
	if (s.size() < 2) return true;
	for (int i = 0; i < s.size() - 1; i++) {
		if (s[i] > s[i + 1]) return false;
	}
	return true;
}

int main() { ios_base::sync_with_stdio(false);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		
		again:
		if (s.size() == 1) {
			ans(s);
		} else {
			int p = -1;
			for (int i = 0; i < s.size() - 1; i++) {
				if (s[i] > s[i + 1]) { p = i; break; }
			}
			
			if (p == -1) ans(s);
			else {
				s[p]--;
				for (int i = p + 1; i < s.size(); i++) {
					s[i] = '9';
				}
				int f = 0;
				while (s[f] == '0') f++;
				s = s.substr(f);
				if (!tidy(s)) goto again;
				ans(s);
			}
		} 
	}
	
	return 0;
}
