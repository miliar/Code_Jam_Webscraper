#include <iostream>
#include <string>
#include <bitset>

void print(int caseNum, std::string output) {
  std::cout << "Case #" << caseNum << ": " << output << std::endl;
}

int main() {
  std::string line;
  getline(std::cin, line);
  int T = std::stoi(line);

  for (int t = 1; t <= T; ++t) {
    getline(std::cin, line);
    size_t pos = line.find(" ");
    std::string S = line.substr(0, pos);
    int K = std::stoi(line.substr(pos+1));

    int count = 0;

    int S_size = S.size();
    for (int i = 0; i <= S_size-K; ++i) {
      if (S[i] == '+') continue;
      for (int j = i; j < i+K; ++j) {
        S[j] = (S[j] == '+') ? '-' : '+';
      }
      count++;
    }

    bool impossible = false;
    for (int i = 0; i < K-1; ++i) {
      if (S[S_size-i-1] == '-') {
        impossible = true;
        break;
      }
    }

    std::string IMP("IMPOSSIBLE");
    print(t, impossible ? IMP : std::to_string(count));
  }

  return 0;
}
