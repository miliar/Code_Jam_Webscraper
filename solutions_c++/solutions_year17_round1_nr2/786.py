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

const int N = 1005;
int req[N], n, p, adj[N][N];
pair <int, int> pa[N][N];

int cel(int x, int y) {
  assert(y != 0);
  return (x + y - 1) / y;
}

int flor(int x, int y) {
  return x / y;
}

bool bad(vector <int> & ptr) {
  for (int i = 0; i < n; ++i) {
    if (ptr[i] == p) return 1; 
  }
  return 0;
}

bool good(vector <int> &ptr) {
  pair <int, int> rag = {0, N * N * N};
  
  for (int i = 0; i < n; ++i) {
    rag.first = max(pa[i][ptr[i]].first, rag.first);
    rag.second = min(pa[i][ptr[i]].second, rag.second);
  }
  
  return rag.first <= rag.second;
}

void decAll(vector <int> &ptr) {
  for (int i = 0; i < n; ++i) {
    ptr[i]++;
  }
}

void decOne(vector <int> &ptr) {
  int mn = N * N * N, id = -1;
  for (int i = 0; i < n; ++i) {
    if (mn > pa[i][ptr[i]].second) {
      mn = pa[i][ptr[i]].second;
      id = i;
    }
  }
  
  assert(id != -1);
  ptr[id]++;
}

struct Solution {
  void solve() {
    int tt;
    scanf("%d", &tt);
    
    for (int _t = 1; _t <= tt; ++_t) {
      scanf("%d %d", &n, &p);
      
      for (int i = 0; i < n; ++i) {
        scanf("%d", req + i);
      }
      
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
          scanf("%d", &adj[i][j]);
          pa[i][j] = {cel(10 * adj[i][j], 11 * req[i]), flor(10 * adj[i][j], 9 * req[i])};
        }
      }
      
      for (int i = 0; i < n; ++i) {
        sort(pa[i], pa[i] + p, [] (const pair <int, int> A, const pair <int, int> B) {
          if (A.second != B.second) {
            return A.second < B.second;
          }
          return A.first < B.first;
        });
      }
      
      int res = 0;
      
      vector <int> ptr(n, 0);
      while (!bad(ptr)) {
        if (good(ptr)) {
          res++;
          decAll(ptr);
        } else {
          decOne(ptr);
        }
      }
      
      printf("Case #%d: %d\n", _t, res);
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

