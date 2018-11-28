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

const int maxn = 64;

int n,m;
int w[maxn];
int a[maxn][maxn];
int c[maxn];

int main() {
  //freopen("/home/acrush/CLionProjects/helloworld/input.txt", "r", stdin);
  //freopen("/home/acrush/CLionProjects/helloworld/b1.in", "r", stdin); freopen("/home/acrush/CLionProjects/helloworld/b1.out", "w", stdout);
  freopen("/home/acrush/CLionProjects/helloworld/b2.in", "r", stdin); freopen("/home/acrush/CLionProjects/helloworld/b2.out", "w", stdout);

  // std::ios_base::sync_with_stdio(false);
  int ntestcase;
  cin >> ntestcase;
  for (int case_id = 1; case_id <= ntestcase; ++case_id) {
    printf("Case #%d: ", case_id);

    cin>>n>>m;
    REP(i,n) cin>>w[i];
    REP(i,n) REP(j,m) cin>>a[i][j];
    REP(i,n) sort(a[i],a[i]+m);
    memset(c,0,sizeof(c));
    int ret=0;
    for (int e=1;e<=1000000;e++) {
      bool ok=true;
      bool bad=false;
      REP(i,n) {
        int z=e*w[i];
        int l=(z*9+9)/10;
        for (;c[i]<m && a[i][c[i]]<l;++c[i]);
        if (c[i]>=m) { bad=true; break; }
        int r=(z*11)/10;
        if (a[i][c[i]]>r) ok=false;
      }
      if (bad) break;
      if (!ok) continue;
      ++ret;
      REP(i,n) ++c[i];
      --e;
    }
    printf("%d\n",ret);
  }

  return 0;
}