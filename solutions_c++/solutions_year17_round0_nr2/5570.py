/*
 Author:    sergioRG
*/
#include <bits/stdc++.h>
using namespace std;
string num;
string ans;
bool some_found;

// imitar parte creciente -> digito menos uno -> todo nueves
string backtrack(int digit, bool smaller, int at_least) {
  if(digit == int(num.size())) {
    some_found = at_least > 0;
    return "";
  }
  int current_digit = num[digit]-'0';
  int to_start = at_least;
  int to_end = smaller ? 9 : current_digit;
  for(int i=to_end; i>=to_start; --i) {
    string cand;
    cand += char(i+'0');
    cand += backtrack(digit+1, smaller || i < current_digit, i);
    if(some_found) return cand;
  }
  if(at_least == 0) {
    return '0' + backtrack(digit+1, true, at_least);
  }
  return "";
}

string as_number(string x) {
  int n = int(x.size());
  string ret;
  int i = 0;
  while(i<n && x[i] == '0') ++i;
  while(i<n) {
    ret += x[i];
    ++i;
  }
  return ret;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(0);
  int T;
  cin >> T;
  for(int test_case=1; test_case<=T; ++test_case) {
    some_found = false;
    ans = "";
    cin >> num;
    ans = backtrack(0, false, 0);
    cout << "Case #" << test_case << ": " << as_number(ans) << endl;
  }
}
