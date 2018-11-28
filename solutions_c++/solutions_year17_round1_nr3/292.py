#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef complex<double> cplx;

#define sqr(x) ((x)*(x))
#define pb push_back
#define X first
#define Y second
#define sit(a) set<a>::iterator
#define mit(a,b) map<a,b>::iterator

const ll mod=1000000007LL;
const int maxn=100005,maxm=1005;
const double eps=1e-10;
const double pi=acos(-1.0);

int b,d,hd,ad,hk,ak;

int mn=105;

queue<int> q;

int cov(int at,int bt,int ct,int dt)
{
    return at*mn*mn*mn+bt*mn*mn+ct*mn+dt;
}

map<int,int> ma;

ll solve()
{
    ma.clear();
    while(!q.empty()) q.pop();
    ma[cov(hd,ad,hk,ak)]=0;q.push(cov(hd,ad,hk,ak));
    while(!q.empty())
    {
        int x=q.front();q.pop();
        int at=x/(mn*mn*mn),bt=x/(mn*mn)%mn,ct=x/mn%mn,dt=x%mn;
        int da=ma[x];
        if(ct-bt<=0) return da+1;
        int cut;
        if(at-dt>0)
        {
            cut=cov(at-dt,bt,ct-bt,dt);
            if(ma.find(cut)==ma.end()) {q.push(cut);ma[cut]=da+1;}
        }
        if(hd-dt>0)
        {
            cut=cov(hd-dt,bt,ct,dt);
            if(ma.find(cut)==ma.end()) {q.push(cut);ma[cut]=da+1;}
        }
        if(at-max(dt-d,0)>0)
        {
            cut=cov(at-max(dt-d,0),bt,ct,max(dt-d,0));
            if(ma.find(cut)==ma.end()) {q.push(cut);ma[cut]=da+1;}
        }
        if(at-dt>0)
        {
            cut=cov(at-dt,bt+b,ct,dt);
            if(ma.find(cut)==ma.end()) {q.push(cut);ma[cut]=da+1;}
        }
    }
    return mod;
}

int main()
{
    freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T;scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        printf("Case #%d: ",ca);
        scanf("%d %d %d %d %d %d",&hd,&ad,&hk,&ak,&b,&d);
        int re=solve();
        if(re<mod) printf("%d\n",re);else printf("IMPOSSIBLE\n");
        cerr<<"case "<<ca<<" done."<<endl;
    }
    return 0;
}
