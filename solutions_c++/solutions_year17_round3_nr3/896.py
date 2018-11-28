#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#define ld long double

std::string readStr() {
  std::string str;
  std::cin >> str;
  return str;
}

int ReadInt32() {
  int32_t x;
  std::cin >> x;
  return x;
}

int64_t ReadInt64() {
  int64_t x;
  std::cin >> x;
  return x;
}

ld ReadLD() {
  ld x;
  std::cin >> x;
  return x;
}

const long double PI = 3.141592653589793238;

void PrintAnswer(const int test, const ld x) {
  std::cout << "Case #" << test + 1 << ": " << x << "\n";
}

ld Solve(int N, int K, ld U, std::vector<ld> p) {
  std::sort(p.begin(), p.end());
  p.push_back(1.0);
  for (int it = 1; it <= N; ++it) {
    ld cur = p[0];
    ld next = p[it];
    ld add = std::min(U / it, next - cur);
    for (int i = 0; i < it; ++i) {
      p[i] += add;
    }
    U -= add * it;
  }
  for (int i = 0; i < N; ++i) {
    // std::cout << p[i] << "\n";
  }

  ld ans = 1.0;

  for (int i = N - 1; i >= 0; --i) {
    ans *= p[i];
  }
  return ans;
}

int main() {

  std::ios_base::sync_with_stdio(false);

  std::cout.precision(15);
  std::cout << std::fixed;

  int32_t T = ReadInt32();

  for (int i = 0; i < T; ++i) {
    int N = ReadInt32();
    int K = ReadInt32();
    ld U = ReadLD();
    std::vector<ld> p;
    for (int j = 0; j < N; ++j) {
      ld p_j = ReadLD();
      p.push_back(p_j);
    }
    ld answer = Solve(N, K, U, p);
    PrintAnswer(i, answer);
  }

  return 0;

}
