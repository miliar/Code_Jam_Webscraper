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

char flip(char &ch)
    {
    if(ch == '-')ch = '+';
    else ch = '-';
    }

int flip(int a, int b, string &s)
    {
    if(b >= s.size())return -1;
    FOR(i, a, b)
        {
        flip(s[i]);
        }
    return 0;
    }

void solve()
    {
    string s;
    cin>>s;
    int k;
    cin>>k;
    int res = 0;
    bool ok = 1;
    REP(i, s.size())
        {
        if(s[i] == '-')
            {
            res++;
            if(flip(i, i + k - 1, s) == -1)res = 1e9;
            }
        }
    if(res > 1e8)puts("IMPOSSIBLE");
    else printf("%d\n", res);
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
