#include<bits/stdc++.h>
#define PII pair<int,int>
#define f first
#define s second
#define VI vector<int>
#define LL long long
#define MP make_pair
#define LD long double
#define PB push_back
#define ALL(V) V.begin(),V.end()
#define abs(x) max((x),-(x))
#define PDD pair<LD,LD> 
#define VPII vector< PII > 
#define siz(V) ((int)V.size())
#define FOR(x, b, e)  for(int x=b;x<=(e);x++)
#define FORD(x, b, e) for(int x=b;x>=(e);x--)
#define REP(x, n)     for(int x=0;x<(n);x++)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define VVI vector<VI>
using namespace std;
bool ok(vector<LD> V, LD sr, LD u)
    {
    LD s = 0;
    for(auto i : V)
        {
        if(i < sr)s += sr - i;
        }
    return s < u;
    }

void solve()
    {
    int n, kk;
    scanf("%d%d", &n, &kk);
    LD U;
    cin>>U;
    vector<LD> V;
    REP(i, n)
        {
        LD a;
        cin>>a;
        V.PB(a);
        }
    LD p = 0;
    LD k = 1;
    LD sr = -1;
    REP(i, 100)
        {       
        sr = (p + k) / 2;
        if(ok(V, sr, U))
            p = sr;
        else 
            k = sr;
        }
//    cerr<<sr<<endl;
    if(sr > 1)sr = 1;
    LD r = 1;
    for(auto i : V)
        r *= max(i, sr);
    printf("%.8Lf\n", r);
    }
int main()
{
int z;
scanf("%d",&z);
    FOR(iii,1,z)
    {
    printf("Case #%d: ",iii);
    solve();
    }
}
