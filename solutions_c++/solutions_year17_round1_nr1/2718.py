#include <bits/stdc++.h>
#define MAXX 1000005
#define ll long long
#define upperlimit 1000100
#define INF 1e18
#define eps 1e-8
#define endl '\n'
#define pcc pair<char,char>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define MOD 1000000007
#define slld(t) scanf("%lld",&t)
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define plld(t) printf("%lld\n",t)
#define mp(a,b) make_pair(a,b)
#define FF first
#define SS second
#define pb(x) push_back(x)
#define vi vector<int>
#define clr(a) memset(a,0,sizeof(a))
#define debug(a) printf("check%d\n",a)
#define csl ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;
 
ll gcd(ll n1,ll n2){
	if(n1%n2==0)return n2;
	return gcd(n2,n1%n2);
}
ll powmod(ll base,ll exponent)
{
	ll ans=1;
	while(exponent){
		if(exponent&1)ans=(ans*base)%MOD;
		base=(base*base)%MOD;
		exponent/=2;
	}
	return ans;
}
char arr[30][30];
bool taken[200];
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		clr(taken);
		int r,c;
		cin>>r>>c;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
				cin>>arr[i][j];//cout<<arr[i][j];
			//cout<<endl;
		}
		//continue;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				char cc=arr[i][j];
				if(arr[i][j]=='?'||taken[cc])
					continue;
				int k=j-1;
				for(;k>=0;k--)
					{if(arr[i][k]!='?')
						break;
					else
						arr[i][k]=cc;}
				k++;
				int l=j+1;
				for(;l<c;l++)
					{if(arr[i][l]!='?')
						break;
					else
						arr[i][l]=cc;}
				l--;
				int m=i-1,n=i-1;
				for(;m>=0;m--)
				{
					for(int t=k;t<=l;t++)
					{if(arr[m][t]!='?')
						{m=-1;break;}
					//cout<<i<<" "<<j<<" "<<m<<endl;
					if(m!=-1)
					for(int t=k;t<=l;t++)
						assert(arr[m][t]=='?'),arr[m][t]=cc;}
				}
				m=i+1;
				for(;m<r;m++)
				{
					for(int t=k;t<=l;t++)
					if(arr[m][t]!='?')
						{m=r+1;break;}
						//else cout<<"HERE "<<arr[i][j]<<endl;
					//cout<<i<<" "<<j<<" "<<m<<" "<<k<<" "<<l<<endl;
					if(m<r)
					for(int t=k;t<=l;t++)
						assert(arr[m][t]=='?'),arr[m][t]=cc;
					//cout<<i<<" "<<j<<k<<" "<<l<<endl;
				}
				taken[cc]=true;
			}
		}
		cout<<"Case #"<<tt<<": "<<endl;
		for(int i=0;i<r;i++)
			{for(int j=0;j<c;j++)
				cout<<arr[i][j];
				cout<<endl;}

	}
	return 0;
}