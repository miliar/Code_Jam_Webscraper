#include <iostream>
#include <fstream>
#include <vector>

int solve(std::string S, int K) {
  int flip = 0;
  for (size_t idx = 0; idx < S.size(); ++ idx) {
    // find first -, flip from it
    if (S[idx] == '-') {
      ++ flip;
      for (size_t jdx=0; jdx < K; ++jdx) {
        if (idx + jdx >= S.size()) { return -1; }
        S[idx + jdx] = S[idx + jdx] == '-' ? '+' : '-';
      }
    }
  }

  return flip;
}

void solution(const std::string& input, const std::string& output) {
  std::ifstream infile(input);
  std::ofstream outfile(output);

  size_t T;
  infile >> T;

  std::string S;
  int K;
  for (size_t idx=0; idx < T; ++ idx) {
    infile >> S >> K;
    auto answer = solve(S, K);

    outfile << "Case #" << idx + 1 << ": ";

    if (answer >= 0) outfile << answer;
    else outfile << "IMPOSSIBLE";
    outfile << std::endl;
  }
  infile.close();
  outfile.close();
}

int main(int argc, char** argv) {
  solution(argv[1], argv[2]);
  return 0;
}
