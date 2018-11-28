#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 100000 + 10;
const int M = 1000000007;
const double PI = atan(1) * 4;
const int oo = 1000000000;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
#define pb push_back 
#define all(c) (c).begin(),(c).end()
int dp[19][10][2];
string s;
bool calc(int u, int ls, bool f){
	int &ret=dp[u][ls][f];
	if(u==s.size())return ret=1;
	if(ret!=-1)return ret;
	int k=s[u]-'0';
	if(f)k=9;
	for(int i=k; i>=ls; --i)
		if(calc(u+1,i,i<k||f))
			return ret=true;
	return false;
}
string ans;
void solve(int u, int ls, bool f){
	if(u==s.size()){
		cout<<ans<<endl;
		return;
	}
	int k=s[u]-'0';
	if(f)k=9;
	for(int i=k; i>=ls; --i)
		if(calc(u+1,i,i<k||f)){
			if(i || ans.size())
				ans+=i+'0';
			solve(u+1,i,i<k||f);
			return;
		}
}
int main(){
	#ifndef ONLINE_JUDGE
		freopen("B-large.in", "r", stdin);
		freopen("output.txt","w",stdout);
	#endif
	int T;
	cin>>T;
	int t=1;
	while(T--){
		cin>>s;
		memset(dp,-1,sizeof(dp));
		calc(0,0,0);
		ans="";
		cout<<"Case #"<<t++<<": ";
		solve(0,0,0);
	}
	
}


