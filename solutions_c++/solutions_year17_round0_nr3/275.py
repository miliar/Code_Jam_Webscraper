#include <bits/stdc++.h>

using namespace std;

#define PB push_back
#define MP make_pair
#define LL long long
#define int LL
#define st first
#define nd second
#define VI vector<int>
#define LD long double
#define PII pair<int,int>
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())

template <class C> void mini(C& a4, C b4) { a4 = min(a4, b4); }
template <class C> void maxi(C& a4, C b4) { a4 = max(a4, b4); }

template <class TH> void _dbg(const char *sdbg, TH h) { cerr << sdbg << "=" << h << "\n"; }
template <class TH, class ... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while (*sdbg != ',') cerr << *sdbg++; cerr << "=" << h << ","; _dbg(sdbg+1, a...);
}

template <class T> ostream &operator<<(ostream &os, vector<T> V) {
  os << "["; for (auto vv : V) os << vv << ","; return os << "]";
}

template <class L, class R> ostream &operator<<(ostream &os, pair<L,R> P) {
  return os << "(" << P.st << "," << P.nd << ")";
}


#ifdef LOCAL
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) (__VA_ARGS__)
#define cerr if(0)cout
#endif


struct Testcase {
  void run(int id) {
    LL N, K;
    cin >> N >> K;

    map<LL, LL> intvCounts;
    intvCounts[N] = 1;

    LL lastLen = N;
    while (K > 0) {
      auto I = *intvCounts.rbegin();
      intvCounts.erase(prev(intvCounts.end()));

      lastLen = I.first;
      LL count = I.second;

      intvCounts[lastLen / 2] += count;
      intvCounts[(lastLen - 1) / 2] += count;
      K -= count;
    }

    cout << "Case #" << id << ": " << lastLen / 2 << " " << (lastLen - 1) / 2 << "\n";
  }
};


int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout << fixed << setprecision(11);
  cerr << fixed << setprecision(6);

  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    Testcase tc;
    tc.run(i + 1);
  }
}
