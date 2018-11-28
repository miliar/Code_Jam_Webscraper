#include <bits/stdc++.h>
using namespace std;
void input()
{
    freopen("ain.txt","r",stdin);
    freopen("aout.txt","w",stdout);
}
void solveCase(int testCase);
int main()
{
    input();
    int testCases;
    scanf("%d",&testCases);
    for(int testCase = 1; testCase <= testCases; testCase++)
        solveCase(testCase);
}
const int MAXN = 1010;
struct pancake
{
    int r,h;
    void read()
    {
        scanf("%d%d",&r,&h);
    }
}p[MAXN];
bool cmp(pancake p1, pancake p2)
{
    if(p1.r==p2.r) return p1.h>p2.h;
    return p1.r<p2.r;
}
typedef long long ll;
struct maxholder
{
    vector<ll> val;
    maxholder(int k)
    {
        val.resize(k);
    }
    void ins(ll x)
    {
        if(val.size()==0) return;
        if(x<val[0]) return;
        val[0]=x;
        for(int i=0;i<val.size()-1;i++)
        {
            if(val[i]>val[i+1]) swap(val[i],val[i+1]);
        }

    }
    ll get()
    {
        if(val.size()==0) return 0;
        ll ret = 0;
        for(int i=0;i<val.size();i++)
        {
            if(val[i]==0) return -1ll;
            ret += val[i];
        }
        return ret;
    }
    void debug()
    {
        for(int i=0;i<val.size();i++) printf("%lld ",val[i]);
        printf("\n");
    }
};
double pi = acos(-1.0);
void solveCase(int testCase)
{
    printf("Case #%d: ", testCase);
    int n,k;
    scanf("%d%d",&n,&k);
    for(int i=1;i<=n;i++)
        p[i].read();
    sort(p+1,p+n+1,cmp);
    maxholder x = *new maxholder(k-1);
    double maxx = 0;
    for(int i=1;i<=n;i++)
    {
        ll obim = 1ll * p[i].r * p[i].h;
        ll povrs = p[i].r;
        //x.debug();
        ll pre = x.get();
        //printf("obim : %lld polup : %lld pre : %lld \n", obim, povrs, pre);
        if(pre >= 0) maxx = max(maxx, pi * 2 * (pre + obim) + pi * povrs * povrs);
        x.ins(obim);
    }
    printf("%.8f\n", maxx);
}
