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
int n,m,a,b,c,d;

const int MXN = 1e6 + 6;
int t[MXN];

int ler(int i)
    {
    int rr = 0;
    while(t[i-rr] == 0)rr++;
    return rr;
    }
int rig(int i)
    {
    int rr = 0;
    while(t[i+rr] == 0)rr++;
    return rr;
    }

void solve()
    {
    int n, k;
    cin>>n>>k;
    FOR(i, 1, n)
        {
        t[i] = 0;
        }
    
    t[0] = t[n+1] = 1;
    
    FOR(i, 1, k)
        {
        PII best = MP(-1, -1);
        int idx = -1;
        FOR(j, 1, n)
            {
            int l = ler(j) - 1;
            int r = rig(j) - 1;
            PII now = MP(min(l, r), max(l, r));
            if(now > best)
                {
                best = now;
                idx = j;
                }
            }
        t[idx] = 1;
        if(i == k)cout<<best.s<<" "<<best.f<<endl;
        }
    }
main()
{
int z;
scanf("%d",&z);
FOR(iii,1,z)
  {
  printf("Case #%d: ",iii);
  solve();
  }
}
