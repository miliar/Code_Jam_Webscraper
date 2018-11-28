#include <iostream>
#include <fstream>
#include <vector>
#include <cassert>
#include <algorithm>

std::string prepare(std::string S) {
  auto first_pos = S.find_first_not_of("0");
  if (first_pos == std::string::npos) return "0";
  return S.substr(first_pos);
}

std::string solve(std::string S) {
  for (int idx = S.size()-1; idx >= 0; --idx) {
    int jdx = idx - 1;
    if (jdx < 0) {
      return prepare(S);
    }
    if (S[idx] < S[jdx]) {
      assert(S[jdx] > '0'); // since it's greater than S[idx]
      S[jdx] = char(int(S[jdx]) - 1);
      for (size_t kdx = idx; kdx < S.size(); ++ kdx) {
        S[kdx] = '9';
      }
    }
  }
  return prepare(S);
}


void solution(const std::string& input, const std::string& output) {
  std::ifstream infile(input);
  std::ofstream outfile(output);

  size_t T;
  infile >> T;

  std::string S;
  for (size_t idx=0; idx < T; ++ idx) {
    infile >> S;
    auto answer = solve(S);

    outfile << "Case #" << idx + 1 << ": ";

    outfile << answer;
    outfile << std::endl;
  }
  infile.close();
  outfile.close();
}

int main(int argc, char** argv) {
  solution(argv[1], argv[2]);
  return 0;
}
