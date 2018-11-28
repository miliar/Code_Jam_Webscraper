#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pi 3.14159265358979323846264338327950288
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SZ(x) ((int)x.size())

#define Left k * 2, l, mid
#define Right k * 2 + 1, mid + 1, r
#define N 1111111
using namespace std;
bool check(LL x) {
  string s = to_string(x);
  int n = s.length();
  for (int i = 1; i < n; i++)
    if (s[i] < s[i - 1]) return false;
  return true;
}
LL brute_force(LL x) {
  for (LL i = x; i; i--)
    if (check(i)) return i;
  return 0;
}
LL work(LL x) {
  LL ans = 0;
  if (check(x)) ans = x;
  string s = to_string(x);
  string sub = "";
  string t = "";
  int n = s.length();
  bool eq = false;
  for (int i = 0; i < n - 1; i++) {
    if (s[i] >= s[i + 1]) {
      if (eq && s[i] > s[i + 1]) break;
      if (eq && s[i] == s[i + 1]) {
        sub += s[i];
        continue;
      }
      sub += (char)(s[i] - 1);
      t = sub;
      for (int j = i + 1; j < n; j++)
        t += '9';
      ans = max(ans, stoll(t));
      if (s[i] == s[i + 1]) {
        eq = true;
        sub[i] = s[i];
      }
    }
    else {
      eq = false;
      sub += s[i];
  }
  }
  return ans;
}

int T;
LL x;
int main() {

  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);
  for (int cas = 1; cas <= T; cas ++) {
    cin >> x;
    cout << "Case #" << cas << ": " << work(x) << endl;
  }

  /*bool flag = true;
  for (LL i = 1; i <= 1000000; i++) {

    LL ans1 = work(i);
    LL ans2 = brute_force(i);
    if (ans1 == ans2) {
      if (i % 10000 == 0) cout << i << " " << "Check OK!" << endl;
    }
    else {
      cout << i << " " << "Check Error : work = " << ans1 << " brute_force = " << ans2 << endl;
      flag = false;
    }
  }
  if (flag) cout << "All check passed." << endl;*/
}
