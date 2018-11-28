#include <bits/stdc++.h>
using namespace std;

int main() {
   ios_base::sync_with_stdio(false);
   cin.tie(NULL);

   int t;
   cin >> t;

   int c = 1;

   string number;
   int k;

   while (t > 0) {
      cin >> number >> k;

      cout << "Case #" << c << ": ";
      unsigned int cnt = 0;
      for (unsigned int i = 0; i < number.length(); i++) {
         if (number[i] == '+')
            cnt++;
      }
      if (cnt == number.length())
         cout << 0 << "\n";
      else {
         // when all are not ideal
         cnt = 0;
         for (unsigned int i = 0; i <= number.length() - k; i++) {
            if (number[i] == '-') {
               cnt++;
               for (int j = 0; j < k; j++) {
                  if (i + j < number.length()) {
                     if (number[i + j] == '+')
                        number[i + j] = '-';
                     else
                        number[i + j] = '+';
                  }
               }
            }
         }
         int fl = 0;
         for (unsigned int i = number.length() - k + 1; i < number.length(); i++) {
            if (number[i] != '+') {
               fl = 1;
               break;
            }
         }
         if (fl == 0)
            cout << cnt << "\n";
         else 
            cout << "IMPOSSIBLE\n";
      }
      t--;
      c++;
   }
   return 0;
}
