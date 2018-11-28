#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define ll long long
#define mp make_pair
#define MAX 100005
#define mod 1000000007
#define pb push_back
#define INF 1e18
#define pii pair<long,int>

int s[MAX];
long k[MAX];
vector<pii> v;
vector< pair<double,double> > u;

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("outputB.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t,n,i,z;
    long d;
    double temp,temp2,minm;
    scanf("%d",&t);
    for(z=1;z<=t;z++)
    {
        scanf("%ld%d",&d,&n);
        for(i=0;i<n;i++)
        {
            scanf("%ld%d",&k[i],&s[i]);
            v.pb(mp(k[i],s[i]));
        }
        printf("Case #%d: ",z);
        sort(v.begin(),v.end());
        for(i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(v[j].s<v[i].s)
                {
                    temp=((double)v[i].s*(double)(v[j].f)-(double)v[j].s*(double)(v[i].f))/(double)((v[i].s-v[j].s));
                    temp2=(double)(v[j].f-v[i].f)/(double)(v[i].s-v[j].s);
                    if(temp<d)
                        u.pb(mp(temp,temp2));
                }
            }
            temp2=(d-(double)v[i].f)/(double)v[i].s;
            u.pb(mp(d,temp2));
        }
        minm=u[0].f/u[0].s;
        for(i=1;i<u.size();i++)
        {
            if(minm>(u[i].f/u[i].s))
                minm=u[i].f/u[i].s;
        }
        printf("%lf\n",minm);
        u.clear();
        v.clear();
    }
    return 0;
}
