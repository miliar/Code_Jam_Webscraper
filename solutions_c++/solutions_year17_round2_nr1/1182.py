#include <cstdio>
#include <string>
#include <iostream>
#define min(a, b) (a < b ? a : b)
using namespace std;

long long st[1010], sp[1010];
double ed[1010], edt[1010];
long long d;

void calc(int a, int b) {
  // cannot catch
  if (st[a] >= st[b]) { return; }
  if (ed[a] <= st[b]) { return; }
  if (sp[a] <= sp[b]) { return; }

  double t = double(st[b] - st[a]) / (sp[a] - sp[b]);
  ed[a] = st[a] + t * sp[a];
  if (ed[a] > d) {
    ed[a] = d;
  }
}

int main() {
  int T;
  cin >> T;

  for (int _ = 1; _ <= T; ++_) {
    int n;
    cin >> d >> n;

    double mp = 1e30;

    for (int i = 0; i < n; ++i) {
      scanf("%lld%lld", &st[i], &sp[i]);
      ed[i] = double(d - st[i]) / sp[i];
      mp = min(mp, d / ed[i]);
    }

    // for (int i = 0; i < n; ++i)
    //   for (int j = 0; j < n; ++j) if (i != j) {
    //     calc(i, j);
    //   }

    // double mp = 1e30;
    // for (int i = 0; i < n; ++i) {
    //   if (ed[i] > st[i] && sp[i] > 0) {
    //     double v = ed[i] / (double(ed[i] - st[i]) / sp[i]);
    //     mp = min(mp, v);
    //   }
    // }

    cout << "Case #" << _ << ": ";
    printf("%.6f\n", mp);
  }
  return 0;
}
