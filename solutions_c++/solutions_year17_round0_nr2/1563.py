#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <list>

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " << 

using namespace std;

string solve(string s) {
  int n = (int)s.size();
  for (int i=0; i<n-1; i++)
    if (s[i] > s[i+1]) {
      long long left = stoll(s.substr(0, i+1));
      string sleft = solve(to_string(left-1));
      for (int j=i+1; j<n; j++)
        sleft += '9';
      return sleft;
    }
  return s;
}

int main() {
  int t;
  cin >> t;
  for (int tt=0; tt<t; tt++) {
    string s;
    cin >> s;
    cout << "Case #" << tt+1 << ": " << stoll(solve(s)) << endl;
  }
  return 0;
}
