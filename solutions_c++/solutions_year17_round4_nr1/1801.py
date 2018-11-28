#include <algorithm>
#include <array>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <iterator>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>
//#define NDEBUG
#include <cassert>

template <class result_t> void print_result(int case_num, result_t result) {
  std::cout << "Case #" << case_num + 1 << ": " << result << std::endl;
}

int main() {
  int num_cases = 0;
  std::cin >> num_cases;
  std::cin.ignore();
  for (int case_num = 0; case_num < num_cases; ++case_num) {
    int N, P;
    std::cin >> N >> P;
    std::vector<int> groups(P, 0);
    for (int i = 0; i < N; ++i) {
      int t;
      std::cin >> t;
      ++groups[t % P];
    }

    int result = 0;
    switch (P) {
    case 2:
      result = groups[0] + (groups[1] + 1) / 2;
      break;
    case 3:
      result = groups[0] + std::min(groups[1], groups[2]) +
               (int)std::ceil((double)(std::max(groups[1], groups[2]) -
                          std::min(groups[1], groups[2])) *
                         1.0 / 3.0);
      break;
    case 4: 
      {
        int ones = std::min(groups[1], groups[3]);
        int phase1 = groups[0] + groups[2]/2 + ones/2;
        int remain = std::max(groups[1],groups[3]) - ones;
        result = phase1;
        if (groups[2] % 2 == 1) {
          result += 1;
          remain -= 2;
          if (remain > 0) {
            result += (int) std::ceil(double(remain)/4.0);
          }
        } else {
          result += (int) std::ceil(double(remain)/4.0);
        }
      }
    default:
      assert(0);
    }
    print_result(case_num,result);
  }
  return 0;
}
