#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vi vector<int>

ll n , k ;
map< ll , ll >  mp ;
pair< ll , ll > ans , tmp ;
map< ll ,ll >::iterator it ;

int main(){
    freopen("C_large.in","r",stdin);
    freopen("C_large.out","w",stdout);
	int t;
	scanf("%d",&t) ;
	for(int T = 1 ;T <= t; T++){
		scanf("%lld%lld",&n,&k) ;
		mp.clear() ;
		mp[n] = 1 ;
		ans = { (n-1)/2 , n/2 } ;
		while( k > 0 ){
			it = mp.end() ;
			it-- ;
			tmp = *it ;
			k -= tmp.se ;
			mp[tmp.fi/2] += tmp.se ;
			mp[(tmp.fi-1)/2] += tmp.se ;
			ans = { (tmp.fi-1)/2 , tmp.fi/2 } ;
			mp.erase(tmp.fi) ;
		}
		printf("Case #%d: %lld %lld\n", T , ans.se , ans.fi ) ;
	}
	return 0;
}
