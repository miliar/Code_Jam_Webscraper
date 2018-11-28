#include <iostream>
#include <string>
using namespace std;

void toTidy(string& s, int idx) {
  int l = s.length();
  s[idx] = s[idx]-1;
  for(int i = idx+1; i < l; i++) {
    s[i] = '9';
  }
}

string getTidy(string s) {
  int l = s.length();
  if(l == 1)
    return s;

  for(int i = l-2; i >= 0; i--) {
    if(s[i] > s[i+1])
      toTidy(s, i);
  }

  if(s[0] == '0') {
    s.erase(0, 1);
  }

  return s;
}

int main() {
  int nc;
  cin >> nc;
  string sa[nc];
  for(int i = 0; i < nc; i++) {
    cin >> sa[i];
    cout << "Case #" << (i+1) << ": " << getTidy(sa[i]) << endl;
  }

  return 0;
}
