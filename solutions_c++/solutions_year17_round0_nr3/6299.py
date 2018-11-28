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

class Compare
{
public:
    bool operator() (ll a,ll b)
    {
        return a<b;
    }
};

ll t,n,k,l,r;
int main()
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	FileInOut;
	int kk=1;
	cin>>t;
	while(t--)
	{
		
		cin>>n>>k;
		priority_queue<int,vector<int>,Compare> q;
		q.push(n);
		//set(a,0);
		k--;
		while(k--)
		{
			int n=q.top();
			q.pop();
			if(n%2==0)
			{
				q.push(n/2-1);
				q.push(n/2);
			}
			else
			{
				q.push(n/2);
				q.push(n/2);
			}
			
		}
		cout<<"CASE #"<<kk<<": ";
		kk++;
		n=q.top(),l,r;
		if(n%2==0)
		{
			l=n/2-1;
			r=n/2;
		}
		else
		{
			l=r=n/2;
		}
		cout<<max(l,r)<<" "<<min(l,r)<<endl;
	}	
	return 0;
}	

