#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

bool go(string& s) {
  size_t ptr = 0;
  while(ptr + 1 < s.size() && s[ptr] <= s[ptr + 1]){
    ptr += 1;
  }
  if(ptr + 1 == s.size()){
    return false;
  }
  s[ptr] -= 1;
  ptr += 1;
  while(ptr < s.size()){
    s[ptr] = '9';
    ptr += 1;
  }
  return true;
}

void solve() {
  string s;
  cin >> s;
  while(go(s));
  cout << stoll(s) << endl;
}

int main() {
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";
    solve();
  }
}
