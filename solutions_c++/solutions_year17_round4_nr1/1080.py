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
int n, P;
map<pair<int, VI>, int> memo;
int backtrack(int mod, VI cnt)
    {
    int s = 0;
    for(auto i : cnt)s += i;
    if(s == 0)return 0;
    
    mod %= P;
    if(memo.count(MP(mod, cnt)))return memo[MP(mod, cnt)];
    
    
    int r = 0;
    REP(i, cnt.size())
        {
        if(cnt[i])
            {
            cnt[i]--;
            r = maxi(r, backtrack(mod + i, cnt));
            cnt[i]++;
            }
        }
    return memo[MP(mod, cnt)] = r + (mod == 0);
    }
void solve()
    {
    memo.clear();
    cin>>n>>P;
    VI cnt;
    cnt.resize(4);
    FOR(i, 1, n)
     {
     int a;
     cin>>a;
     cnt[a % P]++;
     }
    int result = cnt[0];
    cnt[0] = 0;
    result += backtrack(0, cnt);
    cout<<result<<endl;
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
