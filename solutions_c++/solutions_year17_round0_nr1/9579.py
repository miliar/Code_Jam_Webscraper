#include <bits/stdc++.h>
using namespace std;
int T;
string s;
int k;
int main(){
	freopen("A.inp","r",stdin);
	freopen("A.out","w",stdout);
	cin >> T;
	int cnt = 0;
	while(T--){
		cout << "Case #" << ++cnt << ": ";
		cin >> s;
		cin >> k;
		int ans = 0;
		for(int i = 0; i < s.size() - k + 1; i++){
			if(s[i] == '-'){
				for(int j = 1; j <= k; j++){
					if(s[i + j - 1] == '+') s[i + j - 1] = '-';
					else s[i + j - 1] = '+';
				}
				ans++;
			}
		}
		for(int i = 0; i < s.size(); i++) if(s[i] == '-') ans = -1;
		if(ans == -1) cout << "IMPOSSIBLE\n";
		else cout << ans << "\n";
	}
}