/*************************************************************************
     File Name: gcjb-small.cpp
     ID: obsoles1
     PROG: 
     LANG: C++ 
     Mail: 384099319@qq.com 
     Created Time: Fri 07 Apr 2017 11:43:05 PM EDT
 ************************************************************************/
#include<iostream>
#include<cstring>
using namespace std;
const int N = 20;
char s[N];

int main() {
  //freopen("B-small-attempt2.in", "r", stdin);
  freopen("B-large.in", "r", stdin);
  freopen("b-large.out", "w", stdout);
  //freopen("b-small.out", "w", stdout);
  int t, length;
  cin >> t;
  for (int caseNum = 1; caseNum <= t; ++caseNum) {
    cout << "Case #" << caseNum << ": ";
    cin >> s;
    length = strlen(s);
    if (length == 1) {
      cout << s << endl;
      continue;
    }
    int pos = 0;
    for (int i = 1; i < length; ++i) {
      if (s[i] > s[pos]) pos = i;
      else if (s[i] < s[pos]) {
        if (pos == 0 && s[pos] == '1') length--;
        else {
          s[pos]--;
          for (int j = pos + 1; j < length; ++j) {
            s[j] = '9';
          }
        }
        break;
      }
    }
    if (length == strlen(s)) cout << s << endl;
    else {
      for (int i = 0; i < length; ++i) cout << '9';
      cout << endl;
    }
  }
}
