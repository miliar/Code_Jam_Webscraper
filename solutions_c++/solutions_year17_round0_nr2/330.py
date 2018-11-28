#include <bits/stdc++.h>

using namespace std;

int main() {
   int t, k;
   cin >> t;
   for(int i = 1; i <= t; ++i) {
      string x;
      bool flag = true;
      cin >> x;
      cout << "Case #" << i << ": ";
      for(int j = 1; j < x.size() && flag; ++j) {
         if(x[j] < x[j-1]) {
            flag = false;
            if(x[j-1] == '1') for(k=1;k < x.size();++k)
               cout << 9;
            else {
               for(k = j; k > 0 && x[k] <= x[k-1]; k--);
               x[k++]--;
               for(;k < x.size();++k) x[k] = '9';
               cout << x;
            }
         }
      }
      if(flag) cout << x;
      cout << endl;
   }
}
