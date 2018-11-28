#include <algorithm>
#include <iostream>
#include <queue>

int main() {
  long long T;
  std::cin >> T;
  for (long long t = 1; t <= T; ++t) {
    long long n, k;
    std::cin >> n >> k;
    
    long long people = 1;
    long long used = 1;

    while (used < k) {
      used = used * 2 + 1;
      people = people * 2;
    }

    std::cout << "Case #" << t << ": ";
    if (used >= n) {
      
      std::cout << "0 0\n";

    } else {

      long long remain = n - used;

      long long rank = people - (used - k) - 1LL;

      long long gap = (remain / people) + (rank < (remain % people));

      std::cout << ((gap / 2LL) + (gap & 1LL)) << " " << (gap / 2LL) << "\n";

    }

  }
  return 0;
}
