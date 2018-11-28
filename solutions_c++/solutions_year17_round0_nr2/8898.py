#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll dp[20][2][1100];
ll k;
set<ll>se;
string conv(ll num)
{
	string str;
	while(num){
		str = str + (char)(num%10 + '0');
		num /= 10;
	}
	reverse(str.begin(),str.end());
	return str;
}
ll solve(string & str,ll id,ll sml,ll mask, ll curr)
{
	if(id == str.length()){
		if(mask != 1){
			se.insert(curr);
			return 1;
		}
		return 0;
	}
/*	if(dp[id][sml][mask] != -1){
		return dp[id][sml][mask];
	}*/
	ll an = 0;
	for(ll i = 1;i < 10;i++){
		if(mask&(1<<i)){
			an = i;
		}
	}
	ll limit = 9;
	if(sml){
		limit = str[id] - '0';
	}
	ll ans = 0;
	ll sm2 = 0;
	for(ll i = an;i <= limit;i++){
		if(i < str[id] - '0'){
			sm2 = 0;
		}
		else{
			sm2 = sml;
		}
		ans += solve(str,id+1,sm2,mask|(1<<i),curr*10 + i);
	}
	return (dp[id][sml][mask] = ans);
}
int main()
{
	ll i,n,j,k,l,t;
	set<ll> :: iterator it;
	string str;
	memset(dp,-1,sizeof(dp));
        n = 1000000000000000000;
        str = conv(n);
        solve(str,0,1,0,0);
	cin >> t;
	for(i = 1;i <= t;i++){
		memset(dp,-1,sizeof(dp));
		cin >> n;
		cout << "Case #" << i << ": ";
		if(se.find(n) != se.end()){
			cout << n << endl;
		}
		else{
			it = se.lower_bound(n);
			it--;
			cout << *it << endl;
		}
//		str = conv(n);
//		cout << solve(str,0,1,0) << endl;
	}
}
