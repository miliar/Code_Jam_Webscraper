#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<iterator>

struct solver_2017_q_a {
  std::string run(std::string S, int K) {
    std::string impossible = "IMPOSSIBLE";
    unsigned char plus = '+', minus = '-';
    long long num_checking, num;
    int count = 0;
    int size = S.size();
    std::string S2 = S;
    std::stringstream ss;

    for (int i = 0; i < size - K + 1; ++i) {
      if (S2[i] == minus) {
        // flip
        ++count;
        for (int j = 0; j < K; ++j) {
          if (S2[i + j] == plus) {
            S2[i + j] = minus;
          } else {
            S2[i + j] = plus;
          }
        }
      }
      // std::cerr << S2 << std::endl;
    }
    for (int i = size - K + 1; i < size; ++i) {
      if (S2[i] == minus) {
        return impossible;
      }
    }
    ss << count;

    return ss.str();;
  }

};

int main(void) {
  solver_2017_q_a solver;

  int T, K;
  std::string S;

  std::cin >> T;
  for (int i = 0; i < T; ++i) {
    std::cin >> S >> K;
    // std::cerr << K << S << std::endl;
    std::cout << "Case #" << (i + 1) << ": " << solver.run(S, K) << std::endl;
  }

  return 0;
}
