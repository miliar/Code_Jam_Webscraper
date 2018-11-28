#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <vector>
using namespace std;

double const kPi = acos(-1.0);

struct Pancake {
  uint64_t m_radius = 0;
  uint64_t m_height = 0;
};

double Solve(int n, int k, vector<Pancake> pancakes) {
  assert(k <= n);
  assert(k >= 1);

  sort(pancakes.begin(), pancakes.end(),
       [&](Pancake const &lhs, Pancake const &rhs) {
         return lhs.m_radius < rhs.m_radius;
       });

  uint64_t best = 0;
  for (int i = k - 1; i < n; ++i) {
    vector<uint64_t> products;
    for (int j = 0; j < i; ++j)
      products.push_back(pancakes[j].m_radius * pancakes[j].m_height);
    sort(products.rbegin(), products.rend());
    products.resize(k - 1);

    uint64_t result = 0;
    for (uint64_t p : products)
      result += 2 * p;
    result += 2 * pancakes[i].m_radius * pancakes[i].m_height;
    result += pancakes[i].m_radius * pancakes[i].m_radius;

    if (result > best)
      best = result;
  }

  return kPi * best;
}

int main() {
  int numTests;
  scanf("%d", &numTests);
  for (int testNum = 1; testNum <= numTests; ++testNum) {
    int n, k;
    scanf("%d%d", &n, &k);
    vector<Pancake> pancakes(n);
    for (int i = 0; i < n; ++i) {
      int r, h;
      scanf("%d%d", &r, &h);
      pancakes[i].m_radius = r;
      pancakes[i].m_height = h;
    }

    printf("Case #%d: %.7lf\n", testNum, Solve(n, k, pancakes));
  }
  return 0;
}
