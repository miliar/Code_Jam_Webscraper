#include <bits/stdc++.h>

using namespace std;

int main(){
	// freopen("A-large.in","r",stdin);
	// freopen("answer.txt","w",stdout);
	cin.sync_with_stdio(0); cin.tie(0);
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc){
		string S; cin >> S;
		int k; cin >> k;
		int f[1010];
		memset(f, 0, sizeof(f));
		int ans = 0;
		// cout << S << " " << k << endl;
		for (int i=0; i<=S.length() - k; ++i){
			if (i > 0) f[i] += f[i-1];
			if (f[i]%2) S[i] = ((S[i] == '+')?'-':'+');
			if (S[i] == '-'){
				f[i]++;
				f[i+k]--;
				S[i] = '+';
				ans++;
			}
		}
		for (int i=S.length()-k+1; i<S.length(); ++i){
			if (i > 0) f[i] += f[i-1];
			if (f[i]%2) S[i] = ((S[i] == '+')?'-':'+');
		}
		bool valid = true;
		for (int i=0; i<S.length(); ++i){
			if (S[i] == '-'){
				valid = false;
			}
		}
		if (valid){
			// cout << ans << endl;
			printf("Case #%d: %d\n", tc, ans);
		}
		else{
			// cout << "IMPOSSIBLE" << endl;
			printf("Case #%d: IMPOSSIBLE\n", tc);
		}
	}
	return 0;
}