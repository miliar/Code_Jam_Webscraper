#include <bits/stdc++.h>
using namespace std;

int dp[20][10][2];
int t;
string inp;
string ans;
int ipos;

int calc(int idx, int last, int locked) {
	if (idx==(int)inp.size()) return 1;
	int &ret = dp[idx][last][locked];
	if (ret!=-1) return ret;
	ret=0;
	if (locked) {
		int num = inp[idx]-'0';
		for (int i=last;i<=num;++i)
			ret=max(ret,calc(idx+1,i,(i==num) ? 1 : 0));
	} else {
		for (int i=last;i<=9;++i)
			ret=max(ret,calc(idx+1,i,0));
	}
	return ret;
}

void backtrack(int idx, int last, int locked) {
	if (idx==(int)inp.size()) return;
	if (locked) {
		int num = inp[idx]-'0';
		for (int i=num;i>=last;--i) {
			if (dp[idx+1][i][(i==num) ? 1 : 0]) {
				ans.push_back('0'+i);
				backtrack(idx+1,i,(i==num) ? 1 : 0);
				return;
			}
		}
	} else {
		for (int i=9;i>=last;--i) {
			if (dp[idx+1][i][0]) {
				ans.push_back('0'+i);
				backtrack(idx+1,i,0);
				return;
			}
		}
	}
}

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	cin >> t;
	for (int tcs=1;tcs<=t;++tcs) {
		memset(dp,-1,sizeof(dp));
		cin >> inp;
		calc(0,0,1);
		ans="";
		backtrack(0,0,1);
		ipos=0;
		while (ipos<(int)ans.size() && ans[ipos]=='0') ++ipos;
		ans=ans.substr(ipos);
		cout << "Case #" << tcs << ": " << ans << '\n';
	}
	return 0;
}
