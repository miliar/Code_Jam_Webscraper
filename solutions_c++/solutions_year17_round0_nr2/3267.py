#include <fstream>
#include <sstream>

std::string computeResult(const std::string &S) {
  // 98765 -> 89999
  // 78099 -> 77999
  // 77666 -> 69999

  // 77999 78888
  // 89999 99999
  // 99999 111111

  // d1 d2 d3 d4...
  // d_n, d_{n+1}
  
  // go back to the first d_i in a row equal to d_n. everything before
  // must be strictly less (since we assume d_n d_n+1 is the first
  // decrease)
  // if d_i > 1, we can decrement d_i, and make the remaining digits 9's.
  // if d_i == 1, this must mean we are at the beginning too. then, we chop the first one, and make the rest of the digits 9's.
  // d_i cannot be 0

  // find when the digit goes down.
  int L = S.length();
  int pos = -1;
  for (int i=0;i<L-1;++i) {
    if (S[i] > S[i+1]) {
      for (int j=i;j>=0;--j) {
        if (S[j] != S[i]) {
          break;
        }
        pos = j;
      }
      break;
    }
  }
  if (pos == -1) {
    return S;
  }

  std::stringstream ss{};
  if (S[pos] == '1') {
    for (int i=0;i<L-1;++i) {
      ss << '9';
    }
    return ss.str();
  }

  for (int i=0;i<pos;++i) {
    ss << S[i];
  }
  char c = S[pos] - 1;
  ss << c;
  for (int i=pos+1;i<L;++i) {
    ss << '9';
  }
  return ss.str();
}

int main() {
  std::ifstream fin {"B-large.in"};
  std::ofstream fout {"B-large.out"};
  int T;
  fin >> T;
  for (int i=1;i<=T;++i) {
    std::string S;
    fin >> S;

    std::string result = computeResult(S);
    fout << "Case #" << i << ": " << result << std::endl;
  }
  return 0;
}
