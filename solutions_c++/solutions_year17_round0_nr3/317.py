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
const int inf=0x3f3f3f3f;
const int maxn=100005,maxm=1005;
const double eps=1e-10;
const double pi=acos(-1.0);

map<ll,ll> ma;

void solve(ll n,ll k)
{
    ma.clear();ma[-n]=1;
    ll cu=1;mit(ll,ll) it;
    while(1)
    {
        it=ma.begin();
        ll x=-(it->X),y=it->Y;

        //for(mit(ll,ll) ite=ma.begin();ite!=ma.end();++ite) cout<<ite->X<<","<<ite->Y<<"; ";cout<<cu<<"!"<<y<<endl;

        if(cu+y<=k)
        {
            cu+=y;ma.erase(it);
            ma[-((x-1)/2)]+=y;
            ma[-(x/2)]+=y;
        }
        else
        {
            printf("%lld %lld\n",x/2,(x-1)/2);
            return;
        }
    }
}

int main()
{
    freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T;scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        printf("Case #%d: ",ca);
        ll n,k;scanf("%lld %lld",&n,&k);
        solve(n,k);
        cerr<<"case "<<ca<<" done."<<endl;
    }
    return 0;
}
