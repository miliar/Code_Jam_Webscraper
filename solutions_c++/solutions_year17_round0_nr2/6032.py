#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	int I = 1;
	while (t--){
		cout << "Case #" << I++ << ": ";
		string s; cin >> s;
		while (true){
			int idx = -1;
			for (int i = 0; i < s.size() - 1; i++){
				if (s[i]>s[i + 1]){
					s[i]--;
					idx = i + 1;
					break;
				}
			}
			if (idx == -1)
				break;
			while (idx < s.size())
				s[idx++] = '9';
		}
		int ind = upper_bound(s.begin(), s.end(), '0') - s.begin();
		while (ind < s.size())
			cout << s[ind++];
		cout << endl;
	}
	return 0;
}