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

const int N = 55;
const long double eps = 1e-11;

long double p[N];

struct Solution {
  void solve() {
    int tt;
    cin >> tt;
    
    for (int _t = 1; _t <= tt; ++_t) {
      int n, k;
      cin >> n >> k;
      
      long double u;
      cin >> u;
      //DG(u);
      for (int i = 0; i < n; ++i) {
        cin >> p[i];
        //DG(p[i]);
      }
      
      long double lo = 0, hi = 1;
      
      while (hi - lo > eps) {
        long double mid = (lo + hi) / 2;
        
        // all values >= mid
        long double now = 0;
        for (int i = 0; i < n; ++i) {
          if (p[i] > mid + eps) continue;
          now += mid - p[i];
        }
        
        if (u > now + eps) {
          lo = mid;
        } else {
          hi = mid;
        }
      }
      
      long double res = 1;
      for (int i = 0; i < n; ++i) {
        res *= max(p[i], lo);
      }
      
      printf("Case #%d: %.17lf\n", _t, res);
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

