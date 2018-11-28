#include <cassert>
#include <cstring>

#include <algorithm>
#include <iostream>

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define REP(i,n) FOR(i,0,n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

using namespace std;

bool is_tidy(string s) {
  while (s.size() > 1 && s[0] == '0') s = s.substr(1);
  char last = '0';
  for (char d : s) {
    if (d < last)
      return false;
    last = d;
  }
  return true;
}

int main(void) {
  int ntc; cin >> ntc;
  REP(itc, ntc) {
    cout << "Case #" << itc+1 << ": ";
    
    llint nv; cin >> nv;
    string ns = to_string(nv);
    int len = ns.size();
    string best = string(len, '0');
    
    REP(i, len+1) {
      string nov = ns.substr(0, i);
      if (i < len && ns[i] == '0') continue;
      if (i < len) nov += char(ns[i] - 1);
      if (i < len-1) nov += string(len-i-1, '9');
      if (is_tidy(nov) && nov <= ns && nov > best)
        best = nov;
    }

    cout << stoll(best);
    cout << endl;
  }
  return 0;
}
