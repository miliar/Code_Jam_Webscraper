#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<double> vd;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<pii> vii;
typedef vector<vl> vvl;
typedef vector<vd> vvd;

#define VAR(a, b) __typeof(b) a=(b)
#define DEBUG(x) cerr << #x " = " << (x) << endl
#define CLR(a, val) memset(a, val, sizeof(a))
#define REP(i, n) for (int i = 0, _n = (n); i < _n; i++)
#define FOR(i, a, b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i, a, b) for (int i = (a), _b = (b); i >= _b; i--)
#define PB push_back
#define MP make_pair
#define MT make_tuple

template<class T1, class T2>
ostream& operator << (ostream &o, const pair<T1, T2> &p) {
  return o << "(" << p.first << ", " << p.second << ")";
}

template<class T1, class T2, class T3>
ostream& operator << (ostream &o, const tuple<T1, T2, T3> &t) {
  return o << "(" << get<0>(t) << ", " << get<1>(t) << ", " << get<2>(t) << ")";
}

template<class T1, class T2, class T3, class T4>
ostream& operator << (ostream &o, const tuple<T1, T2, T3, T4> &t) {
  return o << "(" << get<0>(t) << ", " << get<1>(t) << ", " << get<2>(t) << ", " << get<3>(t) << ")";
}

template<class T>
ostream& operator << (ostream &o, const vector<T> &v) {
  o << '{';
  for (auto it = v.begin(); it != v.end(); ++it)
    o << (it == v.begin() ? "" : ", ") << *it;
  return o << '}';
}

template<class T>
ostream& operator<<(ostream &o, const set<T> &s) {
  o << '{';
  for (auto it = s.begin(); it != s.end(); ++it)
    o << (it == s.begin() ? "" : ", ") << *it;
  return o << '}';
}

template<class K, class V>
ostream& operator<<(ostream &o, const map<K, V> &m) {
  o << '{';
  for (auto it = m.begin(); it != m.end(); ++it)
    o << (it == m.begin() ? "" : ", ") << it->first << ": " << it->second;
  return o << '}';
}

const int INF = 500000;

class runner {
public:
  int Ac, Aj;
  int dp[2][2][1500][750];
  vi C, D, J, K;
  vi S;

  string res;

  void read() {
    cin >> Ac >> Aj;
    C = D = vi(Ac);
    REP(i, Ac)
      cin >> C[i] >> D[i];
    J = K = vi(Aj);
    REP(i, Aj)
      cin >> J[i] >> K[i];
  }

  int f(int s, int c, int m, int t) {
    auto &res = dp[s][c][m][t];
    if (res != -1)
      return res;
    if (t > 720)
      return res = INF;
    if (m == 1440) {
      if (t == 720)
        return res = (c != s);
      return res = INF;
    }

    m++;
    if (c == 0)
      t++;

    if (S[m] == c) {
      res = f(s, 1-c, m, t) + 1;
    } else if (S[m] == 1-c) {
      res = f(s, c, m, t);
    } else {
      int res1 = f(s, c, m, t);
      int res2 = f(s, 1-c, m, t) + 1;
      res = min(res1, res2);
    }

    return res;
  }

  void run(void) {
    S = vi(1500, -1);
    REP(i, Ac)
      FOR(j, C[i], D[i]-1)
        S[j] = 0;
    REP(i, Aj)
      FOR(j, J[i], K[i]-1)
        S[j] = 1;

    CLR(dp, -1);
    int res;
    if (S[0] == -1)
      res = min(f(0, 0, 0, 0), f(1, 1, 0, 0));
    else if (S[0] == 1)
      res = f(0, 0, 0, 0);
    else
      res = f(1, 1, 0, 0);

    ostringstream oss;
    oss << res;
    this->res = oss.str();
  }

  static void *run_helper(void *context) {
    ((runner *)context)->run();
    return 0;
  }
};

int main(int argc, char *argv[]) {
  int T = 0;
  cin >> T; //cin.getline(NULL, 0);

  int from = 0, to = T-1;
  if (argc == 3) {
    from = atoi(argv[1])-1;
    to = min(to, atoi(argv[2])-1);
  }

  vector<runner> runners(T);
  for (int t = 0; t < T; t++)
    runners[t].read();

  #ifdef _MT_
    pthread_attr_t attrs;
    pthread_attr_init(&attrs);
    pthread_attr_setstacksize(&attrs, 256*1024*1024);

    vector<pthread_t> threads(T);
    for (int t = from; t <= to; t++)
      pthread_create(&threads[t], &attrs, &runner::run_helper, &runners[t]);
    for (int t = from; t <= to; t++)
      pthread_join(threads[t], NULL);
  #else
    for (int t = from; t <= to; t++)
      runners[t].run();
  #endif

  for (int t = from; t <= to; t++)
    cout << "Case #" << (t + 1) << ": " << runners[t].res << endl;

  return 0;
}
