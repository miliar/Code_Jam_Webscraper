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
char s[MAX];
int main()
{
    READ("A-large.in");
    WRITE("out.txt");
    int T,n,k;
    scanf("%d",&T);
    FOR(cs,1,T){
        getchar();
        scanf("%s%d",s,&k);
        n=strlen(s);
        int cnt=0;
        FOR(i,0,n-k){
            if(s[i]=='-'){
                FOR(j,i,i+k-1){
                   if(s[j]=='+')s[j]='-';
                   else if(s[j]=='-')s[j]='+';
                }
                cnt++;
            }
        }
        bool imp=false;
        FOR(i,0,n-1)if(s[i]=='-')imp=true;
        if(imp)printf("Case #%d: IMPOSSIBLE\n",cs);
        else printf("Case #%d: %d\n",cs,cnt);
    }
    return 0;
}

