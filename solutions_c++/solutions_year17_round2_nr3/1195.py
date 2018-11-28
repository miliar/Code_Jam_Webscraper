/*While alive CODE*/

                    /*War will happen and code will follow*/

#include <bits/stdc++.h>
using namespace std;
#define mem(x,y) memset(x,y,sizeof(x))
#define bitcount    __builtin_popcountll
#define mod 1000000007
#define N 1000009
#define fast ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define ss(s) cin>>s;
#define si(x)  scanf("%d",&x);
#define sl(x)  cin>>x;
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()
#define S second
#define F first
#define ll long long 
ll power(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll dist[107][107],e[107],s[107],d[107];
double dp[107];

int n,q;


int qt;

void clrsc()
{

	for(int i=0;i<=102;i++)
	{
		dp[i]=0;
		e[i]=0;s[i]=0;d[i]=0;
		for(int j=0;j<=102;j++)
			dist[i][j]=0;
	}

}
void init(){
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
}
void init2(){
	for(int i=1;i<=n;i++)
        {
        	for(int j=i+1;j<=n;j++)
        	{
        		dist[i][j]=dist[i][j-1]+d[j];
        	}
        }
}
void init3(){
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
}
int main()
{
  	freopen("C-small-attempt0.in","r",stdin);
    freopen("output32.out","w",stdout);
    
    cin >> qt;
    for(int t=1;t<=qt;t++)
    {
       
        clrsc();
        
        cin>>n>>q;
        init();

        

        int t1,t2;
        cin>>t1>>t2;

        init2();


        init3();
         printf("Case #%d: ",t);
        printf("%.8f\n", dp[n]);}

return 0;}

