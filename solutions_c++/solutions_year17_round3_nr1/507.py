#include <bits/stdc++.h>

#define DG(x) cerr << #x << " is " << x << endl

#define rep(i, begin, end) for (__typeof(end) \
i = (begin) - ((begin) > (end)); i != (end) - \
((begin) > (end)); i += 1 - 2 * ((begin) > (end)))

#define F first
#define S second
#define pb push_back

typedef long long L;

const long double PI = 4 * atan(1);
const long double INF = 10000000000000000LL;
const int N = 1005;

using namespace std;

pair <int, int> cakes[N];
long double dp[N][N][2];

long double f(int i, int j, int beg) {
  assert(i < N && j < N);
  if (dp[i][j][beg] != (long double)-1) return dp[i][j][beg];
  
  long double& res = (dp[i][j][beg] = 0);
  
  if (j == 0) {
    return res = 0;
  }
  
  if (i == 0) {
    return res = -INF;
  }
  
  // dont select
  res = max(res, f(i - 1, j, beg));
  res = max(res, (!beg ? -PI * cakes[i - 1].F * cakes[i - 1].F : 0) + PI * cakes[i - 1].F * cakes[i - 1].F + 2 * PI * cakes[i - 1].F * cakes[i - 1].S + f(i - 1, j - 1, 0));
  
  return res;
}

struct Solution {
  void solve() {
    int tt;
    scanf("%d", &tt);
    
    for (int _t = 1; _t <= tt; ++_t) {
      int n, k;
      scanf("%d %d", &n, &k);
      
      for (int i = 0; i < n; ++i) {
        scanf("%d %d", &cakes[i].F, &cakes[i].S);
      }
      
      sort(cakes, cakes + n);
      
      for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= n; ++j) {
          dp[i][j][0] = dp[i][j][1] = -1;
        }
      }
      
      printf("Case #%d: %.17lf\n", _t, f(n, k, 1));
    }
  }
  
  struct Debug {
    L random(L l, L r) {
      return l + (rand() * 1./RAND_MAX) * (r - l);
    }
  
    void pn(L lo, L hi, bool rnd = 0) {
      if (rnd) {
        printf("%lld\n", random(lo, hi));
      } else {
        printf("%lld\n", hi);
      }
    } 
  
    void par(L lo, L hi, L cnt = 1, bool rnd = 0) {
      for (int i = 0; i < cnt; ++i) {
        printf("%lld%c", rnd ? random(lo, hi) : hi, (i == cnt - 1) ? '\n': ' ');
      }
    }
  
    void gen() {
      freopen("IN.txt", "w", stdout);
      // input format
    }
  };
  
  void run() {
    // runs
    Debug db;
    //db.gen();
    freopen("IN.txt", "r", stdin);
    freopen("OUT.txt", "w", stdout);
    
    clock_t b = clock();
    solve();
    clock_t e = clock();
    
    cerr << "Time Taken for random case : " << (e - 1.0 * b) / CLOCKS_PER_SEC << endl;
  }
  
};

int main()
{
  Solution solution;
  solution.run();
  return(0);
}

