#include <cassert>
#include <cctype>
//#include <cinttypes>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%ld",&n)
#define sll(n)                      scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ssp(n)                      scanf("%[^\n]%*c",n)
#define prt(x)                      printf("%d\n",x);
#define plt(x)                      printf("%lld\n",x);

#define INF                         0x3f3f3f3f
#define EPS                         1e-12

#define bitcount                    __builtin_popcount
#define bitcountl                   __builtin_popcountl
#define bitcountll                  __builtin_popcountll
#define gcd                         __gcd

#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define rall(a)                     a.rbegin(),a.rend()

#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                   memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define dot(a,b)                    ((conj(a)*(b)).X)
#define cross(a,b)                  ((conj(a)*(b)).imag())
#define normalize(v)                ((v)/length(v))
#define rotate(p,about,theta)       ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b)               (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)                ( (n >> b) & 1)
#define strjoin( x, y )              x ## y
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())
#define MOD
#define ADD(X,Y)                     ((X) = ((X) + (Y)%MOD) % MOD)

char *strrev(char *str)
{
  char *p1, *p2;
  if (! str || ! *str)
    return str;
  for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2)
  {
    *p1 ^= *p2;
    *p2 ^= *p1;
    *p1 ^= *p2;
  }
  return str;
}

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef stringstream ss;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<vector<int> > vvi;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;


#ifdef DEBUG
      #define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
      #define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
      #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
      #define trace4(a,b,c,d)     cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<endl;
      #define trace5(a,b,c,d,e)   cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<endl;
      #define trace6(a,b,c,d,e,f) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<" | "#f" = "<<f<<endl;
#else
      #define trace1(x)           
      #define trace2(x,y)         
      #define trace3(x,y,z)       
      #define trace4(a,b,c,d)     
      #define trace5(a,b,c,d,e)   
      #define trace6(a,b,c,d,e,f) 
#endif

vi arr,l,r;
int n;

void calc(int i)
{
  int x=i-1, y=i+1;
  while(!arr[x] && x>=0)
    --x;
  while(!arr[y] && x<=n+1)
    ++y;

  l[i]=i-x-1;
  r[i]=y-i-1;
}

int main()
{

#ifdef SMALL
  freopen("C-small-1-attempt0.in","rt",stdin);
  freopen("C-small-1.out","wt",stdout);
#endif
#ifdef LARGE
  freopen("C-large.in","rt",stdin);
  freopen("C-large.out","wt",stdout);
#endif

  int t,k,x,y,z,pos,mx1,mx2,val1,val2;
  s(t);
  forall(x,0,t)
  {
    s(n);
    s(k);
    arr.clear();
    arr.resize(n+2,0);

    arr[0]=arr[n+1]=1;
    
    forall(v,0,k)
    {
     l.clear();
     l.resize(n+2,0);
     r.clear();
     r.resize(n+2,0);

     forall(i,1,n+1)
     {
      if(!arr[i])
        calc(i);
    }
    pos=1;
    while(arr[pos])
      ++pos;
    mx1=miN(l[pos],r[pos]);
    mx2=maX(l[pos],r[pos]);
    forall(i,pos+1,n+1)
    {
      if(!arr[i])
      {
        val1=miN(l[i],r[i]);
        val2=maX(l[i],r[i]);
        if(val1 > mx1)
        {
          trace6(pos,i,val1,mx1,val2,mx2);
          pos=i;
          mx1=val1;
          mx2=val2;
        }
        else if(val1==mx1 && val2 > mx2)
        {
          trace6(pos,i,val1,mx1,val2,mx2);
          pos=i;
          mx2=val2;
        }
      }
    }
    
    arr[pos]=1;
    trace2(pos,mx1);
  }
  calc(pos);
  y=maX(l[pos], r[pos]);
  z=miN(l[pos], r[pos]);

  printf("Case #%d: %d %d\n",x+1,y,z);
}
return 0;
}