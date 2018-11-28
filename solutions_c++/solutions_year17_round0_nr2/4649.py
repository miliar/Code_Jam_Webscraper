#include <iostream>

using namespace std;

static int GetDigit(char ch) {
  return ch - '0';
}

static void TidyNumber(string& N, int index) {
  N[index] -= 1;
  for (int i = index + 1; i < N.length(); ++i) {
    N[i] = '9';
  }
  if (N[0] == '0') {
    N = N.substr(1);
  }
}

static string GetLastTidyNumber(const string& N) {
  string result = N;
  int prevDigit = GetDigit(result[0]);
  int prevIndex = 0;
  for (int i = 1; i < N.length(); ++i) {
    int digit = GetDigit(result[i]);
    if (prevDigit > digit) {
      TidyNumber(result, prevIndex);
      break;
    } else if (prevDigit < digit) {
      prevIndex = i;
      prevDigit = digit;
    }
  }

  return result;
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    string N;
    cin >> N;
    cout << "Case #" << (t + 1) << ": " <<  GetLastTidyNumber(N) << endl;
  }

  return 0;
}
