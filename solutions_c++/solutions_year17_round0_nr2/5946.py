#include <iostream>
#include <unordered_set>
#include <cstring>

using namespace std;

static bool is_tidy(string& s) {
  int start = 0;
  for (int i = 0; i < s.size(); ++i) {
    if (s[i] == '0') continue;
    start = i;
    break;
  }

  for (int i = start + 1; i < s.size(); ++i) {
    if (s[i-1] > s[i])
      return false;
  }
  return true;
}

static void sub_1(string& s, int start, int end) {
  int carry = 1;
  for (int i = end; i >= start; --i) {
    int n = s[i] - '0';
    if (n >= carry) {
      n -= carry;
      s[i] = n + '0';
      break;
    }
    n += 10;
    n -= carry;
    s[i] = n + '0';
    carry = 1;
  }
  // cout << s << endl;
}

static void tidy(string N) {
  int start = 0, end = N.size() - 1;
  while (!is_tidy(N)) {
    end = N.size() - 1;
    while (N[end] == '9')
      --end;
    sub_1(N, start, end);
  }
  string res;
  start = 0;
  for (int i = 0; i < N.size(); ++i) {
    if (N[i] == '0') continue;
    start = i;
    break;
  }
  for (int i = start; i < N.size(); ++i) {
    res += N[i];
  }
  cout << res;
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    string N;
    cin >> N;
    cout << "Case #" << i+1 << ": ";
    tidy(N);
    cout << endl;
  }
  return 0;
}

