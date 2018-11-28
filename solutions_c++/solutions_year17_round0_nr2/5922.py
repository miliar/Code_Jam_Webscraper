#!/usr/bin/env cppsh
#include <iostream>
#include <sstream>
#include <string>
using namespace std;
typedef long long ll;

class Solution
{
public:
  ll last_tidy(ll n) {
    string str = ll_to_str(n);
    while (int pos = find_inversion(str)) {
      fixup(str, pos);
    }
    return str_to_ll(str);
  }

  int find_inversion(const string& s) {
    for (int i = s.size()-1; i > 0; --i) {
      if (s[i-1] > s[i])
        return i;
    }
    return 0;
  }

  void fixup(string& s, int inversion_pos) {
    int i = inversion_pos - 1;
    s[i]--;
    for (i = i + 1; i < s.size(); ++i) {
      s[i] = '9';
    }
  }

  string ll_to_str(ll n) {
    stringstream ss;
    ss << n;
    return ss.str();
  }

  ll str_to_ll(const string& str) {
    string s(str);
    s = s.substr(s.find_first_of("123456789"));
    stringstream ss;
    ss << s;
    ll n;
    ss >> n;
    return n;
  }
};

int main(int argc, char *argv[]) {
  Solution soln;
  int T;
  cin >> T;
  ll num;
  for (int t = 1; t <= T; ++t) {
    cin >> num;
    cout << "Case #" << t << ": " << soln.last_tidy(num) << "\n";
  }
  
  return 0;
}
