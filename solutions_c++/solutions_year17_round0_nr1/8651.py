#include<bits/stdc++.h>

using namespace std;

string s;
int k, T;


int main() {
   cin >> T;
   for (int t = 1; t <= T; t++) {
      cin >> s >> k;

      int counter = 0;
      for (int i = 0; i < s.size(); i++) {
         if (s[i] == '-' && i + k - 1 < s.size()) {
            counter++;
            for (int j = 0; j < k; j++) {
               if (s[i + j] == '-')
                  s[i + j] = '+';
               else
                  s[i + j] = '-';
            }
         }
      }

      bool ok = true;
      for (int i = 0; i < s.size(); i++) {
         if (s[i] == '-')
            ok = false;
      }

      if (ok)
         cout << "Case #" << t << ": " << counter << endl;
      else
         cout << "Case #" << t << ": IMPOSSIBLE" << endl;
   }

   return 0;
}