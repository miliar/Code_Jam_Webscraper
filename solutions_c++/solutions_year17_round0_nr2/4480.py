#include<iostream>
using namespace std;

int main() {
   int t, x, d[20], i, j, p, k, large;
   long long int n, nn, y;
   cin >> t;
   for (x = 1; x <= t; x++) {
      cin >> n;
      k = 0;
      nn = n;
      while (nn > 0) {
         d[k] = nn%10;
         k++;
         nn /= 10;
      }
      j = k-1;
      while (j-1 >= 0 && d[j] <= d[j-1])
         j--;
      y = 0;
      large = d[j];
      for (p = k-1; d[p] != large; p--) ;
      for (i = k-1; i >= 0; i--) {
         if (j > 0 && i == p) {
            y = y*10 + d[i] - 1;
            i--;
            while (i >= 0) {
               y = y*10 + 9;
               i--;
            }
         }
         else
            y = y*10 + d[i];
      }
      cout << "Case #" << x << ": " << y << endl;
   }
   return 0;
}
