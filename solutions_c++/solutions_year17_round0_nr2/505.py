#include "bits/stdc++.h"
using namespace std;
#define pb push_back
char str[800];
int dp[800][800][2];
string ans;
int solve(int cur, int v, int ok){
	if(!str[cur]) return true;
	if(dp[cur][v][ok]) return false;
	if(ok){
		for(int e = 9; e >= v; e--){
			if(solve(cur+1, e, ok)){
				ans.pb(e + '0');
				return true;
			}
		}
 	} else {
		for(int e = str[cur]-'0'; e >= v; e--)
			if(solve(cur+1, e, e != str[cur]-'0')){
				ans.pb(e + '0');
				return true;
			}
	}
	dp[cur][v][ok] = 1;
	return false;	
}
int main(){
	int cases;
	cin >> cases;
	for(int cs = 1; cs <= cases; cs++){
		cout << "Case #" << cs << ": ";
		memset(str, 0, sizeof(str));
		cin >> str;
		memset(dp, 0, sizeof(dp));
		ans = "";
		for(int e = str[0]-'0'; e >= 0; e--){
			if(solve(0, 0, 0)){
				while(ans.back() == '0') ans.pop_back();
				reverse(ans.begin(), ans.end());
				cout << ans << endl;
				break;
					//cout << char(e + '0');
				//print(1, e, e != str[0]-'0');
			}
		}

	}
	return 0;
}
