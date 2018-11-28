#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <unordered_map>
using namespace std;

//ifstream fin("A-small-attempt0.in");
//ofstream fout("A-small.out");

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int cnt(string& s, char c) {
  int out = 0;
  for (int i = 0; i < s.size(); ++i) {
    if (s[i] == c) {
      ++out;
    }
  }
  return out;
}

void task() {
  string s;
  int k;
  fin >> s >> k;
  int plus = cnt(s, '+');
  int minus = cnt(s, '-');
  
  if (k == 1) {
    fout << minus;
    return;
  }
  if (plus == s.size()) {
    fout << 0;
    return;
  }

  int res = 0;
  for (int i = 0; i < s.size(); ++i) {
    if (s[i] == '-' && i + k - 1 < s.size()) {
      for (int j = i; j < i + k; ++j) {
        s[j] = (s[j] == '+') ? '-' : '+';
      }
      i = -1;
      ++res;
    }
  }
  plus = cnt(s, '+');
  if (plus == s.size()) {
    fout << res;
  }
  else {
    fout << "IMPOSSIBLE";
  }
}

int main() {

  long long t = 0;
  fin >> t;

  for (long long i = 0; i < t; i++) {
    fout << "case #" << i + 1 << ": ";
    task();
    fout << endl;
  }
  fout.close();
  cout << "OK";
  return 0;
}