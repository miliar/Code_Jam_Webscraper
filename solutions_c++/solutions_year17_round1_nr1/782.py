#include <bits/stdc++.h>

#define DG(x) cerr << #x << " is " << x << endl

#define rep(i, begin, end) for (__typeof(end) \
i = (begin) - ((begin) > (end)); i != (end) - \
((begin) > (end)); i += 1 - 2 * ((begin) > (end)))

#define F first
#define S second
#define pb push_back

typedef long long L;

using namespace std;

const int N = 26;

int dp[N][N][N][N];
int dff[N][N];
char s[N][N], ans[N][N];
int n, m;

int get(int x1, int y1, int x2, int y2) {
  return dff[x2][y2] - dff[x1][y2] - dff[x2][y1] + dff[x1][y1];
}

int f(int x1, int y1, int x2, int y2) {
  assert(x1 <= x2);
  assert(y1 <= y2);
  
  if (dp[x1][y1][x2][y2] != -1) return dp[x1][y1][x2][y2];
  
  int& res = (dp[x1][y1][x2][y2] = 0);
  
  if (x1 == x2 || y1 == y2) {
    return res = 1;
  }
  
  for (int dx = x1 + 1; dx <= x2; ++dx) {
    for (int dy = y1 + 1; dy <= y2; ++dy) {
      res |= (get(x1, y1, dx, dy) == 1) & f(dx, y1, x2, y2) & f(x1, dy, dx, y2);
      res |= (get(x1, y1, dx, dy) == 1) & f(x1, dy, x2, y2) & f(dx, y1, x2, dy);
    }
  }
  
  return res;
}

void g(int x1, int y1, int x2, int y2) {
  if (x1 == x2 || y1 == y2) {
    return;
  }
  
  for (int dx = x1 + 1; dx <= x2; ++dx) {
    for (int dy = y1 + 1; dy <= y2; ++dy) {
      if ((get(x1, y1, dx, dy) == 1) & f(dx, y1, x2, y2) & f(x1, dy, dx, y2)) {
        char pre = 0;
        for (int i = x1; i < dx; ++i) {
          for (int j = y1; j < dy; ++j) {
            if (s[i][j] != '?') pre = s[i][j];
          }
        }
        assert(pre != 0);
        
        for (int i = x1; i < dx; ++i) {
          for (int j = y1; j < dy; ++j) {
            ans[i][j] = pre;
          }
        }
        g(dx, y1, x2, y2);
        g(x1, dy, dx, y2);
        return;
      }
      if ((get(x1, y1, dx, dy) == 1) & f(x1, dy, x2, y2) & f(dx, y1, x2, dy)) {
        char pre = 0;
        for (int i = x1; i < dx; ++i) {
          for (int j = y1; j < dy; ++j) {
            if (s[i][j] != '?') pre = s[i][j];
          }
        }
        assert(pre != 0);
        
        for (int i = x1; i < dx; ++i) {
          for (int j = y1; j < dy; ++j) {
            ans[i][j] = pre;
          }
        }
        g(x1, dy, x2, y2);
        g(dx, y1, x2, dy);
        return;
      }
    }
  }
  cout << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
  assert(false);
}

struct Solution {
  void solve() {
    int tt;
    scanf("%d", &tt);
    
    for (int _t = 1; _t <= tt; ++_t) {
      scanf("%d %d", &n, &m);
      
      for (int i = 0; i < n; ++i) {
        scanf("%s", s[i]);
      }
      
      memset(dff, 0, sizeof(dff));
      
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
          dff[i + 1][j + 1] = dff[i][j + 1] + dff[i + 1][j] - dff[i][j] + (s[i][j] != '?');
          //cout << i + 1 << ' ' << j + 1 << " $ " << dff[i + 1][j + 1] << endl;
        }
      }
      
      memset(ans, 0, sizeof(ans));
      memset(dp, -1, sizeof(dp));
      g(0, 0, n, m);
      
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
          ans[i][j] != 0;
        }
      }
      
      printf("Case #%d: \n", _t);
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
          printf("%c", ans[i][j]);
        }
        printf("\n");
      }
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

