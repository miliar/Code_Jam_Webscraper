#include <cstdint>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <unordered_set>
#include <string.h>
#include <stack>
#include <cmath>
#include <map>
#include <queue>
#include <bitset>
#include <sstream>
#include <queue>
#include <stdio.h>
#include <stdlib.h>

#define INF 1000000000 
#define all(a) (a).begin(), (a).end()
#define ll long long

#define umap unordered_map
#define vi vector<int>

#define mp make_pair
#define pii pair<int, int>
#define pb push_back

using namespace std;

void
solve(long long n, int cas) {
   if (n == 0) {
      cout << "Case #" << cas + 1 << ": " << n << endl;
      return;
   }
   string res;
   string s = to_string(n);
   int N = s.size();
   int j = N - 1;
   for (; j > 0; --j) {
      if (s[j] - '0' < s[j - 1] - '0')
         break;
   }
   for (int i = N - 1; i > 0; i--) {
      long long curr = s[i] - '0';
      long long next = s[i-1] - '0';
      if (next > curr || curr == 0) {
         res.pb(9 + '0');
          s[i-1] =  (next > 0) ? (next - 1) + '0' : 0;
      } else {
         if (i > j && j != 0) {
            res.pb(9 + '0');
         }
         else {
            res.pb(s[i]);
         }
      }
   }
   if (s[0] - '0' > 0)
      res.pb(s[0]);
   reverse(all(res));
   cout << "Case #" << cas + 1 << ": " << res << endl;
}

int
main() {
   int n = 0;
   cin >> n;
   for (int i = 0; i < n; i++) {
      long long val = 0;
      cin >> val;
      solve(val, i);
   }
   return 0;
}