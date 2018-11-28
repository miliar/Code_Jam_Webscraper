#pragma GCC optimize ("O2")
#include <bits/stdc++.h>
#include <unistd.h>

using namespace std;

#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
#define fst first
#define snd second

template<typename A, typename B>
ostream& operator <<(ostream& s, const pair<A, B>& p)
{
  return s << "(" << p.first << "," << p.second << ")";
}
template<typename T>
ostream& operator <<(ostream& s, const vector<T>& c)
{
  s << "[ ";
  for (auto it : c) s << it << " ";
  s << "]";
  return s;
}

int main()
{
  IOS;
  int T;
  cin >> T;
  string num;
  for (int tt = 1; tt <= T; ++tt) {
    cin >> num;
    int bp = -1;
    for (int i = 1; i < (int)num.length(); ++i) {
      if (num[i] < num[i - 1]) {
        bp = i;
        break;
      }
    }
    if (bp != -1) {
      bp -= 1;
      for (int i = bp; i > 0; --i) {
        if (num[i] == num[i - 1])
          bp--;
        else
          break;
      }
      num[bp] -= 1;
      for (int i = bp + 1; i < (int)num.length(); ++i) {
        num[i] = '9';
      }
    }
    int st = 0;
    while (num[st] == '0')
      st++;
    cout << "Case #" << tt << ": ";
    cout << num.substr(st) << endl;
  }
  return 0;
}
