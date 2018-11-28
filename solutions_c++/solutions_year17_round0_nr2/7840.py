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
ll t,a[20],i,n,j;
string s;
int main()
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	FileInOut;
	cin>>t;
	int k=1;
	while(t--)
	{
		cin>>s;
		
		int n=s.length();
		for(int i=0;i<n;i++)
			a[i]=s[i]-48;
//		for(int i=0;i<n;i++)	cout<<a[i]<<" ";
//		cout<<endl;
		for(int i=1;i<n;i)
		{
			if(a[i]>=a[i-1])
				i++;
			else
			{
		//		cout<<"dewfwe"<<endl;
				a[i]=9;
				for(int j=i+1;j<n;j++)
					a[j]=9;
				j=i-1;
				
				if(a[j]==1)
				{
					while(j>=0 && a[j]==1)
					{
						if(j==0)
						{
							a[j]=0;
						}
						else
						{	
							a[j]=9;
						}
						j--;
					}
				}
				else
				{
					a[j]--;
					if(j>0 && a[j]+1==a[j-1])
					{
						int z=a[j]+1;
						a[j]=9;
						j--;
						while(j>=0 && a[j]==z)
						{
							a[j]--;
							j--;
						}
					}
				}
				/*a[j]--;
				int k=j-1;
				while(a[j]==0 && j>0)
				{
					a[j]=9;
					j--;
					a[j]--;
				}
				while(a[k]==a[k-1])
				{
					a[k-1]--;
					k--;
				}
				//a[j]--;	
				break;*/
			}
		}
		int i;
		if(a[0]==0)	i=1;
		else i=0;
		cout<<"CASE #"<<k<<": ";
		for(i;i<n;i++)
			cout<<a[i];
		cout<<endl;
		k++;
	}
	return 0;
}	

