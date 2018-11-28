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
#define DBG(c) cout << #c << " = " << c << endl;
#define RTIME ((double)clock()/(double)CLOCKS_PER_SEC)
#define fequal(a,b) (fabs(a - b)<(1e-9))
int toint(const string &s) { stringstream ss; ss << s; int x; ss >> x; return x; }
string tostring ( int number ){  stringstream ss; ss<< number; return ss.str();}
typedef long long ll;
typedef long double lf;

ll gcd(ll a,ll b){return (b==0)? a:gcd(b,a%b); }
void nope(int dec = 0){if(!dec) cout<<"NO";else cout<<"YES";exit(0);}

lf need[100];
int val[100][100];
pii token[100][100];
int in[100];
int n,p;
bool check()
{
	for(int i=1;i<=n;i++)
		if(in[i]>p)
			return false;
	return true;
}
int main()
{
	std::ios::sync_with_stdio(false);cin.tie(0);
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int o=1;o<=t;o++)
	{
		cin>>n>>p;
		for(int i=1;i<=n;i++)
			cin>>need[i];
		// /OK OK
		for(int i=1;i<=n;i++)
			for(int j=1;j<=p;j++)
				cin>>val[i][j];

		for(int i=1;i<=n;i++)
			sort(val[i]+1,val[i]+p+1);
		int ans=0;
		 //cout<<"Token"<<endl;
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=p;j++)
			{	
				//lf a=(need[i]*9)/10;
				//lf b=(need[i]*11)/10;
				lf a=((val[i][j]*10)/(need[i]*9));
				lf b=((val[i][j]*10)/(need[i]*11));
				token[i][j]=mp(ceil(b),floor(a));
				//cout<<token[i][j].fi<<","<<token[i][j].se<<" ";
			}
			//cout<<endl;
		}
	

		for(int i=1;i<=n;i++) in[i]=1;

	
		while(check())
		{	
			// cout<<"Indices "<<endl;
			// for(int i=1;i<=n;i++)
			// 	cout<<in[i]<<" ";
			// cout<<endl;
			// char ch=cin.get();
			int req=0;
			int ul=INT_MAX;
			for(int i=1;i<=n;i++)
				{
					req=max(req,token[i][in[i]].fi);
					ul=min(ul,token[i][in[i]].se);
				}
			// 	cout<<"#"<<endl;
			// cout<<req<<" "<<ul<<endl;
			if(ul>=req)
			{
				ans++;
				for(int i=1;i<=n;i++)
					in[i]++;

			}
			else
			{
				for(int i=1;i<=n;i++)
					if(token[i][in[i]].se<req)
						in[i]++;
			}
			//cout<<ans<<endl;
			

		}	

		cout<<"Case #"<<o<<": "<<ans<<endl;

	}		
	return 0;
}