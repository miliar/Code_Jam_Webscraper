#include <bits/stdc++.h>

#define pb push_back
#define db double
#define int long long
#define all(c) (c).begin(), (c).end()
using namespace std;

const int N = 1e6 + 1;
const int mod = 1e9 + 7;
typedef pair<int, int> pii;

inline int read () {
   char c = getchar();
   int t = 0, f = 1;
   while (!isdigit(c)) f = (c == '-') ? -1 : 1, c = getchar();
   while (isdigit(c)) t = t * 10 + c - 48, c = getchar();
   return t * f;
}
void writeln(string res, int test) {
   cout << "Case #" << test << ": " << res << endl;
}
bool check(string s) {
   for(int i = 0; i + 1 < s.size(); i ++)
      if(s[i] > s[i + 1])
         return false;
   return true;
}
void solve(int test) {
   string s, ans;
   cin >> s;
   if(check(s)) {
      writeln(s, test);
      return;
   }
   int n = s.size(), id;
   for(int i = 0; i < n - 1; i ++) {
      if(s[i] > s[i + 1]) {
         id = i;
         break;
      }
   }
   char x = s[id] - 1;
   if(x == '0') {
      for(int i = 1; i < n; i ++)
         ans += '9';
      writeln(ans, test);
      return;
   }
   int ind = 0;
   for(int i = id; i > 0; i --) {
      if(s[i] > s[i - 1]) {
         ind = i;
         break;
      }
   }
   for(int i = 0; i < ind; i ++)
      ans += s[i];
   ans += s[ind] - 1;
   for(int i = ind + 1; i < n; i ++)
      ans += '9';
   writeln(ans, test);
}
main() {
   freopen("B-large.in", "r", stdin);
   freopen("output.txt", "w", stdout);
   int t = read();
   for(int i = 1; i <= t; i ++)
      solve(i);
}
/**
40
132
1000
132135464
1210
125646464
7
111111111111111110
*/
