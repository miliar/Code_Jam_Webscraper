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
int k, res1, res2;
void rek(int n, int id) {
   priority_queue <pii> q;
   q.push({n, 1});
   while(!q.empty()) {
      pii v = q.top();
      q.pop();
      int ind = v.second, len = v.first;
      if(len & 1) {
         if(id == k) {
            res1 = len / 2;
            res2 = len / 2;
            return;
         }
         id ++;
         q.push({len / 2, ind});
         q.push({len / 2, ind + len / 2 + 1});
      }
      else {
         if(id == k) {
            res1 = len / 2 - 1;
            res2 = len / 2;
            return;
         }
         id ++;
         q.push({len / 2, ind + len / 2});
         q.push({len / 2 - 1, ind});
      }
   }
}
void solve(int test) {
   int n = read();
   k = read();
   rek(n, 1);
   cout << "Case #" << test << ": " << res2 << " " << res1 << endl;
}
main() {
   freopen("C-small-2-attempt0.in", "r", stdin);
   freopen("output.txt", "w", stdout);
   int t = read();
   for(int i = 1; i <= t; i ++)
      solve(i);
}
