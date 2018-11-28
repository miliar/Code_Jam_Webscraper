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
solve(string s, int k, int cas) {
   int a = 0;
   int n = s.size();

   string sa = s;
   bool left= true;
   for (int i = 0; i < n; i++) {
      if (sa[i] == '-') {//flip
         a++;
         if (i + k > n) break;
         for (int j = i; j < min(n, (i + k)); j++) {
            sa[j] = (sa[j] == '+') ? '-' : '+';
         }
      }
   }
   for (int i = 0; i < s.size(); i++) {
      if (sa[i] == '-') {
         left = false; a = INF;
         break;
//         cout << "Case #" << cas + 1 << ": " << "IMPOSSIBLE" << endl;
//         return; break;
      }
   }

   string sb = s;
   bool right = true;
   int b = 0;
   for (int i = n -1 ; i >= 0; i--) {
      if (sb[i] == '-') {//flip
         b++;
         if (i - k < 0) break;
         for (int j = i; j > max(0, i - k) ; j--) {
            sb[j] = (sb[j] == '+') ? '-' : '+';
         }
      }
   }
   for (int i = 0; i < s.size(); i++) {
      if (sb[i] == '-') {
         right = false; b = INF;
         break;
//         cout << "Case #" << cas + 1 << ": " << "IMPOSSIBLE" << endl;
//         return; break;
      }
   }

   if (!left && !right) {
      cout << "Case #" << cas + 1 << ": " << "IMPOSSIBLE" << endl;
   } else {
      cout << "Case #" << cas + 1 << ": " << min(a, b) << endl;
   }
}

int
main() {
   int n = 0;
   cin >> n;
   for (int i = 0; i < n; i++) {
      string s;
      cin >> s;
      int k = 0;
      cin >> k;
      solve(s, k, i);
   }
   return 0;
}