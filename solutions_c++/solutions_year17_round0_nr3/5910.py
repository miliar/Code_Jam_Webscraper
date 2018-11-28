#include<bits/stdc++.h>
#define sc(x) scanf("%d",&x)
#define scs(x) scanf("%s",&x)
#define scch(x) scanf("%ch",&x)
#define scl(x) scanf("%lld",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define scl2(x,y) scanf("%lld %lld",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define scl3(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)
#define sc4(w,x,y,z) scanf("%d %d %d %d",&w,&x,&y,&z)
#define scl4(w,x,y,z) scanf("%lld %lld %lld %lld",&w,&x,&y,&z)
#define sc5(x,y,z,p,q) scanf("%d %d %d %d %d",&x,&y,&z,&p,&q)
#define scl5(x,y,z,p,q) scanf("%lld %lld %lld %lld %lld",&x,&y,&z,&p,&q)
#define sc6(x,y,z,p,q,r) scanf("%d %d %d %d %d %d",&x,&y,&z,&p,&q,&r)
#define scl6(x,y,z,p,q,r) scanf("%lld %lld %lld %lld %lld %lld",&x,&y,&z,&p,&q,&r)

#define in(x,a,b) (x>=a && x<=b)
#define out(x,a,b) (x<a || x>b)

#define all(a) a.begin(),a.end()
#define UNIQ(a) a.erase(unique(all(a)),a.end())

#define open       freopen("C-small-1-attempt.txt","r",stdin)
#define close      freopen ("output.txt","w",stdout)

#define xx first
#define yy second
#define m_p make_pair
#define pr printf
#define pb push_back
#define pf push_front
#define pof pop_front
#define pob pop_back
#define co(x) cout<<x<<endl
#define prcs(y) printf("Case %d: ",y)
#define gc() getchar()
#define w(t) while(t--)
#define f(i,p,n) for(i=p;i<=n;i++)
#define f2(i,p,n) for(i=p;i>=n;i--)
#define pi acos(-1)
#define ll long long
#define ull unsigned long long
#define mem(a) memset(a,0,sizeof a)
#define memn(a) memset(a,-1,sizeof a)

#define BUG()      pr("Here\n");
#define BUG2()      pr("Not Here\n");

#define MOD 1000000007
#define MX 1000007
#define INF 1000000000

#define countbit(x) __builtin_popcount(x)
#define _fast ios_base::sync_with_stdio(0); cin.tie(0);

/// Hashing Bases & MOD
///           0123456789
#define Base1 10000019ULL
#define Base2 10000079ULL
#define Base3 10000103ULL
#define M1  1000000007ULL
#define M2  1000000009ULL
#define M3  1000000021ULL
#define M4 999995959
#define M5 999998777
using namespace std;

template <typename T> T BigMod (T b,T p,T m)
{
    if (p == 0) return 1;
    if (p%2 == 0)
    {
        T s = BigMod(b,p/2,m);
        return ((s%m)*(s%m))%m;
    }
    return ((b%m)*(BigMod(b,p-1,m)%m))%m;
}
template <typename T> T ModInv (T b,T m)
{
    return BigMod(b,m-2,m);
}
template <typename T> T gcd(T a,T b)
{
    if (!b) return a;
    return gcd(b,a%b);
}

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
typedef map<int,int> MII;
typedef map<int,bool>MIB;
typedef map<string,int>MSI;

priority_queue<pair<ll,PLL> >pq;
pair<ll,PLL>tmp;

int main()
{
    open;
    close;

    ll t,i,j,q,k,n,l,r,st,ed,pos,val,p,x,y,n1,n2,c,dif,idx,st1,st2,ed1,ed2,m;

    scl(t);

    f(l,1,t)
    {
        scl2(n,k);

        pq.push(m_p(n,m_p(0,0)));

        f(j,1,k)
        {
            tmp=pq.top();
            pq.pop();

            val=tmp.xx;
            st=-1*tmp.yy.xx;
            ed=-1*tmp.yy.yy;

//            cout<<val<<" "<<st<<" "<<ed<<endl;

            if(j==1)
            {
                if(!(val&1ll))
                {
                    p=val>>1ll;

                    n1=p-1;
                    n2=p;

                    st1=p-n1;
                    st2=p+1;

                    ed1=p-1;
                    ed2=p+n2;
                }
                else
                {
                    p=(val>>1ll)+1;

                    n1=n2=(val>>1ll);

                    st1=p-n1;
                    st2=p+1;

                    ed1=p-1;
                    ed2=p+n2;
                }
            }
            else
            {
                if(!(val&1ll))
                {
                    p=val>>1ll;
                    p=p+st-1;

                    n1=(val>>1ll)-1;
                    n2=(val>>1ll);

                    st1=p-n1;
                    st2=p+1;

                    ed1=p-1;
                    ed2=p+n2;
                }
                else
                {
                    p=(val>>1ll)+1;

                    p=p+st-1;

                    n1=n2=(val>>1ll);

                    st1=p-n1;
                    st2=p+1;

                    ed1=p-1;
                    ed2=p+n2;
                }
            }

//            cout<<"POS: "<<p<<endl;
//
//            cout<<n1<<" && "<<st1<<" && "<<ed1<<endl;
//            cout<<n2<<" && "<<st2<<" && "<<ed2<<endl<<endl;

            if(n1>0)pq.push(m_p(n1,m_p(-st1,-ed1)));
            if(n2>0)pq.push(m_p(n2,m_p(-st2,-ed2)));
        }

        while(pq.size())pq.pop();

        printf("Case #%lld: %lld %lld\n",l,max(n1,n2),min(n1,n2));
    }
    return 0;
}
