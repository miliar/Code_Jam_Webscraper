#include <bits/stdc++.h>

#define DG(x) cerr << #x << " is " << x << endl

#define rep(i, begin, end) for (__typeof(end) \
i = (begin) - ((begin) > (end)); i != (end) - \
((begin) > (end)); i += 1 - 2 * ((begin) > (end)))

#define F first
#define S second
#define pb push_back

using namespace std;

typedef long long L;
const int N = 60 * 24 + 10;

int busy[N];
pair <int, int> dp[N][N][2];

pair <int, int> f(int i, int x, int last) {
  if (dp[i][x][last].F != -1) return dp[i][x][last];
  
  pair <int, int>& res = (dp[i][x][last] = make_pair(N, last));
  
  if (i == 60 * 24) {
    if (x != 720) return res = {N, last};
    return res = {0, last};
  }
  
  if (last + 1 == busy[i]) {
    // exchange has to be done
    pair <int, int> to = f(i + 1, !last ? x + 1 : x, !last);
    res = min(res, make_pair(1 + to.F, to.S));
  } else {
    res = min(res, f(i + 1, last ? x + 1 : x, last));
    
    // is it becoming bad
    if (!busy[i]) {
      pair <int, int> to = f(i + 1, !last ? x + 1 : x, !last);
      res = min(res, make_pair(to.F + 1, to.S));
    } 
  }
  
  return res;
}

struct Solution {
  void solve() {
    int tt;
    scanf("%d", &tt);
    
    for (int _t = 1; _t <= tt; ++_t) {
      memset(busy, 0, sizeof(busy));
      
      int n, m;
      scanf("%d %d", &n, &m);
      
      for (int i = 0; i < n; ++i) {
        int c, d;
        scanf("%d %d", &c, &d);
        
        for (int j = c; j < d; ++j) busy[j] = 1;
      }
      
      for (int i = 0; i < m; ++i) {
        int c, d;
        scanf("%d %d", &c, &d);
        
        for (int j = c; j < d; ++j) busy[j] = 2;
      }
      
      for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) dp[i][j][0] = dp[i][j][1] = {-1, -1};
      }
      
      pair <int, int> res1 = f(0, 0, 1);
      pair <int, int> res2 = f(0, 0, 0);
      
      if (res1.S != 1) res1.F++;
      if (res2.S != 0) res2.F++;
      
      assert(res1.F >= 0);
      assert(res2.F >= 0);
      
      printf("Case #%d: %d\n", _t, min(res1.F, res2.F));
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

