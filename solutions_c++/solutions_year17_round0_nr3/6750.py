#include <bits/stdc++.h>

using namespace std;

int T;
int N, K;
bitset<1000002> rooms;
int kthLeft, kthRight;

int main() {
   cin >> T;
   for (int t = 1; t <= T; t++) {
      cin >> N >> K;

      rooms.reset();
      rooms[1] = true;
      rooms[N + 2] = true;


      for (int i = 1; i <= K; i++) {
         int bestPosition;
         int bestDiff = -1, bestDiff2 = -1;;
         kthLeft = kthRight = 0;
         for (int j = 1; j <= N + 2; j++) {
            if (rooms[j] == false) {
               int left, right;
               left = right = 0;
               for (int k = j - 1; k >= 1; k--) {
                  if (rooms[k] == true) {
                     left = j - k - 1;
                     break;
                  }
               }

               for (int k = j + 1; k <= N + 2; k++) {
                  if (rooms[k] == true) {
                     right = k - j - 1;
                     break;
                  }
               }
               int minDiff = min(left, right);
               if (minDiff > bestDiff) {
                  bestDiff = minDiff;
                  bestPosition = j;
                  kthLeft = left;
                  kthRight = right;
                  bestDiff2 = max(left, right);
               }
               else if (minDiff == bestDiff) {
                  int maxDiff = max(left, right);
                  if (bestDiff2 < maxDiff) {
                     bestDiff2 = maxDiff;
                     bestPosition = j;
                     kthLeft = left;
                     kthRight = right;
                  }
               }

               // cout << j << " " << left << " " << right << " " << minDiff << " "  << bestDiff << endl;
            }
         }
// cout << "Best position = " << bestPosition << endl;
         rooms[bestPosition] = true;
         // cout << bestPosition << " ";
      }
      // cout << endl;
      cout << "Case #" << t << ": " << max(kthLeft, kthRight) << " " << min(kthRight, kthLeft) << endl;
   }


   return 0;
}