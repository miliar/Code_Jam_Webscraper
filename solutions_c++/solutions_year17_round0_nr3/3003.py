#include <bits/stdc++.h>
using namespace std;
#define pii             pair<LL , LL >
#define inf             1111111111
#define in(a)           scanf("%lld", &a)
#define ins(a)          scanf("%s", a)
#define in2(a, b)       scanf("%lld%lld", &a, &b)
#define in3(a, b, c)    scanf("%lld%lld%lld", &a, &b, &c)
#define pn              printf("\n")
#define pr(a)           printf("%lld\n", a)
#define prs(a)          printf("%lld ", a)
#define pr2(a, b)       printf("%lld %lld\n", a, b)
#define pr3(a, b, c)    printf("%lld %lld %lld\n", a, b, c)
#define pcs(a)          printf("Case %lld: ", a)
#define mp              make_pair
#define vi              vector<LL >
#define _ceil(n, a)     ((n)%(a)==0?((n)/(a)):((n)/(a)+1))
#define cl              clear()
#define sz              size()
#define pb              push_back
#define mem(a, b)       memset((a), (b), sizeof(a))
#define all(X)          (X).begin(), (X).end ()
#define iter(it, X)     for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define ext(a)          {printf("%s\n", a); return 0;}
#define oka(x, y)       ((x)>=0&&(x)<row&&(y)>=0&&(y)<col)
#define x               first
#define y               second
#define lc              (2*i)
#define rc              (2*i+1)

typedef long long LL;
//LL  dx[]={1,0,-1,0};LL dy[]={0,1,0,-1}; //4 Direction
//LL  dx[]={1,1,0,-1,-1,-1,0,1,0};LL dy[]={0,1,1,1,0,-1,-1,-1,0};//8 direction
//LL  dx[]={2,1,-1,-2,-2,-1,1,2};LL dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//bool check(LL n, LL pos) {return (n & (1<<pos))>>pos;} //typecast 1 in case of int
//LL  on(LL n, LL pos) {return n | (1<<pos);} //typecast 1 in case of int
//LL  off(LL n, LL pos) {return n & ~(1<<pos);} //typecast 1 in case of int
//bool operator < (const data &d) const{return cost<d.cost;} //reverse in priority queue

const LL M=100010;

map< LL, map<LL, LL> > mep;
map< LL, bool > visited;

void f(LL n)
{
    if (visited[n] == 1) return ;
    visited[n] = 1;

    if (n == 1) mep[1][1] = 1;
    else
    {
        f(n/2);
        for (auto it : mep[n/2]) mep[n][it.first] += it.second;

        if (n > 2)
        {
            f((n-1)/2);
            for (auto it : mep[(n-1)/2]) mep[n][it.first] += it.second;
        }

        mep[n][n] ++;
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("C:\\Users\\Dell\\Desktop\\C-large.in", "r", stdin);
    freopen("C:\\Users\\Dell\\Desktop\\out.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);

    LL n;
    LL i, j, k;
    LL t, cs = 0;

    in(t);
    while (t--)
    {
        visited.clear();
        for (auto a : mep) a.second.clear();
        mep.clear();

        in2(n, k);

        f(n);
        vector < pair < LL, LL > > A;
        for (auto it : mep[n]) A.pb(it);
        reverse(all(A));

        LL sum = 0, p;
        for (auto I : A)
        {
            sum += I.second;
            if (sum >= k)
            {
                p = I.first;
                break;
            }
        }

        printf("Case #%d: ", ++cs);
        pr2(p/2, (p-1)/2);
    }



return 0;
}

