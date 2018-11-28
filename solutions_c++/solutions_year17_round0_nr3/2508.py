#include<bits/stdc++.h>
#define nl ('\n')
#define pb push_back
#define MOD 1000000007
#define MAX 100000
typedef long long ll;
using namespace std;
//ll expo(ll x,ll y,ll M){ if(y==0) return 1; ll z = expo(x,y/2,M); if(y&1) return (1ll * ((1ll * x * z)%M) * z)%M; else return (1ll * z * z)%M;}
//ll gcd(ll x,ll y){ if(x==0) return y; return gcd(y%x,x); }
int main()
{
	ios::sync_with_stdio(0);cin.tie(0);
	int i , j , t ; ll n , k , maxim , minim;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n>>k; map<ll,ll> M ; ll tot = 1 , pt = 1 , rank;
		if(k == 1){
			if(n & 1) cout<<"Case #"<<i<<": "<<(n-1)/2<<' '<<(n-1)/2<<nl;
			else cout<<"Case #"<<i<<": "<<(n/2)<<' '<<(n/2) - 1<<nl;
			continue;
		}
		M[n] = 1;
		while(tot < k)
		{
			map<ll,ll> nM;
			for(auto x : M)
			{
				ll y = x.first; ll z = x.second;
				if(y & 1){
					nM[(y-1)/2] += 1ll*2*z;
				}
				else{
					nM[y/2] += z;
					nM[y/2 - 1] += z;
				}
			}
			M = nM;
			pt = 1ll * pt * 2;
			tot += pt;
			if(tot >= k){
				rank = k - tot + pt ;
				break;
			}
		}
		map<ll,ll>::reverse_iterator it = M.rbegin();ll cnt = 0;
		while(it != M.rend())
		{
			cnt += it->second ;
			if(cnt >= rank){
				ll num = it->first;
				if(num & 1) { maxim = (ll)(num-1)/2 ; minim = (ll)(num-1)/2 ; }
				else { maxim = (ll)num/2 ; minim = (ll)(num/2) - 1; }
				break;
			}
			it ++;
		}
		cout<<"Case #"<<i<<": "<<maxim<<' '<<minim<<nl;
	}
	return 0;
}
