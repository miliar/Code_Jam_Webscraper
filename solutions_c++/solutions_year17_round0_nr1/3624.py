#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <cmath>
#include <map>
#include <set>
#define MOD 1000000007
using namespace std;


int main() {
   int t; int tc = 1;
   cin >> t;
   while (t--) {
      string s;
      int k;
      cin >> s;
      cin >> k;
      int ans = 0;

      for (int i = 0; i < (int)s.size() - k + 1; i++) {
         if (s[i] == '-') {
            for (int j = 0; j < k; j++) {
               if (s[i+j] == '-') s[i+j] = '+';
               else s[i+j] = '-';
            }
            ans++;
         }
      }

      bool isHappy = true;
      for (int i = 0; i < (int)s.size(); i++) {
         if (s[i] == '-') isHappy = false;
      }

      cout << "Case #" << tc++ << ": ";
      if (isHappy) cout << ans << endl;
      else cout << "IMPOSSIBLE" << endl;
   }
}
