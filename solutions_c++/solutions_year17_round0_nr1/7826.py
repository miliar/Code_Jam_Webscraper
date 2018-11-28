#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define mod 1000000007
#define INF 1000000000
#define pb push_back
#define ff first
#define ss second
#define pii pair<ll,ll>
#define mp make_pair
#define set(x,y) memset(x,y,sizeof(x))
#define MAXN 100005
#define PI 3.14159265358979323846
//Files
#define FileInOut freopen("C:/Users/Coder/Desktop/input.txt","r",stdin); freopen("C:/Users/Coder/Desktop/output.txt","w",stdout);

//Remainder or Modulus
ll rem(ll a,ll b){return a%b;}
// GCD ALgorithm
ll gcd(ll a,ll b){if (a==0)return b;return gcd(b%a,a);}
// Modular Exponentiation
ll power(ll a,ll b,ll m){ll ans=1;while(b>0){if(b%2!=0){ans=(ans*a)%m;}a=(a*a)%m;b>>=1;}return ans;}
//Fast Input
inline void sf(ll *a){char c=0;while(c<33)c=getc(stdin);*a=0;while(c>33){*a=(*a)*10+c-'0';c=getc(stdin);}}

//  %    ^    5     6
ll t,n,cnt,flag,a[10001];
string s;
int main()
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	FileInOut;
	cin>>t;
	int k=1;
	while(t--)
	{
		flag=1;
		cin>>s>>n;
		set(a,0);
		int len=s.length();
		int cnt=0;
		for(int i=0;i<len;i++)
		{
			if(s[i]=='-')	a[i]=0;
			else	a[i]=1;
		}
		for(int i=0;i<len-n+1;i++)
		{
			if(a[i]==0)	
			{
				cnt++;
				for(int j=i;j<i+n;j++)
				{
					if(a[j]==0)	a[j]=1;
					else	a[j]=0;	
				}
			}	
		}	
	
	
		for(int i=0;i<len;i++)
			if(a[i]==0)
				flag*=0;
		if(!flag)	cout<<"CASE #"<<k<<": IMPOSSIBLE"<<endl;
		else	cout<<"CASE #"<<k<<": "<<cnt<<endl;
		k++;
	}	
	return 0;
}	

