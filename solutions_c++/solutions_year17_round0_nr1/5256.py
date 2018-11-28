/*************************************************************************
     File Name: gcja-small.cpp
     ID: obsoles1
     PROG: 
     LANG: C++ 
     Mail: 384099319@qq.com 
     Created Time: Fri 07 Apr 2017 10:11:18 PM EDT
 ************************************************************************/
#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
const int N = 1010;
char s[N];

int main() {
  freopen("A-small-attempt3.in", "r", stdin);
  freopen("a-small.out", "w", stdout);
  int t, k, cnt;
  cin >> t;
  for (int caseNum = 1; caseNum <= t; ++caseNum) {
    cin >> s >> k;
    //cout << s <<' '<<k<< endl;
    int length = strlen(s), ans = 0;
    bool flag = 1;
    for (int i = 0; i < length; ++i) {
      if (s[i] == '+') continue;
      int change = 0;
      for (int j = i; j < i+k-1 && j < length-1; ++j) {
        //cout << s[j] << ' ';
        if (s[j] != s[j+1]) change++;
      }
      //cout<<endl;
      //cout<<"change="<<change<<endl;
      if (change > 2) {
        flag = 0;
        break;
      }
      if (i+k <= length) {
        for (int j = i; j < i+k; ++j) {
          if (s[j] == '-') s[j] = '+';
          else s[j] = '-';
        }
        ans++;
      }
      //cout<<s<<endl;
    }
    //cout<<s<<endl;
    cnt = 0;
    for (int i = 0; i < length; ++i) if (s[i] == '-') cnt++;
    //cout<<"cnt="<<cnt<<endl;
    cout << "Case #" << caseNum << ": ";
    if (flag && cnt == 0) cout << ans << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
}
