#include <fstream>

struct Result {
  int min;
  int max;
};

Result computeResult(const int &N, const int &K) {
  // N is number of stalls
  // K is number of people
  int bitcounting = K;
  int bits = 0;
  while (bitcounting > 0) {
    bitcounting >>= 1;
    ++bits;
  }
  // K = 2^a + b
  int a = bits-1;
  int pow = 1<<a;
  int b = K - pow;
  int div = (N-pow+1) / pow;
  int rem = (N-pow+1) % pow;

  int emptyStallPool = div;
  if (b < rem) {
    ++emptyStallPool;
  }

  int min = (emptyStallPool - 1) / 2;
  int max = min;
  if ((emptyStallPool - 1) % 2 == 1) {
    ++max;
  }
  Result result {min, max};
  return result;
}

int main() {
  std::ifstream fin {"C-small-2-attempt0.in"};
  std::ofstream fout {"C-small-2-attempt0.out"};
  int T;
  fin >> T;
  for (int i=1;i<=T;++i) {
    int N, K;
    fin >> N >> K;

    Result result = computeResult(N, K);
    fout << "Case #" << i << ": " << result.max << ' ' << result.min << std::endl;
  }
  return 0;
}

// 100
// 1: 100 -> 50 49
// 2: 50 -> 25 24
// 3: 49 -> 24 24
// 4: 25 -> 12 12
// 5: 24 -> 12 11
// 6: 24 -> 12 11
// 7: 24 -> 12 11

// 1
// 2, 3
// 4 5 6 7

// person K = 2^a + b (0 <= b < 2^a)
// after 2^a - 1 people have gone, N - 2^a + 1 stalls are left, divided relatively evenly
// divide this by 2^a. the remainder when dividing will be the number of slightly larger stretches of stalls.

// e.g. after 7 people have gone, 100 - 7 = 93 stalls are left
// divided by 8, we get 93 = 8*11 + 5, so there are 5 stalls with 12, 3 stalls with 11
// person 8 through 12 have 12, 13 through 15 have 11
// persons in [2^3, 2^3 + rem> have more, [2^3+rem, 2^4> have less
