#include <iostream>
#include <vector>

using namespace std;

void genRevArray(long long n, vector<int>* res) {
  while (n > 0) {
    int digit = n % 10;
    res->push_back(digit);
    n = n / 10;
  }
}

long long genNumber(const vector<int>& digits) {
  long long res = 0;
  for (int i = digits.size() - 1; i >= 0; --i) {
    res = res * 10 + digits[i];
  }
  return res;
}

int findFirstSplit(const vector<int>& digits) {
  if (digits.size() == 1) return -1;
  for (int i = 0; i < digits.size(); ++i) {
    if (digits[i] >= digits[i + 1]) continue;
    return i;
  }
  return -1;
}

void printDigits(const vector<int>& rev_digits) {
  for (int i = rev_digits.size() - 1; i >= 0; --i) {
    cout << rev_digits[i];
  }
  cout << endl;
}

long long lastTidy(long long n) {
  vector<int> rev_digits;
  genRevArray(n, &rev_digits);
  int split_point = findFirstSplit(rev_digits);
  while (split_point != -1) {
    for (int i = 0; i <= split_point; ++i) {
      rev_digits[i] = 9;
    }
    rev_digits[split_point + 1]--;
    split_point = findFirstSplit(rev_digits);
  }
  return genNumber(rev_digits);
}

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    long long N;
    cin >> N;
    long long res = lastTidy(N);
    cout << "Case #" << i << ": " << res << endl;
  }
  return 0;
}
