#include<cstdio>
#include<iostream>
#include<string>
using namespace std;

class Solution {
public:
	int minFlips(string s, int len) {
		int ans = 0;
		for (int i = 0; i <= s.size() - len; i++) {
			if (s[i] == '-') {
				for (int j = i; j < i + len; j++) {
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
				ans++;
			}
		}
		for (int i = s.size() - 1; i > s.size() - len; i--) {
			if (s[i] == '-')
				return -1;
		}
		return ans;
	}
};

int main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int T;    // Test Cases
	cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		string ss;    //--------------------------------------XD
		int k;    //oversized flipper
		cin >> ss >> k;
		Solution a;
		int ans = a.minFlips(ss, k);
		cout << "Case #" << kase << ": ";
		if (ans == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << endl;
	}
	return 0;
}