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

const int N = 30;

string s;
string res;
int dp[N][10][2];

int f(int i, int last, int eq) {
  assert(i < N && last < 10 && eq < 2);
  if (dp[i][last][eq] != -1) return dp[i][last][eq];
  
  int& res = (dp[i][last][eq] = 0);
  if (i == s.size()) {
    return res = 1;
  }
  
  if (!eq) {
    for (int j = 9; j >= last; --j) {
      res |= f(i + 1, j, eq);
    }
  } else {
    for (int j = s[i] - '0'; j >= last; --j) {
      res |= f(i + 1, j, j == s[i] - '0');
    }
  }
  
  return res;
}

void g(int i, int last, int eq) {
  assert(i < N && last < 10 && eq < 2);
  if (i == s.size()) {
    return;
  }
  
  if (!eq) {
    for (int j = 9; j >= last; --j) {
      if (f(i + 1, j, eq)) {
        res.pb('0' + j);
        g(i + 1, j, eq);
        return;
      }
    }
  } else {
    for (int j = s[i] - '0'; j >= last; --j) {
      if (f(i + 1, j, j == s[i] - '0')) {
        res.pb('0' + j);
        g(i + 1, j, j == s[i] - '0');
        return;
      }
    }
  }
}

struct Solution {
  void solve() {
    int tt; cin >> tt;
    
    for (int _t = 1; _t <= tt; ++_t) {
      cin >> s;
      L n = atoll(s.c_str());
      
      while (s.size() < 25) {
        s = "0" + s;
      }
      memset(dp, -1, sizeof(dp));
      
      res.clear();
      
      g(0, 0, 1);
      for (int i = 1; i < res.size(); ++i) {
        assert(res[i - 1] <= res[i]);
      }
      
      L ans = atoll(res.c_str());
      assert(1 <= ans && ans <= n);
      
      cout << "Case #" << _t << ": " << ans << endl;
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
      
      int tt = 100;
      pn(1, tt);
      
      while (tt--) {
        pn(1, 1000000000000000000LL, 1);
      }
    }
  };
  
  void run() {
    // runs
    Debug db;
    db.gen();
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
  solution.solve();
  return(0);
}

