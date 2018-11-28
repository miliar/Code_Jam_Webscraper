#include<bits/stdtr1c++.h>
using namespace std;

typedef long long ll;

ll T, N, P;
vector<ll> R;
vector<vector<ll> > Q;

struct ra {
  ll n;
  ll d;
};

bool done(const vector<int>& v) {
  for (int i = 0; i < N; ++i) {
    if (v[i] >= P) return true;
  }
  return false;
}

pair<int, int> calc(int a, int d) {
  int l = (a * 10 + 10) / 11;
  int u = (a * 10) / 9;
  l = (l + d - 1) / d;
  u = u / d;
  //cout << a << " " << d << " : " << l << " " << u << endl;
  return pair<int, int>(l, u);
}

bool common(vector<int>& v) {
  int l = -1;
  int u = numeric_limits<int>::max();
  for (int i = 0; i < N; ++i) {
    pair<int, int> p;
    while (true) {
      if (v[i] >= P) return false;
      p = calc(Q[i][v[i]], R[i]);
      if (p.second < p.first) {
        v[i]++;
      } else {
        break;
      }
    }
    l = max(l, p.first);
    u = min(u, p.second);
  }
  return l <= u;
}

bool lessthan(ra a, ra b) {
  ll aa = a.n * b.d;
  ll bb = b.n * a.d;
  return aa < bb;
}

void inc(vector<int>& v) {
  int m = 0;
  ra mm;
  mm.n = Q[0][v[0]];
  mm.d = R[0];
  for (int i = 1; i < N; ++i) {
    ra x; x.n = Q[i][v[i]]; x.d = R[i];
    if (lessthan(x, mm)) {
      mm = x;
      m = i;
    }
  }
  v[m]++;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> N >> P;
    R.resize(N);
    for (int i = 0; i < N; ++i) {
      cin >> R[i];
    }
    Q = vector<vector<ll> >(N, vector<ll>(P));
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < P; ++j) {
        cin >> Q[i][j];
      }
      sort(Q[i].begin(), Q[i].end());
    }
    vector<int> idx = vector<int>(N, 0);
    int res = 0;
    while (!done(idx)) {
      if (common(idx)) {
        res++;
        for (int i = 0; i < N; ++i) {
          idx[i]++;
        }
      } else {
        if (!done(idx)) inc(idx);
      }
    }
    cout << res << endl;
  }

  return 0;
}
