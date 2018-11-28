#include <cmath>
#include <iostream>

using namespace std;

namespace {

long GetDecreasingIndex(long n) {
  int places = 1;
  while (n >= 10) {
    int ones = n % 10;
    int tens = (n % 100) / 10;
    if (tens > ones) {
      return places;
    }
    n /= 10;
    places++;
  }
  return 0;
}

long Solve(long n) {
  long result = n;
  int places = GetDecreasingIndex(result);
  while (places != 0) {
    int pow_places = static_cast<int>(pow(10, places));
    long prefix = ((result / pow_places) - 1) * pow_places;
    long suffix = pow_places - 1;
    result = prefix + suffix;
    places = GetDecreasingIndex(result);
  }
  return result;
}

}  // namespace

int main() {
  long T, N;
  cin >> T;
  for (size_t i = 1; i <= T; i++) {
    cin >> N;
    cout << "Case #" << i << ": " << Solve(N) << '\n';
  }
  return 0;
}
