#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>

using namespace std;

void flip(string& s, int offset, int fSize) {
  for (int i = offset; i < offset+fSize; i++) {
    s[i] = (s[i] == '+' ? '-' : '+');
  }
}

int solve(string& s, int fSize) {
  int flipped = 0;
  for (int i = 0; i <= s.length()-fSize; i++) {
    if (s[i] == '-') {
      flip(s, i, fSize);
      flipped++;
    }
  }
  
  for (int i = s.length()-fSize; i < s.length(); i++) {
    if (s[i] != '+') {
      return -1;
    }
  }
  
  return flipped;
}

int main() {
  int t_cases;
  cin >> t_cases;
  for (int c = 1; c <= t_cases; c++) {
    string s;
    int k;
    cin >> s >> k;
    
    int flips = solve(s, k);
    cout << "Case #" << c << ": ";
    if (flips == -1) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << flips << endl;
    }
  }
  
  return 0;
}
