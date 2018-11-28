#include <string>
#include <iostream>

int solve1(int N);
bool isTidy(int x);
std::string solve2(std::string N);

int main(int argc, char **argv) {
  int T;
  std::cin >> T;

  //for (int x = 1; x <= T; ++x) {
  //  int N;
  //  std::cin >> N;
  //  std::cout << "Case #" << x << ": " << solve1(N) << std::endl;
  //}

  for (int x = 1; x <= T; ++x) {
    std::string N;
    std::cin >> N;
    std::cout << "Case #" << x << ": " << solve2(N) << std::endl;
  }

  return 0;
}

bool isTidy(int x) {
  int x1;
  while ((x1 = x / 10) > 0) {
    if (x % 10 < x1 % 10) {
      return false;
    }
    x = x1;
  }

  return true;
}

int solve1(int N) {
  while (N > 0) {
    if (isTidy(N)) {
      break;
    }
    --N;
  }

  return N;
}

std::string solve2(std::string N) {
  for (int i = 0; i < N.length()-1; ++i) {
    if (N[i+1] < N[i]) {
      N[i] = N[i] - 1;
      for (int j = i+1; j < N.length(); ++j) {
        N[j] = '9';
      }
      N = solve2(N);
      break;
    }
  }

  int i = 0;
  while (N[i] == '0') {
    ++i;
  }

  return N.substr(i, std::string::npos);
}
