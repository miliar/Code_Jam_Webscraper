#include<bits/stdc++.h>
#include <ext/numeric>
using namespace std;
#define sc(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sc4(a,b,c,d) scanf("%d%d%d%d",&a,&b,&c,&d)
#define scd(a) scanf("%lf",&a)
#define scd2(a,b) scanf("%lf%lf",&a,&b)
#define scd3(a,b,c) scanf("%lf%lf%lf",&a,&b,&c)
#define scd4(a,b,c,d) scanf("%lf%lf%lf%lf",&a,&b,&c,&d)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ALL(x) x.begin(), x.end()
#define BUFF ios::sync_with_stdio(false);
#define endl "\n"
#define power(a,x) __gnu_cxx::power(a, x)
#define forN(i,n) for(int i=0;i<n;i++)
#define eps 1e-5
#define INF INT_MAX
#define INFLL LLONG_MAX
#define gcd(a,b) __gcd(a,b)
typedef unsigned long long int ull;
typedef long long int ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vector<int> >vvi;
#define MAXN 1440
int v[MAXN];
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        vector<pair<ii,int> >vv;
        int n,m;
        cin>>n>>m;
        for(int i=0;i<MAXN;i++)
        {
            v[i]=-1;
        }
        int c0=720;
        int c1=720;
        for(int i=0;i<n;i++)
        {
            int a,b;
            cin>>a>>b;
            vv.pb(mp(mp(a,b),0));
            for(int j=a;j<b;j++)
            {
                v[j]=0;
                c0--;
            }
        }
        for(int i=0;i<m;i++)
        {
            int a,b;
            cin>>a>>b;
            vv.pb(mp(mp(a,b),1));
            for(int j=a;j<b;j++)
            {
                v[j]=1;
                c1--;
            }
        }
        sort(vv.begin(),vv.end());
        priority_queue<pair<int,ii> > pq0,pq1;
        for(int i=0;i<vv.size()-1;i++)
        {
            if(vv[i].se==vv[i+1].se)
            {
                if(vv[i].se==0)
                {
                    pq0.push(mp(-abs(vv[i].fi.se-vv[i+1].fi.fi),mp(vv[i].fi.se,vv[i+1].fi.fi)));
                }
                else
                {
                    pq1.push(mp(-abs(vv[i].fi.se-vv[i+1].fi.fi),mp(vv[i].fi.se,vv[i+1].fi.fi)));
                }
            }
        }
        if(vv.size()>1)
        {
            if(vv[vv.size()-1].se==vv[0].se)
            {
                if(vv[0].se==0)
                {
                    pq0.push(mp(-abs(vv[vv.size()-1].fi.se-(vv[0].fi.fi+MAXN)),mp(vv[vv.size()-1].fi.se,vv[0].fi.fi)));
                }
                else
                {
                    pq1.push(mp(-abs(vv[vv.size()-1].fi.se-(vv[0].fi.fi+MAXN)),mp(vv[vv.size()-1].fi.se,vv[0].fi.fi)));
                }
            }
        }
        while(!pq0.empty())
        {
            pair<int,ii> aux=pq0.top();
            pq0.pop();
            //cout<<aux.fi<<endl;
            //cout<<aux.se.fi<<" "<<aux.se.se<<endl;
            for(int i=0;i<-aux.fi;i++)
            {
                if(c0==0)break;
                int pos=(aux.se.fi+i)%MAXN;
                v[pos]=0;
                c0--;
            }
        }
        while(!pq1.empty())
        {
            pair<int,ii> aux=pq1.top();
            pq1.pop();
            //cout<<aux.fi<<endl;
            //cout<<aux.se.fi<<" "<<aux.se.se<<endl;
            for(int i=0;i<-aux.fi;i++)
            {
                if(c1==0)break;
                int pos=(aux.se.fi+i)%MAXN;
                v[pos]=1;
                c1--;
            }
        }

        int curr=-1;
        for(int ii=0;ii<2*MAXN;ii++)
        {
            if(c0==0)break;
            int i=ii%MAXN;
            if(v[i]!=-1)
            {
                curr=v[i];
            }
            if(curr==0 && v[i]!=0)
            {
                v[i]=0;
                c0--;
            }
        }
        curr=-1;
        for(int ii=0;ii<2*MAXN;ii++)
        {
            if(c1==0)break;
            int i=ii%MAXN;
            if(v[i]!=-1)
            {
                curr=v[i];
            }
            if(curr==1 && v[i]!=1)
            {
                v[i]=1;
                c1--;
            }
        }
        for(int ii=0;ii<2*MAXN;ii++)
        {
            if(c0==0)break;
            int i=ii%MAXN;
            if(v[i]==-1)
            {
                v[i]=0;
                c0--;
            }
        }
        for(int ii=0;ii<2*MAXN;ii++)
        {
            if(c1==0)break;
            int i=ii%MAXN;
            if(v[i]==-1)
            {
                v[i]=1;
                c1--;
            }
        }
        int total1=0;
        for(int i=0;i<MAXN;i++)
        {
            //if(v[i]==-1)cout<<"ERRO"<<endl;
            //cout<<v[i]<<endl;
            if(v[i]!=v[(i+1)%MAXN])
            {
                total1++;
            }
        }
        cout<<"Case #"<<tt<<": "<<total1<<endl;
    }
    return 0;
}
