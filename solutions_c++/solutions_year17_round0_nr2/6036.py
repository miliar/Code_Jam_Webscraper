#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> VI;

const int MAX_N = 1005;

void solve() {
  string s;
  cin >> s;
  int n = s.size();

  for (int i = 0; i < n-1; i++) {
    int i2 = n-i-1;
    int i1 = i2-1;
    char c1 = s[i1];
    char c2 = s[i2];
    if (c1 > c2) {
      s[i1]--;
      for (int j = i2; j < n; j++) {
        s[j] = '9';
      }
    }
  }

  int i = 0;
  while (s[i] == '0') {
    i++;
  }
  for (;i < n; i++) {
    cout << s[i];
  }
}

int main() {
  int N;
  cin >> N;

  for (int i = 0; i < N; i++) {
    cout << "Case #" << (i+1) << ": ";
    solve();
    cout << endl;
  }

  return 0;
}
