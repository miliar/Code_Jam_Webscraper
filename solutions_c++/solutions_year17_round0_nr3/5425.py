#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <bitset>

// only for small input
using namespace std;

bitset<1000008> bath;

void answer(int n, int k){
   bath = 0;
   int mi, ma, ls, lr, macc, mac, i, poz;
   bath[0] = bath[n+1] = 1;
   while (k > 0){
      macc = -1;
      mac = -1;
      for (int x = 1; x <= n; x++)
      if (bath[x] == 0){
         ls = 0;
         i = x-1;
         while (bath[i] == 0) i--, ls++;
         lr = 0;
         i = x+1;
         while (bath[i] == 0) i++, lr++;
         mi = min(ls, lr);
         ma = max(ls, lr);
         if (mi > mac){
            mac = mi;
            macc = ma;
            poz = x;
         }
         else if (mi == mac){
            if (ma > macc){
               mac = mi;
               macc = ma;
               poz = x;
            }
         }
      }
      bath[poz] = 1;
      k--;
   }
   cout << macc << " " << mac;
}

int main()
{
   freopen("data.in", "r", stdin);
   freopen("data.out", "w", stdout);
   int T, n, k;
   cin >> T;
   for (int i = 1; i <= T; i++){
      cin >> n >> k;
      cout << "Case #" << i << ": ";
      answer(n, k);
      cout << "\n";
   }


   return 0;
}
