#include <bits/stdc++.h>
using namespace std;
string s;
int dp[20][20][20], ans[20][20][20];
void print(int pos, int pre, int eq){
	if(pos >= s.size()) return;
	if(ans[pos][pre][eq]) cout << ans[pos][pre][eq];
	if(eq == 0){
		print(pos+1, 9, 0);
	}
	else{
		if(ans[pos][pre][eq] == s[pos] - '0'){
			print(pos+1, ans[pos][pre][eq], 1);
		}
		else print(pos+1, ans[pos][pre][eq], 0);
	}
}
int rec(int pos, int pre, int eq){
	if(pos >= s.size()) return 1;
	if(dp[pos][pre][eq] != -1) return dp[pos][pre][eq];
	if(eq == 0){
		dp[pos][pre][eq] = rec(pos+1, 9, 0);
		ans[pos][pre][eq] = 9;
	}
	else{
		dp[pos][pre][eq] = 0;
		for(int i=9; i>=pre; --i){
			if(i == s[pos] - '0'){
				int val = rec(pos+1, i, 1);
				if(val){
					dp[pos][pre][eq] = 1;
					ans[pos][pre][eq] = i;
					break;
				}
			}
			else if(i < s[pos] - '0'){
				int val = rec(pos+1, i, 0);
				if(val){
					dp[pos][pre][eq] = 1;
					ans[pos][pre][eq] = i;
					break;
				}				
			}
		}
	}	
	// cout << pos << ' ' << pre << ' ' << eq << endl << dp[pos][pre][eq] << endl;
	return dp[pos][pre][eq];
}
int main(){
	int t; cin >> t;
	int cs = 0;
	while(t--){
		++cs;
		cout << "Case #" << cs << ": ";
		memset(dp, -1, sizeof dp);
		cin >> s;
		s = ' ' + s;
		int yes = 0;
		for(int i=9; i>=0; --i){
			if(i == s[1] - '0'){
				int val = rec(2, i, 1);	
				if(val){
					if(i) cout << i;
					print(2, i, 1);
					break;
				}
			}
			else if(i < s[1] - '0'){
				int val = rec(2, i, 0);
				if(val){
					if(i) cout << i;
					print(2, i, 0);
					break;
				}
			}
		}
		cout << endl;
	}
}

