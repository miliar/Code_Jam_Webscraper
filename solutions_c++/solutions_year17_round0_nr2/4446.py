//OM
#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <queue>
#include <utility>
#include <sstream>
#include <algorithm>
using  namespace  std;

#define  x first
#define  y second
#define  pb push_back
#define  mp make_pair
#define  PI (acos(-1.0))
#define  mem(a,b) memset(a,b,sizeof(a))
#define  Sort(x) sort(x.begin(),x.end())
#define  FOR(i, b, e) for(int i = b; i <= (int)(e); i++)
#define  FORR(i, b, e) for(int i = b; i >=(int)(e); i--)
#define  FORI(i, s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
#define  pr(x) cout<<x<<"\n"
#define  prs(x) cout<<x<<" "
#define  pr2(x,y) cout<<x<<" "<<y<<"\n"
#define  pr3(x,y,z) cout<<x<<" "<<y<<" "<<z<<"\n"
#define  ppr(a) cout<<a.x<<" "<<a.y<<"\n"
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

typedef  long long ll;
typedef  pair <int, int> pii;
typedef  pair <double, double> pdd;
typedef  vector <int> vi;
typedef  vector <pii> vpii;


//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};
//int dy[]={0,1,1,1,0,-1,-1,-1};//8 Direction

#define  EPS 1e-9
#define  MAX 100007
#define  MOD 1000000007

int main()
{
    READ("B-large.in");
    WRITE("out.txt");
    int T;
    long long n;
    scanf("%d",&T);
    FOR(cs,1,T){
        scanf("%lld",&n);
        ll ans=1;
        ll lo=0;
        while(lo<=n){
            ans=max(ans,lo);
            lo=lo*10+9;
        }
        int nDigit=0;
        ll res=0;
        ll m=n;
        while(m>0)m/=10ll,nDigit++;
        FOR(i,1,nDigit)res=res*10+1;

        if(res<=n)ans=max(ans,res);
        FOR(i,2,9){
            ll mul=1;
            FOR(j,1,nDigit){
                if(res+mul>n)break;
                res+=mul;
                if(res<=n)ans=max(ans,res);
                mul*=10;
            }
        }
        printf("Case #%d: %lld\n",cs,ans);
    }
    return 0;
}

