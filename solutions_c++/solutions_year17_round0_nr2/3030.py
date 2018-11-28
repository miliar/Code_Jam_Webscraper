#include <bits/stdc++.h>
using namespace std;
string dp[20][10][2];
bool res[20][10][2];
string N;
string solve(int d,int p,bool less) {
	if(d==N.size()) return "";
	if(res[d][p][less]) return dp[d][p][less];
	res[d][p][less]=1;
	if(less) {
		dp[d][p][1]="NG";
		for(int i=p;i<=9;i++) {
			string ret=solve(d+1,i,1);
			if(ret!="NG") dp[d][p][1]=string(1,i+'0')+ret;
		}
	}else {
		dp[d][p][0]="NG";
		for(int i=p;i<=(N[d]-'0');i++) {
			string ret=solve(d+1,i,i<(N[d]-'0'));
			if(ret!="NG") dp[d][p][0]=string(1,i+'0')+ret;
		}
	}
	return dp[d][p][less];
} 
int main() {
	int T;
	cin>>T;
	for(int i=1;i<=T;i++) {
		cin>>N;
		memset(res,0,sizeof(res));
		string ans=solve(0,0,0);
		int len=0;
		while(len<(ans.size()-1)&&ans[len]=='0') len++;
		ans.erase(0,len);
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}
