// Tidy Numbers Small

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

string num,ans;

int main()
{
	std::ios::sync_with_stdio(0);
	ll i,j,k,t,T,q,m,l,r,n;
	cin>>T;
	repr(t,1,T) {
		cin>>num;
		ans = num;
		n=num.size();
		rep(i,n-1) {
			l=num[i]-'0'; r=num[i+1]-'0';
			if(l > r) {
				for(j=i-1;j>=0;j--){if(ans[j]!=ans[i])break;}
				j++;
				ans[j]=((l-1)+'0');
				for(m=j+1;m<n;m++)ans[m]=(9+'0');
				break;
			}
		}
		for(k=0;k<n;k++){if(ans[k]-'0' > 0)break;}
		cout<<"Case #"<<t<<": ";
		for(i=k;i<n;i++)cout<<ans[i];cout<<endl;
	}
}