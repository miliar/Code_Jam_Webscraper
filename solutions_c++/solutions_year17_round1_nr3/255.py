#include <bits/stdc++.h>

using namespace std;

struct node {
  int dist, hd, ak, steps;
};

int min_dist[105][105][105];

int bfs(int hd, int ad, int hk, int ak, int b, int d, int steps) {
  memset(min_dist, 0x3f3f3f3f, sizeof min_dist);

  queue<node> q;
  min_dist[hd][ak][0] = 0;
  q.push(node {0, hd, ak, 0});

  while (q.size()) {
    auto next = q.front();
    q.pop();

    if (next.steps == steps - 1) {
      return next.dist + 1;
    }

    // cure
    node cure {next.dist + 1, hd - next.ak, next.ak, next.steps};

    if (cure.hd > 0 && min_dist[cure.hd][cure.ak][cure.steps] > cure.dist) {
      min_dist[cure.hd][cure.ak][cure.steps] = cure.dist;
      q.push(cure);
    }

    // attack || buf
    node attack {next.dist + 1, next.hd - next.ak, next.ak, next.steps + 1};
    if (attack.hd > 0 && min_dist[attack.hd][attack.ak][attack.steps] > attack.dist) {
      min_dist[attack.hd][attack.ak][attack.steps] = attack.dist;
      q.push(attack);
    }

    // debuf
    node debuff {next.dist + 1, next.hd - max(0, next.ak - d), max(0, next.ak - d), next.steps};
    if (debuff.hd > 0 && min_dist[debuff.hd][debuff.ak][debuff.steps] > debuff.dist) {
      min_dist[debuff.hd][debuff.ak][debuff.steps] = debuff.dist;
      q.push(debuff);
    }
  }

  return -1;
}

int main() {

  int tc;
  cin >> tc;

  for (int t = 1; t <= tc; t++) {
    int hd, ad, hk, ak, b, d;
    cin >> hd >> ad >> hk >> ak >> b >> d;

    int best_steps = 100;

    for (int k = 0; k <= 100; k++) {
      best_steps = min(best_steps, k + (hk + ad + k*b - 1) / (ad + k*b));
    }

    int ans = bfs(hd, ad, hk, ak, b, d, best_steps);

    if (ans != -1) {
      cout << "Case #" << t << ": " << ans << endl;
    } else {
      cout << "Case #" << t << ": IMPOSSIBLE\n";
    }
  }

  return 0;
}
