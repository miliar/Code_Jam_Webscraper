#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int main() {
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("Asmall.txt", "w", stdout);

	int t, tc = 1; cin >> t;
	while(t--){
		string s; cin >> s;
		int k; cin >> k;
		int res = 0;
		vector<bool>f(s.size() + 1, 0);
		bool flip = 0;
		bool ok = 1;
		for(int i = 0; i < s.size(); i++){
			if(f[i])
				flip = !flip;
			if((!flip && s[i] == '-') || (flip && s[i] == '+')){
				if(i + k <= s.size()){
					res++;
					flip = !flip;
					f[i + k] = !f[i + k];
				}
				else ok = 0;
			}
		}
		cout << "Case #" << tc++ << ": ";
		if(ok)
			cout << res << '\n';
		else cout << "IMPOSSIBLE\n";
	}

	return 0;
}
