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
void solve(int test) {
   int n = read(), m = read();
   char a[n + 1][m + 1];
   for(int i = 1; i <= n; i ++) {
      for(int j = 1; j <= m; j ++)
         cin >> a[i][j];
   }
   for(int it = 1; it <= n; it ++) {
      for(int i = 1; i <= n; i ++) {
         char x = '?';
         for(int j = 1; j <= m; j ++) {
            if(a[i][j] != '?') {
               x = a[i][j];
               break;
            }
         }
         if(x != '?') {
            for(int j = 1; j <= m; j ++) {
               if(a[i][j] == '?')
                  a[i][j] = x;
               else
                  x = a[i][j];
            }
         }
         else if (it > 1){
            if(i == 1) {
               for(int j = 1; j <= m; j ++) {
                  for(int k = i; k <= n; k ++) {
                     if(a[k][j] != '?') {
                        x = a[k][j];
                        break;
                     }
                  }
                  a[i][j] = x;
               }
            }
            else {
               for(int j = 1; j <= m; j ++)
                  a[i][j] = a[i - 1][j];
            }
         }
      }
   }
   cout << "Case #" << test << ":\n";
   for(int i = 1; i <= n; i ++) {
      for(int j = 1; j <= m; j ++)
         cout << a[i][j];
      cout << endl;
   }
}
main() {
   freopen("A-large.in", "r", stdin);
   freopen("output.txt", "w", stdout);
   int t = read();
   for(int i = 1; i <= t; i ++)
      solve(i);
}

/*
10
6 2
??
CB
EA
??
D?
??
*/
