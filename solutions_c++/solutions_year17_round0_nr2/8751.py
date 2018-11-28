#include <bits/stdc++.h>

using namespace std;

int T, n;

bool ok(int n) {
   int prev = 10;
   while(n) {
      if (n % 10 > prev) return false;
      prev = n % 10;
      n /= 10;
   }

   return true;
}

int main() {
   cin >> T;
   for (int t = 1; t <= T; t++) {
      cin >> n;

      while(!ok(n)) n--;
      cout << "Case #" << t << ": " << n << endl;
   }
}