#include<bits/stdc++.h>
#define nl ('\n')
#define pb push_back
#define MOD 1000000007
#define MAX 100000
#define FOR(i,a,b) for(int i=a;i<=b;i++)       //only for a<=b
typedef long long ll;
using namespace std;
//ll expo(ll x,ll y,ll M){ if(y==0) return 1; ll z = expo(x,y/2,M); if(y&1) return (1ll * ((1ll * x * z)%M) * z)%M; else return (1ll * z * z)%M;}
//ll gcd(ll x,ll y){ if(x==0) return y; return gcd(y%x,x); }
int main()
{
	ios::sync_with_stdio(0);cin.tie(0);
	int t , k , i , j , jj; string s;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>s>>k;
		int n = s.length();int ans = 0;
		for(j=0;j<=n-k;j++){
			if(s[j] == '-'){
				ans++;
				for(jj=j;jj<=j+k-1;jj++){
					if(s[jj] == '+')
						s[jj] = '-';
					else s[jj] = '+';
				}
			}
			//cout<<s<<nl;
		}
		int fl = 0;
		for(j=n-k+1;j<=n-1;j++){
			if(s[j] == '-'){
				fl = 1;
				break;
			}
		}
		if(fl) cout<<"Case #"<<i<<": "<<"IMPOSSIBLE\n";
		else cout<<"Case #"<<i<<": "<<ans<<nl;
	}
	return 0;
}
