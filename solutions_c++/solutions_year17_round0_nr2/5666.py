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

void solve()
    {
    string s;
    cin>>s;
    bool diff = 0;
    do {
        diff = 0;
        FOR(i, 1, s.size() - 1)
            {
            if(s[i-1] > s[i])
                {
                diff = 1;
                s[i-1]--;
                while(i < s.size())s[i++] = '9'; 
                }
            }
        while(s[0] == '0')s.erase(s.begin());
        }
    while(diff);
    cout<<s<<endl;
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
