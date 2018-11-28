#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

bool is_tidy(long long int test) {
  vector<int> numbers;
  while (test > 0) {
    numbers.push_back(test % 10);
    test /= 10;
  }
  reverse(numbers.begin(), numbers.end());
  return is_sorted(numbers.begin(), numbers.end());
}

long long int find_max_tidy(long long int N) {
  if (N < 10) {
    return N;
  } else {
    long long int max = 0;
    for (int i = 1; i < N + 1; i++) {
      if (is_tidy(i) && max < i) {
        max = i;
      }
    }
    return max;
  }
}

int main() {
  int N;
  long long int test;
  vector<long long int> V;
  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> test;
    V.push_back(test);
  }
  for (int i = 0; i < N; i++) {
    long long int max = find_max_tidy(V[i]);
    cout << "Case #" << i + 1 << ": " << max << endl;
  }
  return 0;
}
