#include <iostream>
#include <sstream>
#include <climits>
#include <stdio.h>
#include <iomanip>
#include <list>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <string>
#include <gmpxx.h>

using namespace std;

int T;

int working(string s, unsigned int f) {
  unsigned int i=0;
  int flips = 0;
  while(i+f <= s.length()) {
    //cerr << "check " << i << " " << s << endl;
    if(s[i] == '-') {
      flips++;
      for(unsigned int j = 0; j<f; j++) {
        if(s[i+j] == '+') {
          s[i+j] = '-';
        } else {
          s[i+j] = '+';
        }
      }
    }
    i++;
  }
  //cerr << "after: " << s << endl;
  for(unsigned int i=0; i<s.length(); i++) {
    if(s[i] == '-') {
      return -1;
    }
  }
  return flips;
}

void solve(int t) {
  cerr << "test " << t << endl;
  string s;
  int f;
  cin >> s;
  cin >> f;
  int result = working(s, f);
  cout << "Case #" << t << ": ";
  if(result == -1) {
    cout << "IMPOSSIBLE";
  } else {
    cout << result;
  }
  cout << endl;
}

int main() {
  cin >> T;
  for(int t=0; t<T; t++) {
    solve(t+1);
  }
}
