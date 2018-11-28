#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

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

const long double PI = 3.141592653589793238;

void PrintAnswer(const int test, const int64_t x) {
  std::cout << "Case #" << test + 1 << ": " << PI * static_cast<long double>(x) << "\n";
}

struct Cake {
  int64_t r;
  int64_t h;
  int64_t area;

  bool operator < (const Cake& other) {
    return area > other.area;
  }
};

int64_t Solve(const int N, const int K, std::vector<Cake>& cakes) {
  std::sort(cakes.begin(), cakes.end());

  int64_t first_type_answer = 0;
  int64_t max_r = 0;

  for (int i = 0; i < K; ++i) {
    first_type_answer += 2 * cakes[i].area;
    max_r = std::max(max_r, cakes[i].r);
  }
  first_type_answer += max_r * max_r;

  int64_t second_type_answer = 0;
  for (int i = 0; i < K - 1; ++i) {
    second_type_answer += 2 * cakes[i].area;
  }
  int64_t max_r_h = 0;
  for (int i = K - 1; i < N; ++i) {
    max_r_h = std::max(max_r_h, cakes[i].r * (cakes[i].r + 2 * cakes[i].h));
  }
  second_type_answer += max_r_h;

  // std::cout << "first type = " << first_type_answer << "\n";
  // std::cout << "second type = " << second_type_answer << "\n";

  return std::max(first_type_answer, second_type_answer);
}

int main() {

  std::ios_base::sync_with_stdio(false);

  std::cout.precision(15);
  std::cout << std::fixed;

  int32_t T = ReadInt32();

  for (int i = 0; i < T; ++i) {
    int N = ReadInt32();
    int K = ReadInt32();
    std::vector<Cake> cakes;
    for (int i = 0; i < N; ++i) {
      int64_t r = ReadInt64();
      int64_t h = ReadInt64();
      cakes.push_back({r, h, r * h});
    }
    int64_t answer = Solve(N, K, cakes);
    PrintAnswer(i, answer);
  }

  return 0;

}
