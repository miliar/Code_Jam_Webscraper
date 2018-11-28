#include <bits/stdc++.h>
using namespace std;
typedef long long Long;

const int N = 24 * 60;
const int OO = 1e7;

bool active[N][2];

int memo[N][N][2][2];
int vis[N][N][2][2];
int vis_id;

int Solve(int minute, int first_done, bool first_last, bool first_beg) {
  if (first_done > N / 2 || minute - first_done > N / 2) return OO;

  if (minute == N) {
    return ((first_done == N / 2) ? (first_last != first_beg) : OO);
  }

  int& res = memo[minute][first_done][first_last][first_beg];
  int& last_vis = vis[minute][first_done][first_last][first_beg];
  if (last_vis == vis_id) return res;

  last_vis = vis_id;

  res = OO;

  if (!active[minute][0]) {
    if (minute == 0) {
      first_beg = first_last = true;
    }
    res = min(res,
      Solve(minute + 1, first_done + 1, true, first_beg) + !first_last);
  }
  if (!active[minute][1]) {
    if (minute == 0) {
      first_beg = first_last = false;
    }
    res = min(res,
      Solve(minute + 1, first_done, false, first_beg) + first_last);
  }

  return res;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

#ifdef Local
  freopen("test.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif

  int t;
  cin >> t;

  for (int cs = 1; cs <= t; ++cs) {
    cout << "Case #" << cs << ": ";
    memset(active, false, sizeof active);

    ++vis_id;

    int ac[2];
    cin >> ac[0] >> ac[1];

    for (int p = 0; p < 2; ++p) {
      while (ac[p]--) {
        int start, end;
        cin >> start >> end;
        for (int i = start; i < end; ++i) {
          active[i][p] = true;
        }
      }
    }
    cout << Solve(0, 0, true, true) << '\n';
  }
}
