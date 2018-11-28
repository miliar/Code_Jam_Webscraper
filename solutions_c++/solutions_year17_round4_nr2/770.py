#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1000 + 10;
const int INF = (int)(1e9);

typedef vector<int> VI;
typedef vector<VI> VVI;

bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
  for (int j = 0; j < w[i].size(); j++) {
    if (w[i][j] && !seen[j]) {
      seen[j] = true;
      if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
        mr[i] = j;
        mc[j] = i;
        return true;
      }
    }
  }
  return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
  mr = VI(w.size(), -1);
  mc = VI(w[0].size(), -1);

  int ct = 0;
  for (int i = 0; i < w.size(); i++) {
    VI seen(w[0].size());
    if (FindMatch(i, w, mr, mc, seen)) ct++;
  }
  return ct;
}

int n, c, m;
int ticket_own[MAXN];
int p[MAXN], b[MAXN];

void solve_small() {
    for(int i = 1; i <= c; ++i) ticket_own[i] = 0;
    for(int i = 1; i <= m; ++i) ticket_own[b[i]]++;
    if ((ticket_own[1] == 0) || (ticket_own[2] == 0)) {
        cout << m << " " << 0 << "\n";
        return;
    }
    int cnt_1 = 0, cnt_2 = 0;
    for(int i = 1; i <= m; ++i) {
        if (b[i] == 1) cnt_1 += (p[i] == 1);
        if (b[i] == 2) cnt_2 += (p[i] == 1);
    }
    int t_1 = min(cnt_1, ticket_own[2] - cnt_2), t_2 = min(cnt_2, ticket_own[1] - cnt_1);
    int n_rides = cnt_1 + cnt_2;
    VVI w(m + 1, VI(m + 1, 0));
    for(int i = 1; i <= m; ++i)
        for(int j = 1; j <= m; ++j)
            if ((b[i] == 1) && (b[j] == 2) && (p[i] != 1) && (p[j] != 1))
                if (p[i] != p[j])
                    w[i][j] = 1;
    VI mr(m + 1, 0), mc(m + 1, 0);
    int x = BipartiteMatching(w, mr, mc);
    int L = ticket_own[1] - cnt_1 - t_2, R = ticket_own[2] - cnt_2 - t_1;
    n_rides += max(L, R);
    int n_promote = max(0, min(L, R) - x);
    cout << n_rides << " " << n_promote << "\n";
}

void run() {
    cin >> n >> c >> m;
    for(int i = 1; i <= m; ++i) {
        cin >> p[i] >> b[i];
    }

    if (c == 2) {
        solve_small();
    }
    else {
        cout << "-1 -1\n";
    }
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int ntests = 1;
    cin >> ntests;
    for(int tc = 1; tc <= ntests; ++tc) {
        cout << "Case #" << tc << ": ";
        run();
    }
}
