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
struct pt {
   int x;
   char y;
};
bool comp(pt a, pt b) {
   return a.x > b.x;
}
pt a[3];
void solve(int test) {
   cout << "Case #" << test << ": ";
   int n = read(), x, r, y, b;
   cin >> a[1].x >> x >> a[2].x >> x >> a[3].x >> x;
   a[1].y = 'R';
   a[2].y = 'Y';
   a[3].y = 'B';
   sort(a + 1, a + 4, comp);
   r = a[1].x;
   y = a[2].x;
   b = a[3].x;
   if(2 * r > n) {
      puts("IMPOSSIBLE");
   }
   else {
      bool q = 0;
      while(y > b) {
         cout << a[1].y << a[2].y;
         r --;
         y --;
      }
      while(r > min(y, b) > 0) {
         while(y > b) {
            cout << a[1].y << a[2].y;
            r --;
            y --;
         }
         if(q) {
            if(b > 0) {
               cout << a[1].y << a[3].y;
               b --;
               r --;
            }
         }
         else {
            if(y > 0) {
               cout << a[1].y << a[2].y;
               y --;
               r --;
            }
         }
         q = !q;
      }
      while(r > 0)
         cout << a[1].y << a[2].y << a[3].y, r --;
      cout << endl;
   }
}

main() {
   freopen("B-small-attempt1.in", "r", stdin);
   freopen("output.txt", "w", stdout);
   int t = read();
   for(int i = 1; i <= t; i ++)
      solve(i);
}

/**
3
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
*/
