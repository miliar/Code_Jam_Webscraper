#include <bits/stdc++.h>

#define ll long long
using namespace std;

const int MAXN = 2005;
const int MOD = 1000000007;

int cnt[MAXN];

int main(){
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		cout << "Case #" << tc << ": ";
		string s; cin >> s;
		int n = s.length();
		int k; cin >> k;
		int ans = 0;
		for(int i=0;i<=n-k;i++){
			if(cnt[i] % 2 == 0 && s[i] == '-' || cnt[i] % 2 != 0 && s[i] == '+'){
				for(int j=i+1;j<i+k;j++) cnt[j]++;
				ans++;
			}
		}
		int f = 0;
		for(int i=n-k+1;i<n;i++){
			if(cnt[i] % 2 == 0 && s[i] == '-' || cnt[i] % 2 != 0 && s[i] == '+') f |= 1;
		}
		if(f) cout << "IMPOSSIBLE\n";
		else cout << ans << '\n';
		memset(cnt,0,sizeof cnt);
	}
	return 0;
}

