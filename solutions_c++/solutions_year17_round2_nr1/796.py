#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 1000 + 100;
typedef pair<double, double> pdd;


int N;
double D;
pdd horses[MAXN];

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1;t <= T;++t) {
    scanf("%lf %d", &D, &N);

    for (int i = 0;i < N;++i) {
      scanf("%lf %lf", &horses[i].first, &horses[i].second);
    }

    sort(horses, horses + N);

    pdd horse = horses[N - 1];

    for (int i = N - 2;i >= 0;--i) {
      if ((D - horses[i].first) / horses[i].second > (D - horse.first) / horse.second)
        horse = horses[i];
    }

    double time = (D - horse.first) / horse.second;

    double speed = D / time;

    printf("Case #%d: %lf\n", t, speed);
  }
  return 0;
}
