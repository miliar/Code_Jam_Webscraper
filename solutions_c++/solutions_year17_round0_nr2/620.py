#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int main() {
		freopen("A-large.in", "r", stdin);
		freopen("Bsmall.txt", "w", stdout);

	int t, tc = 1; cin >> t;
	while(t--){
		string s; cin >> s;
		int tmp = 20;
		while(tmp--){
			for(int i = 0; i + 1 < s.size(); i++){
				if(s[i] > s[i + 1]){
					s[i]--;
					for(int j = i + 1; j < s.size(); j++)
						s[j] = '9';
					break;
				}
			}
		}
		while(s.size() && s[0] == '0')
			s.erase(0, 1);
		if(!s.size())
			s = "0";
		cout << "Case #" << tc++ << ": " << s << '\n';
	}

	return 0;
}
