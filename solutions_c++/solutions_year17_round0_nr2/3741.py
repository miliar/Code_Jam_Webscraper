#include<bits/stdc++.h>
using namespace std;

string s;

#define MAX 25
int dp[MAX][10][2];
int p[MAX][10][2];

int compute(int i,int prev,int flag) {
	
	if(i == s.size()) 
		return 1;
	
	if(dp[i][prev][flag]!=-1)
		return dp[i][prev][flag];
	
	dp[i][prev][flag] = 0;
	
	if(flag ==0) {
		
		for(int j = prev;j<(s[i]-'0');j++)
		{
			if(compute(i+1,j,1)) {
				dp[i][prev][flag] = 1;
				p[i][prev][flag] = j;
			}
		}
		if((prev<=(s[i]-'0')) && compute(i+1,s[i]-'0',0)) {
			dp[i][prev][flag] = 1;
			p[i][prev][flag] = (s[i]-'0');
		}
	}
	else {
		for(int j = prev;j<=9;j++) {
			if(compute(i+1,j,1)) {
				dp[i][prev][flag] = 1;
				p[i][prev][flag] = j;
			}
		}
	}
	return dp[i][prev][flag];
}

string ans = "";

void build(int i,int prev,int flag) {
	
	//cout<<i<<" "<<prev<<" "<<flag<<" "<<s.size()<<endl;
	if(i >= s.size())
		return;
	
	compute(i,prev,flag);
	
	if(p[i][prev][flag] == -1)
		return;
		
//	cout<<p[i][prev][flag]<<endl;
	
	ans = ans + char('0' + p[i][prev][flag]);
	
	if(p[i][prev][flag] == (s[i]-'0'))
		build(i+1,p[i][prev][flag],flag);
	else
		build(i+1,p[i][prev][flag],1);
} 

int main() {
	
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	
	int t;
	cin>>t;
	
	for(int tst = 1;tst<=t;tst++) {
		
		cin>>s;
		
		memset(p,-1,sizeof(p));
		memset(dp,-1,sizeof(dp));
	
		compute(0,0,0);
		
		ans = "";
		build(0,0,0);
		
		string temp = "";
		int idx = 0;
		while(idx<ans.size() && ans[idx]=='0')
			idx++;
		
		if(idx == ans.size())
			temp = "0";
		else {
			while(idx<ans.size())
			{
				temp = temp + ans[idx];
				idx++;
			}
		}
		
		cout<<"Case #"<<tst<<": "<<temp<<endl;
	}
	
	return 0;
}
