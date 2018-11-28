// Oversized Pancake Flipper

#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

#define MAX(x,y) ((x)>(y)?(x):(y))
#define MIN(x,y) ((x)<(y)?(x):(y))
#define MOD(x)   ((x)>0?(x):(-(x)))
#define pb push_back
#define mp make_pair
#define rep(i,n) for(i=0;i<n;i++)
#define repr(i,j,n) for(i=j;i<=n;i++)
#define per(i,n) for(i=n-1;i>=0;i--)
#define endl '\n'
using namespace std;
typedef long long ll;
const ll maxn = (ll) 1e5+9;
const ll mod = (ll) 1e9+7;

string s;

int main()
{
	std::ios::sync_with_stdio(0);
	ll i,j,k,t,T,q,m,l,r,n,ans;
	bool f;
	cin>>T;
	repr(t,1,T) {
		cin>>s>>k;
		n=s.size(),f=1,ans =0;
		for(i=0;i<n && f;i++){
			// cout<<s<<endl;
			if(s[i] == '+') continue;
			else {
				if(n-i < k) f = 0;
				else {
					ans++;
					for(j=i;j<i+k;j++) {
						if(s[j] == '-')s[j]='+';
						else s[j]='-';
					}
				}
			}
		}
		if(f) cout<<"Case #"<<t<<": "<<ans<<endl;
		else cout <<"Case #"<<t<<": "<<"Impossible" << endl;
	}
}