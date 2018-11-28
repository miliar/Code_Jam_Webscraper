#include <bits/stdc++.h>
using namespace std;

inline int Flip(string &s, int st, int len) {
	for(int i=0; i<len; ++i) {
		if(s[st+i] == '+') s[st+i] = '-';
		else s[st+i] = '+';
	}
}

inline bool check(string &s, int st, int len) {
	for(int i=0; i<len; ++i) if(s[st+i] == '-') return false;
	return true;
}

int main()
{
	int t, tc=0;
	cin >> t;

	while(t--) {
		string s;
		int k;
		cin >> s >> k;

		int res = 0;
		for(int i=0; i<(int)s.size() && res != -1; ++i) {
			if(i <= (int) s.size() - k) {
				if(s[i] == '-') {
					Flip(s, i, k);
					res++;
				}
			}
			else if(s[i] == '-') res = -1;
		}

		cout << "Case #" << ++tc << ": ";
		if(res == -1) cout << "IMPOSSIBLE\n";
		else cout << res << "\n";
	}

	return 0;
}