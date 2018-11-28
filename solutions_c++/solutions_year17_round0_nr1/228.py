#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<lint, lint> pi;

void solve(){
	string s;
	int k;
	cin >> s >> k;
	int ans = 0;
	for(int i=0; i+k-1<s.size(); i++){
		if(s[i] == '-'){
			for(int j=i; j<i+k; j++) s[j] = '-' + '+' - s[j];
			ans++;
		}
	}
	if(count(s.begin(), s.end(), '-')){
		puts("IMPOSSIBLE");
	}
	else{
		cout << ans << endl;
	}
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d: ",i);
		solve();
	}
}
