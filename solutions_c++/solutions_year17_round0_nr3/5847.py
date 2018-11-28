#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>

using namespace std;

typedef uint64_t cnt;

inline void p(int t, int Lmax, int Lmin) {
  cout << "Case #" << t << ": " << Lmax << " " << Lmin << endl;
}


inline tuple<cnt,cnt> solve(cnt N, cnt K) {
  //cout << "N:" << N << ", K: " << K << endl;
  int64_t i = 0;
  cnt sum = 1;
  while (K > sum) {
    ++i;
    sum += pow(2, i);
  }
  sum -= pow(2, i);
  --i;
  if (K == 1) {
    i = -1;
  }
  //cout << "i: " << i << endl;
  cnt delta = K - sum;
  //cout << "delta: " << delta << endl;
  vector<tuple<cnt ,cnt >> nums;
  nums.push_back(make_tuple(N, 1));

  //cout << N << " " << 1 << endl;

  for (cnt j = 0; j < i + 1; ++j) {
    tuple<cnt ,cnt > x = nums.back();
    nums.pop_back();
    cnt num = get<0>(x);
    cnt freq = get<1>(x);
    cnt high = 0;
    cnt high_freq = 0;
    cnt low_freq = 0;
    if (num % 2 == 0) {
      high = cnt ((num - 1) / 2) + 1;
      high_freq = freq;
      low_freq = freq;
      if (!nums.empty()) {
        x = nums.back();
        nums.pop_back();
        freq = get<1>(x);
        low_freq += 2 * freq;
      }
    } else {
      high =cnt ((num - 1) / 2);
      high_freq = 2 * freq;
      if (!nums.empty()) {
        x = nums.back();
        nums.pop_back();
        freq = get<1>(x);
        high_freq += freq;
        low_freq += freq;
      }
    }
    if (low_freq > 0) {
      //cout << "low: (" << high - 1 << ", " << low_freq << ") ";
      nums.push_back(make_tuple(high - 1, low_freq));
    }
    //cout << "high: (" << high << ", " << high_freq << ")" << endl;
    nums.push_back(make_tuple(high, high_freq));
  }

  tuple<cnt, cnt> x = nums.back();
  nums.pop_back();
  cnt n = get<0>(x);
  cnt freq = get<1>(x);
  if (delta > freq) {
    n -= 1;
  }
  cnt Lmin = cnt((n -1) / 2);
  cnt Lmax = Lmin;
  if (n % 2 == 0) {
    Lmax += 1;
  }

  return make_tuple(Lmax, Lmin);
}

int main() {
  cnt T, N, K;

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> N >> K;
    tuple<cnt ,cnt > r = solve(N, K);
    p(i, get<0>(r), get<1>(r));
  }

  return 0;
}
