#include <iostream>

using namespace std;

long long FindSubRoot(long long n, long long k) {
  k -= 1ll;

  long long worst_case = n;
  long long power_2 = 1ll;
  while (worst_case) {
    if (k >= power_2) {
      k -= power_2;
      worst_case = (worst_case - 1) / 2;
      power_2 += power_2;
      continue;
    }

    long long layer_sum = n - power_2 + 1;
    long long best_case_num = max(0ll, layer_sum - worst_case * power_2);

    // cerr << k << " " << worst_case << " " << power_2 << " " << layer_sum << " " << best_case_num << "\n";

    if (k < best_case_num) {
      return worst_case + 1;
    } else {
      return worst_case;
    }
  }

  return 1ll;
}

void Solve(int case_id) {
  long long n, k; cin >> n >> k;

  long long x = FindSubRoot(n, k);
  long long a = x / 2;
  long long b = (x - 1) / 2;
  cout << "Case #" << case_id << ": " << a << " " << b << "\n";
}

int main() {
  int cases_num; cin >> cases_num;

  for (int i = 0; i < cases_num; ++i) {
    Solve(i + 1);
  }

  return 0;
}
