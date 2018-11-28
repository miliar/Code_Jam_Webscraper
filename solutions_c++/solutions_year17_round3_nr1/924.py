#include <iostream>
#include <cmath>
#include <set>
using namespace std;

struct pancake {
  long long topArea, sideArea;
};

bool cmp(pancake x, pancake y) {
  if (x.topArea == y.topArea) {
    return x.sideArea > y.sideArea;
  }
  return x.topArea > y.topArea;
}

int main() {
  int T, N, K, k;
  long long R, H;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    scanf("%d%d", &N, &K);
    pancake *pancakes = new pancake[N];
    for (int j = 0; j < N; j++) {
      scanf("%lld%lld", &R, &H);
      pancakes[j].topArea = R * R;
      pancakes[j].sideArea = 2 * R * H;
    }
    sort(pancakes, pancakes + N, cmp);
    multiset<long long, greater<long long> > s;
    multiset<long long>::iterator it;
    long long answer = 0;
    for (k = N - K + 1; k < N; k++) {
      s.insert(pancakes[k].sideArea);
    }
    for (int j = N - K; j >= 0; j--) {
      long long sum = pancakes[j].topArea + pancakes[j].sideArea;
      for (it = s.begin(), k = 1; k < K; it++, k++) {
        sum += *it;
      }
      answer = max(answer, sum);
      s.insert(pancakes[j].sideArea);
    }
    printf("Case #%d: %.9f\n", i + 1, (double) 1.0 * M_PI * answer);
  }
}