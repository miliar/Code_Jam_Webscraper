#include<bits/stdc++.h>
using namespace std;

#define FRE(i,a,b)  for(i = a; i <= b; i++)
#define FRL(i,a,b)  for(i = a; i < b; i++)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define all(x)      x.begin(),x.end()
#define un(x)       x.erase(unique(all(x)), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define sl(n)       scanf("%lld", &n)
#define sll(a,b)    scanf("%lld %lld", &a, &b)
#define slll(a,b,c) scanf("%lld %lld %lld", &a, &b, &c)
#define D(x)        cerr << #x " = " << (x) << '\n'
#define DBG         cerr << "Hi" << '\n'
#define pb          push_back
#define PI          acos(-1.00)
#define xx          first
#define yy          second
#define eps         1e-9

typedef long long int LL;
typedef double db;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;

#define MAX     50

struct point{
    int v;
    bool ed;
    int type;
};

inline bool operator < ( point a, point b)
{
    if(a.v == b.v)
        return a.ed < b.ed;
    return a.v < b.v;
}

int n, p, R[MAX+10], A[MAX+10][MAX+10];
vector<point>B;

pii go(int a, int b)
{
    pii ret;
    double mn = (a*10.00)/(11.00*b);
    ret.xx = ceil(mn)+.5;

    double mx = (a*10.00)/(9.00*b);
    ret.yy = floor(mx)+.5;

    if(ret.xx == 0)
        ret.xx++;
    return ret;
}

int cnt[MAX+10], taken[MAX+10];

bool make()
{
    for(int i = 1; i<=n; i++)
    {
        if(cnt[i] <= 0)
            return false;
    }
    for(int i = 1; i<=n; i++)
        cnt[i]--, taken[i]++;
    return true;
}

int solve()
{
    sort(all(B));
    int ans = 0;
    for(int i = 0; i<B.size(); i++)
    {
        if(B[i].ed == 0)
        {
            cnt[B[i].type]++;
            ans += make();
        }
        else
        {
            if(taken[B[i].type] == 0)
                cnt[B[i].type]--;
            else
                taken[B[i].type]--;
        }
    }
    return ans;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i, j, cs, t;
    sf(t);
    FRE(cs,1,t)
    {
        B.clear();
        mem(cnt,0);
        mem(taken,0);
        sff(n,p);
        FRE(i,1,n)
            sf(R[i]);
        FRE(i,1,n)
        {
            FRE(j,1,p)
            {
                sf(A[i][j]);
                pii range = go(A[i][j], R[i]);
                if(range.xx > range.yy)
                    continue;
                B.pb({range.xx, 0, i});
                B.pb({range.yy, 1, i});
            }
        }

        printf("Case #%d: %d\n",cs,solve());
    }
    return 0;
}


