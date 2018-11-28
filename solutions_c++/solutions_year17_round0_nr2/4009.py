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

void solve(int t) {
  cerr << "test " << t << endl;
  string s;
  cin >> s;
  for(int i=s.length()-1; i>0; i--) {
    if(s[i] < s[i-1]) {
      s[i-1]--;
      for(unsigned int j=i; j<s.length(); j++) {
        s[j] = '9';
      }
    }
  }
  cout << "Case #" << t << ": ";
  if(s[0] != '0') {
    cout << s[0];
  }
  for(unsigned int i=1; i<s.length(); i++) {
    cout << s[i];
  }
  cout << endl;
}

int main() {
  cin >> T;
  for(int t=0; t<T; t++) {
    solve(t+1);
  }
}
