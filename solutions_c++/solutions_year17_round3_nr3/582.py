#include <bits/stdc++.h>
#define MAX 1000005
#define ll long long
#define upperlimit 1000100
#define INF 1e18
#define eps 1e-7
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
double p[MAX];
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out3.txt", "w", stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		
		double ans=1.0,mul=0;
		int no=0;
	    int n,k;
	    cin>>n>>k;
	    double u;
	    cin>>u;
	    for(int i=1;i<=n;i++)
	    {
	        cin>>p[i];
	    }
	    n++;
	    p[n]=1.00000;
	    sort(p+1,p+n+1);
	    for(int i=1;i<=n;i++)
	    {
	    	if(u-(i-1)*(p[i]-p[i-1])+eps>0)
	    	{
	    		u-=(i-1)*(p[i]-p[i-1]);
	    		mul =p[i];
	    		no=i;
	    	}
	    	else
	    	{
	    		mul=p[i-1]+u/(i-1);
	    		no=i-1;
	    		break;
	    	}
	    	//cout<<i<<" "<<u<<endl;
	    }
	    //cout<<mul<<endl;
	    for(int i=1;i<=no;i++)
	    	ans*=mul;
	    for(int i=no+1;i<=n;i++)
	    	ans*=p[i];
	    /*for(double i=0.00000;i<=1.000000;i+=0.0000002)
	    {
	        double ans=1.0;
	        double tempu=u;
	        for(int j=0;j<n;j++)
	        {
	            if(p[j]<i)
	            {
	                tempu-=i-p[j];
	                ans*=i;
	            }
	            else
	            ans=ans*p[j];
	        }
	        if(tempu+eps>=0.000000)
	            prt=max(prt,ans);
	    }*/
		cout<<"Case #"<<tt<<": ";//<<2*n-2*ans<<endl;
		//ans=3.14159265359*ans;
		printf("%0.9llf\n",ans);
	}
	//cout<<t<<endl;
	return 0;
}