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
#define MOD 1000000007
#define MAX 100005


ll dist[105][105],e[105],s[105],d[105];
double dp[105];


void clr()
{

	for(int i=0;i<=102;i++)
	{
		dp[i]=0;
		e[i]=0;s[i]=0;d[i]=0;
		for(int j=0;j<=102;j++)
			dist[i][j]=0;
	}

}


int main()
{
    //ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    freopen("C-small-attempt0.in","r",stdin);freopen("output.txt","w",stdout);
    int qt;
    sd(qt);
    for(int t=1;t<=qt;t++)
    {
        printf("Case #%d: ",t);
        clr();
        int n,q;
        cin>>n>>q;

        for(int i=1;i<=n;i++)
        	cin>>e[i]>>s[i];

        for(int i=1;i<=n;i++)
        {
        	for(int j=1;j<=n;j++)
        	{
        		int x;
        		cin>>x;
        		if(i+1==j)
        			d[j]=x;
        	}
        }

        int t1,t2;
        cin>>t1>>t2;

        for(int i=1;i<=n;i++)
        {
        	for(int j=i+1;j<=n;j++)
        	{
        		dist[i][j]=dist[i][j-1]+d[j];
        	}
        }


        dp[1]=0;

        for(int i=2;i<=n;i++)
        {
        	dp[i]=1e18;
        	for(int j=1;j<i;j++)
        	{

        		if(e[j]>=dist[j][i])
        		{
        			dp[i]=min(dp[i],dp[j]+((1.0*dist[j][i])/s[j]));
        		}
        	}
        }

        printf("%.8f\n", dp[n]);


    }






    return 0;


}