#include <cstdio>
#include <map>
using namespace std;
#define MAXN 1000

int main() {
  int c = 0, n_cases;
  int n_horse, dest;
  int p;
  double q;
  map<int, double> horse;
  map<int, double>::reverse_iterator bottle_neck, it;
  scanf("%d", &n_cases);
  while (c < n_cases) {
    horse.clear();
    printf("Case #%d: ", ++c);
    scanf("%d %d", &dest, &n_horse);
    for (int i = 0; i < n_horse; ++i) {
      scanf("%d %lf", &p, &q);
      horse[p] = q;
    }
    it = bottle_neck = horse.rbegin();
    for (++it; it != horse.rend(); ++it) {
      double cost_n = (dest - it->first) / it->second;
      double cost_b = (dest - bottle_neck->first) / bottle_neck->second;
      if (cost_n > cost_b) {
        bottle_neck = it;
      }
    }
    printf("%.6lf\n", dest * bottle_neck->second / (dest - bottle_neck->first));
  }
  return 0;
}
