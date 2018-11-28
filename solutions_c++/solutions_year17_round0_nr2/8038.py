#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int get_digit(long long n, int index, int length) {
  int i = length - 1 - index;
  while (i > 0) {
    n /= 10;
    i--;
  }

  return (int)(n % 10);
}

int get_length(long long n) {
  int length = 0;
  do {
    ++length;
    n /= 10;
  } while (n);

  return length;
}

// Decrement the index-th digit and set the lower digits to 9s.
void decrement(long long &n, int index, int length) {
  int i = length - 1 - index;
  while (i > 0) {
    n /= 10;
    i--;
  }

  i = length - 1 - index;
  while (i > 0) {
    n *= 10;
    i--;
  }

  n--;
}

bool is_tidy(long long n, int& start) {
  int length = get_length(n);
  int curr = get_digit(n, 0, length);
  int prev = 0;
  for (int i = 1; i < length; ++i) {
    prev = curr;
    curr = get_digit(n, i, length);
    if (curr < prev) {
      start = i;
      return false;
    }
  }

  start = -1;
  return true;
}

void process_case() {
  long long N;
  cin >> N;

  // single digit
  if (N < 10) {
    cout << N;
    return; 
  }

  int start;
  while (!is_tidy(N, start)) {
    decrement(N, start - 1, get_length(N));
  }

  cout << N;
}

int main() {
  int T;
  cin >> T;

  for (int n = 0; n < T; ++n) {
    cout << "Case #" << (n + 1) << ": ";
    process_case();
    cout << endl;
  }
}
