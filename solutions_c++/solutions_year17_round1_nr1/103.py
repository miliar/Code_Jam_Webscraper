#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <functional>
#include <utility>
#include <set>
#include <map>
#include <complex>
#include <queue>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string.h>
#include <unordered_set>
#include <unordered_map>
#include <mmintrin.h>
#include <xmmintrin.h>
#include <emmintrin.h>
#include <cassert>

#ifndef ONLINE_JUDGE
#include <gperftools/profiler.h>
#endif

using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned short ushort;
typedef unsigned char uchar;
typedef pair<int, int> ipair;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
#define SIZE(A) ((int)(A.size()))
#define LENGTH(A) ((int)(A.length()))
#define MP(A, B) make_pair(A,B)
const double pi = acos(-1.0);
#define FOR(i, a, b) for(int i=(a);i<(b);++i)
#define REP(i, a) for(int i=0;i<(a);++i)
#define ALL(a) (a).begin(),(a).end()

template<class T>
T sqr(const T& x) { return x * x; }

template<class T>
T lowbit(const T& x) { return (x ^ (x - 1)) & x; }

template<class T>
int countbit(const T& n) { return (n == 0) ? 0 : (1 + countbit(n & (n - 1))); }

template<class T>
void ckmin(T& a, const T& b) { if (b < a) a = b; }

template<class T>
void ckmax(T& a, const T& b) { if (b > a) a = b; }

const int maxsize=32;

char s[maxsize][maxsize];
int f[maxsize][maxsize][maxsize][maxsize];

int solve(int x1,int y1,int x2,int y2) {
  int& ret=f[x1][y1][x2][y2];
  if (ret>=0) return ret;
  int cnt=0;
  char w=0;
  FOR(x,x1,x2+1) FOR(y,y1,y2+1) if (s[x][y]!='?') { if (w==0) w=s[x][y],cnt=1; if (w!=s[x][y]) ++cnt; }
  if (cnt==0) return ret=0;
  if (cnt==1) return ret=1;
  FOR(x,x1,x2) if (solve(x1,y1,x,y2) && solve(x+1,y1,x2,y2)) return ret=1;
  FOR(y,y1,y2) if (solve(x1,y1,x2,y) && solve(x1,y+1,x2,y2)) return ret=1;
  return ret=0;
}
void construct(int x1,int y1,int x2,int y2) {
  int cnt=0;
  char w=0;
  FOR(x,x1,x2+1) FOR(y,y1,y2+1) if (s[x][y]!='?') { if (w==0) w=s[x][y],cnt=1; if (w!=s[x][y]) ++cnt; }
  if (cnt==0) return;
  if (cnt==1) {
    FOR(x,x1,x2+1) FOR(y,y1,y2+1) s[x][y]=w;
    return;
  }
  FOR(x,x1,x2) if (solve(x1,y1,x,y2) && solve(x+1,y1,x2,y2)) { construct(x1,y1,x,y2); construct(x+1,y1,x2,y2); return; }
  FOR(y,y1,y2) if (solve(x1,y1,x2,y) && solve(x1,y+1,x2,y2)) { construct(x1,y1,x2,y); construct(x1,y+1,x2,y2); return; }
  assert(0);
}
int main() {
  //freopen("/home/acrush/CLionProjects/helloworld/input.txt", "r", stdin);
  //freopen("/home/acrush/CLionProjects/helloworld/a1.in", "r", stdin); freopen("/home/acrush/CLionProjects/helloworld/a1.out", "w", stdout);
  freopen("/home/acrush/CLionProjects/helloworld/a2.in", "r", stdin); freopen("/home/acrush/CLionProjects/helloworld/a2.out", "w", stdout);

  // std::ios_base::sync_with_stdio(false);
  int ntestcase;
  cin >> ntestcase;
  for (int case_id = 1; case_id <= ntestcase; ++case_id) {
    printf("Case #%d:\n", case_id);
    memset(s,0,sizeof(s));
    int n,m;
    memset(f,255,sizeof(f));
    cin>>n>>m;
    REP(i,n) cin>>s[i];
    if (!solve(0,0,n-1,m-1)) {
      printf("BAD\n");
      exit(0);
    }

    construct(0,0,n-1,m-1);
    REP(i,n) printf("%s\n",s[i]);
  }

  return 0;
}