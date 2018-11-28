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


double p[100];
int main()
{
    //ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    freopen("C-small-1-attempt2.in","r",stdin);freopen("output.txt","w",stdout);
    int qt;
    sd(qt);
    for(int t=1;t<=qt;t++)
    {


        printf("Case #%d: ",t);
        int n,k;
        cin>>n>>k;
        double u;
        cin>>u;

        for(int i=1;i<=n;i++)
        	cin>>p[i];

        sort(p+1,p+n+1);

        for(int i=2;i<=n;i++)
        {	
        	if(u==0)break;
        	int cnt=i-1;

        	double temp=(1.0*u)/cnt;

        	if(temp>=p[i]-p[i-1])
        	{
        		for(int j=i-1;j>0;j--)
        		{
        			u-=p[j+1]-p[j];
        			p[j]=p[j+1];
        		}
        	}
        	else
        	{
        		for(int j=1;j<i;j++)
        		{
        			p[j]+=temp;
        		}
        		u=0;
        	}
        }

        double temp=(1.0*u)/n;
        
        double ans=1;
        for(int i=1;i<=n;i++)
        {
        	p[i]+=temp;

        	ans=ans*p[i];
        }
        printf("%.8f\n",ans);





    }






    return 0;


}