#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front
#define vi vector<int>
#define vl vector<ll>
#define vii vector<pii >
#define vll vector<pll>
#define pll pair<ll,ll>
#define pii pair<int,int>
#define pi 3.14159265358979
#define EL printf("\n")
#define OK printf("OK");
#define foreach(i,t) for(auto i =t.begin();i!=t.end();i++) 
#define pii pair<int,int>
#define pdn(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%d",&n)
#define pn printf("\n")
#define  omap unordered_map
#define PI 3.14159265
#define Inf 1e9
#define mod 1000000007
#define precise(n,k) fixed<<setprecision(k)<<n
#define fequal(a,b) (fabs(a - b)<(1e-9))
typedef long long ll;
typedef long double lf;

ll gcd(ll a,ll b){return (b==0)? a:gcd(b,a%b); }
void nope(int dec = 0){if(!dec) cout<<"NO";else cout<<"YES";exit(0);}

int main()
{
	std::ios::sync_with_stdio(false);cin.tie(0);
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		string s,ans;
		cin>>s;
		for(int i=0;i<s.length();)
		{
			if(i==s.length()-1||s[i]<=s[i+1])
				ans.pb(s[i++]);
			else

			if(s[i]>s[i+1])
			{
				ans.pb(s[i]-1);
				for(int j=i-1;j>=0&&ans[j]>ans[j+1];j--)
				{
						ans[j]--;
						ans[j+1]='9';
				}
				i++;
				while(i<s.length())
				{
					ans.pb('9');
					i++;
				}
			}
		}

		cout<<"Case #"<<p<<": ";
		int j=0;
		while(j<ans.length()-1&&ans[j]=='0')
			j++;
		while(j<ans.length())
			cout<<ans[j++];
		cout<<endl;

	}
	return 0;
}