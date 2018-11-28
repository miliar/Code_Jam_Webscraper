#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define INF 0x3F3F3F3F
#define pii pair<int,int>
#define pll pair<long long int, long long int>
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define vpii vector<pair<int,int> > 
#define vll vector<long long int>
#define PI acos(-1.0)

pll findAns(ll llim, ll rlim, ll qtd){
	ll pos = (rlim-llim)/2 + llim;
	if(qtd==1)
		return mp(pos-llim-1,rlim-pos-1);
	
	qtd--;
	if((rlim-llim-1)%2 != 0){
		if(qtd%2 == 0)
			return findAns(pos, rlim, qtd/2);
		else
			return findAns(llim, pos, qtd - qtd/2);
	}
	else{
		if(qtd%2 != 0)
			return findAns(pos, rlim, qtd - qtd/2);
		else
			return findAns(llim, pos, qtd/2);
	}
}

int main(){
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	int tc;
	cin >> tc;
	for(int kase=1; kase<=tc; kase++){
		ll n,k;
		cin >> n >> k;
		
		pll ans = findAns(0, n+1, k);
		
		printf("Case #%d: %lld %lld\n", kase, (ans.first>ans.second?ans.first:ans.second), (ans.first<ans.second?ans.first:ans.second) );
	}
	return 0;
}
