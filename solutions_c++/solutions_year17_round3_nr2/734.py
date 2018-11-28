#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <unordered_map>
using namespace std;
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()
#define FOR(i,s,n) for(int i=(s);i<(n);++i)
#define REP(i,n) FOR(i,0,(n))
#define PB(x) push_back((x))
#define CLR(a,v) memset((a),(v),sizeof((a)))
typedef long long ll;

int ac,aj;
pair<int,int> pc[111], pj[111];
pair<int,int> p[222];

int s[1500], d[1500], t[1500];
int f[1500][733][2], n;

int g(int i, int x, int k)
{
    int pv = k==1?1:-1;
    if(i>0&&t[i-1]!=0&&t[i-1]!=pv)return 333;

    if(x<0)return 333;
    if(f[i][x][k]!=-1)return f[i][x][k];
    if(t[i]==1&&x<1) return 333;

    if (i==n-1)
    {
        if(t[i]==1)x-=1;
        return (t[i]!=pv) + (t[0]!=t[i])+(x==0?0:333);
    }

    if(t[i]==0)
    {
        return f[i][x][k]=min((pv!=1)+g(i+1,x-1,1), (pv!=-1)+g(i+1,x,0));
    }

    return f[i][x][k]=(pv!=t[i])+g(i+1,t[i]==1?x-1:x,t[i]==1?1:0);
}

void solve()
{
    scanf("%d %d", &ac, &aj);
    REP(i,ac)scanf("%d %d", &pc[i].first, &pc[i].second);
    REP(i,aj)scanf("%d %d", &pj[i].first, &pj[i].second);

    int m=0;
    REP(i,ac)p[m].first = pc[i].first, p[m++].second=pc[i].second;
    REP(i,aj)p[m].first = pj[i].first, p[m++].second=-pj[i].second;

    sort(p,p+m);

    n = 0;
    if (p[0].first != 0)
    {
        s[n]=0;
        d[n] = p[0].first;
        FOR(k,s[n],s[n]+d[n])t[k]=0;
        ++n;
    }

    REP(i,m)
    {
        s[n]=p[i].first;
        d[n]= abs(p[i].second) - p[i].first;
        FOR(k,s[n],s[n]+d[n])t[k]=p[i].second > 0 ? 1 : -1;
        ++n;

        if (abs(p[i].second) != 1440)if(i==m-1||abs(p[i].second)!=p[i+1].first)
        {
            s[n]=abs(p[i].second);
            d[n]= (i==m-1)?1440-s[n]:p[i+1].first-s[n];
            FOR(k,s[n],s[n]+d[n])t[k]=0;
            ++n;
        }
    }

    //printf("\n");REP(i,n)printf("%d %d\n", t[i], d[i]);

    int res = 333;
    n=24*60;
    FOR(a,-1,2)if(a!=0)FOR(b,-1,2)if(b!=0)
    {
        int sa=t[0], sb=t[n-1];
        if(t[0]==0)t[0]=a;
        if(t[n-1]==0)t[n-1]=b;

        REP(i,n)REP(j,733)REP(k,2)f[i][j][k]=-1;

        for(int i=n-1;i>=0;--i)REP(j,733)REP(k,2)g(i,j,k);
        res=min(res,f[0][720][t[0]==1?1:0]);


        t[0]=sa, t[n-1]=sb;
    }


    printf("%d\n",res);
}


int main()
{
    //freopen("../input.txt", "r", stdin);
    //freopen("../data/B-small-attempt0.in", "r", stdin);
    freopen("../data/B-large.in", "r", stdin);

    freopen("../output.txt", "w+", stdout);

    int T;
    scanf("%d", &T);
    REP(i, T)
    {
        printf("Case #%d: ", i+1);
        solve();
    }

    return 0;
}
