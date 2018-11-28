#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <limits>

using namespace std;

struct pancake {
  int r;
  int h;
  long long rh;

  long long volume_factor() const {
    return ((long long)r) * r + ((long long) 2) * r * h;
  }
};

double solve() {
  int n, k;

  cin >> n >> k;

  vector<pancake> pancakes(n);

  for (int i = 0; i < n; i++) {
    cin >> pancakes[i].r >> pancakes[i].h;
    pancakes[i].rh = ((long long) pancakes[i].r) * pancakes[i].h;
  }

  sort(pancakes.begin(), pancakes.end(),
    [](const pancake& lhs, const pancake& rhs) {
      return lhs.rh < rhs.rh;
    });

  long long max_height_sum = 0;
  const pancake* min_height_pancake = NULL;
  const pancake* max_r_pancake = NULL;

  for (int i = 0; i < k; i++) {
    const pancake& p = pancakes[n - i - 1];
    max_height_sum += p.rh;
    if (min_height_pancake == NULL || min_height_pancake->rh > p.rh) {
      min_height_pancake = &p;
    }

    if (max_r_pancake == NULL || max_r_pancake->r < p.r) {
      max_r_pancake = &p;
    }
  }

  const pancake* max_bottom_pancake = NULL;
  for (int i = 0; i < n - k; i++) {
    const pancake& p = pancakes[i];
    if (p.r > max_r_pancake->r && (max_bottom_pancake == NULL || (max_bottom_pancake->volume_factor() < p.volume_factor()))) {
      max_bottom_pancake = &p;
    }
  }

  double result1 = 2 * ((double) M_PI) * max_height_sum + ((double) M_PI) * max_r_pancake->r * max_r_pancake->r;
  double result2 = 0.0;
  if (max_bottom_pancake != NULL) {
     result2 = 2 * ((double) M_PI) * (max_height_sum - min_height_pancake->rh + max_bottom_pancake->rh) + ((double) M_PI) * max_bottom_pancake->r * max_bottom_pancake->r;
  }

  return result1 > result2 ? result1 : result2;
}

int main() {
  int t;

  cin >> t;

  cout << fixed << setprecision(6);

  for (int a = 0; a < t; a++) {
    double r = solve();
    cout << "Case #" << a + 1 << ": " << r << endl;
  }

  return 0;
}