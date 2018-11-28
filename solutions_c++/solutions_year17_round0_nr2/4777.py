#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, int> plli;
typedef pair<double,double> pdd;
typedef pair<string,int> psi;
const int MOD = 1e9 + 7;

int t,len;

string n;

int dp[200][20][2];

int calc(int idx ,int prev, bool greater){
	if(idx == len){
		return 1;
	}
	int &ret = dp[idx][prev][greater];
	if(ret != -1)
		return ret;
	ret = 0;
	for(int i = prev ; i <= 9 ; i++){
		if(!greater && (i > (n[idx]-'0')))
			break;
		bool nw = ((n[idx]-'0')>i) ? 1 : greater;
		ret =ret || calc(idx + 1,i,nw);
	}	
	return ret;
}

string res = "";

void build(int idx , int prev , bool greater){
	if(idx == len)
		return;
	for(int i = 9 ; i >= prev ; i--){
		if(!greater && (i > (n[idx]-'0')))
			continue;
		bool nw = ((n[idx]-'0')>i) ? 1 : greater;
		if(calc(idx + 1,i,nw)){
			res += (i + '0');
			build(idx+1,i,nw);
			return;
		}
	}	
}
int main() {
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	for(int it = 1 ; it <= t ; it++){
		cin >> n;
		string ans = "";
		while(ans.size() < ((int)n.size())-1){
			ans += '9';
		}
		len = n.size();
		memset(dp,-1,sizeof dp);
		if(calc(0,1,0)){
			res = "";
			build(0,1,0);
			ans = res;
		}
		printf("Case #%d: %s\n",it,ans.c_str() );
	}   	
    return 0;
}