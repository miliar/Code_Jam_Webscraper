#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

void solve(string s, int k) {
  int size = s.length()-1;
  int cnt = 0;

  for (int i = 0; i < (size+1) / 2; ++i) {
    if (s[i] == '-' && (i + k) <= size+1) {
      for (int j = 0; j < k; ++j)
        s[j+i] = s[j+i] == '-' ? '+' : '-';

      ++cnt;
    } 

    if (s[size-i] == '-' && size+1-i-k >= 0) {
      for (int j = 0; j < k; ++j) 
        s[size-i-j] = s[size-i-j] == '-' ? '+' : '-';

      ++cnt;
    }
  }

  for (int i = 0; i < (size+1); ++i) {
    if (s[i] == '-') {
      cout << "IMPOSSIBLE";
      return;
    }
  }

  cout << cnt;
}

int main() {
  int T;
  cin >> T;
  
  for (int t = 0; t < T; ++t) {
    string s;
    int k;

    cin >> s >> k;

    cout << "Case #" << t+1 << ": ";
    solve(s, k);
    cout << "\n"; 
  }

  return 0;
}