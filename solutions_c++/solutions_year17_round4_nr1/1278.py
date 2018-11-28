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

const int N = 105;
int dp[N][N][N][4];
int a[N];
int n, p;
int xx, yy, zz;

int f(int x, int y, int z, int rm) {
  if (dp[x][y][z][rm] != -1) return dp[x][y][z][rm];
  
  int& res = (dp[x][y][z][rm] = 0);
  
  int val = (rm == 0);
  if (x < xx) {
    res = max(res, val + f(x + 1, y, z, (rm + 1) % p));
  }
  if (y < yy) {
    res = max(res, val + f(x, y + 1, z, (rm + 2) % p));
  }
  if (z < zz) {
    res = max(res, val + f(x, y, z + 1, (rm + 3) % p));
  }
  
  return res;
}

struct Solution {
  void solve() {
    int tt;
    ios::sync_with_stdio(0);
    cin >> tt;
    
    for (int _t = 1; _t <= tt; ++_t) {
      cin >> n >> p;
      
      ::xx = ::yy = ::zz = 0;
      int cnt = 0;
      for (int i = 0; i < n; ++i) {
        int now;
        cin >> now;
        if (now % p == 1) {
          ::xx ++;
        } else if (now % p == 2) {
          ::yy ++;
        } else if (now % p == 3) {
          ::zz ++;
        } else if (now % p == 0) {
          cnt++;
        }
      }
      
      memset(dp, -1, sizeof(dp));
      cout << "Case #" << _t << ": " << cnt + f(0, 0, 0, 0) << endl;
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

