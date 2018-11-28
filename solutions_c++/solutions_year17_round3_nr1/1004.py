/*Divyam Goyal - IIT-BHU*/
#include<bits/stdc++.h>
using namespace std;

#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define bitcount    __builtin_popcountll
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mp(a,b) make_pair(a,b)
#define F first
#define S second
#define pb(x) push_back(x)
#define MOD 100000000000000007
#define MAX 100005

bool cmp(pair<int,int> a,pair<int,int> b)
{
	if(a.F==b.F)
		return a.S>b.S;
	return a.F>b.F;
}

pair<int,int>d[1005];
double p1=3.14159265358979323846264338327950288419716939937510582097494459230781640628;
ll a[1005];

ll dp[1005][1005];

int main()
{
    //ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    freopen("A-large.in","r",stdin);freopen("output.txt","w",stdout);
    int qt;
    sd(qt);
    for(int t=1;t<=qt;t++)
    {
        printf("Case #%d: ",t);
        int n,k;
        cin>>n>>k;

        for(int i=1;i<=n;i++)
        {
        	int x,y;
        	cin>>x>>y;
        	d[i]=mp(x,y);
        }

        sort(d+1,d+n+1,cmp);
        double ans=0;
        for(int i=1;i<=n;i++)
        	a[i]=1ll*d[i].F*d[i].S;

        dp[n][0]=0;
        dp[n][1]=a[n];
        for(int i=2;i<=n+1;i++)
        	dp[n][i]=-MOD;

        for(int i=n-1;i>0;i--)
        {
        	for(int j=1;j<=k;j++)
        	{
        		dp[i][j]=max(dp[i+1][j],dp[i+1][j-1]+a[i]);
        	}   	
        }

        for(int i=1;i<=n-k+1;i++)
        {
        	double temp=0;

        	temp=temp+(1.0*p1*(1.0*(1ll*d[i].F*d[i].F)));

        	
        	temp=temp+(2.0*p1*(1.0*(dp[i+1][k-1]+1ll*d[i].F*d[i].S)));
 			
        	

        	ans=max(ans,temp);
        }
        printf("%.8f\n",ans);



    }






    return 0;


}