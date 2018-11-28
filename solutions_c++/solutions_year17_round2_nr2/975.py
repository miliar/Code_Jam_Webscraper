#include <bits/stdc++.h>

using namespace std;

bool not_ok(char a, char b) {
   if(a == 'V') return b != 'Y';
   if(a == 'G') return b != 'R';
   if(a == 'O') return b != 'B';
   if(b == 'V') return a != 'Y';
   if(b == 'G') return a != 'R';
   if(b == 'O') return a != 'B';
   return (a == b);
}

bool is_ok(string s) {
   int n = s.size();
   for(int i = 0; i < n; ++i) {
      char a = s[i];
      char b = s[(i+1) % n];
      if(not_ok(a,b)) return false;
   }
   return true;
}

int main() {
   int T;
   cin >> T;
   for(int test = 1; test <= T; ++test) {
      int N, R, O, Y, G, B, V;
      cin >> N >> R >> O >> Y >> G >> B >> V;
      vector<vector<char>> tabR;
      vector<vector<char>> tabY;
      vector<vector<char>> tabB;
      if((R + Y == 0) || (B + R == 0) || (B + Y == 0)) {
         while(R > 0) {
            vector<char> tabtab;
            while(G > 0 && R > 0) {
               tabtab.push_back('G');
               tabtab.push_back('R');
               G--;
               R--;
            }
            tabR.push_back(tabtab);
      while(R > 0) {
         vector<char> tabtabtab = {'R'};
         R--;
         tabR.push_back(tabtabtab);
      }
         }
         while(Y > 0) {
            vector<char> tabtab;
            while(Y > 0 && V > 0) {
               tabtab.push_back('V');
               tabtab.push_back('Y');
               V--;
               Y--;
            }
            tabY.push_back(tabtab);
      while(Y > 0) {
         vector<char> tabtabtab = {'Y'};
         Y--;
         tabY.push_back(tabtabtab);
      }
         }
         while(B > 0) {
            vector<char> tabtab;
            while(O > 0 && B > 0) {
               tabtab.push_back('O');
               tabtab.push_back('B');
               O--;
               B--;
            }
            tabB.push_back(tabtab);
            while(B > 0) {
               vector<char> tabtabtab = {'B'};
               B--;
               tabB.push_back(tabtabtab);
            }
         }

      }
      else {
      while(R > 0) {
         vector<char> tabtab = {'R'};
         R--;
         while(G > 0 && R > 0) {
            tabtab.push_back('G');
            tabtab.push_back('R');
            G--;
            R--;
         }
         tabR.push_back(tabtab);
      }
      while(Y > 0) {
         vector<char> tabtab = {'Y'};
         Y--;
         while(Y > 0 && V > 0) {
            tabtab.push_back('V');
            tabtab.push_back('Y');
            V--;
            Y--;
         }
         tabY.push_back(tabtab);
      }
      while(B > 0) {
         vector<char> tabtab = {'B'};
         B--;
         while(O > 0 && B > 0) {
            tabtab.push_back('O');
            tabtab.push_back('B');
            O--;
            B--;
         }
         tabB.push_back(tabtab);
      }
/*      int M = tab.size();
      int tar = (M+1) / 2;
      int j = 0;
      for(int i = 0; i < tar; ++i) {
         vector<char> tabtab = tab[i];
         for(int k = 0; k < tabtab.size(); ++k) {
            ans[j] = tabtab[k];
            j++;
         }
         if(i + tar < M) {
            vector<char> tabtabtab = tab[i + tar];
            for(int k = 0; k < tabtabtab.size(); ++k) {
               ans[j] = tabtabtab[k];
               j++;
            }
         }
      }
*/
      }
      string ans (N,'e');
      int j = 0;
      char last = 'X';
      char first = 'X';
      int iR = tabR.size() - 1, iB = tabB.size() - 1, iY = tabY.size() - 1;
      if(iR >= iB && iR >= iY) {
         first = 'R';
         last = 'R';
         vector<char> tabtab = tabR[iR];
         for(int k = 0; k < tabtab.size(); ++k) {
            ans[j] = tabtab[k];
            j++;
         }
         iR--;
      }
      else if(iB >= iR && iB >= iY) {
         first = 'B';
         last = 'B';
         vector<char> tabtab = tabB[iB];
         for(int k = 0; k < tabtab.size(); ++k) {
            ans[j] = tabtab[k];
            j++;
         }
         iB--;
}
      else {
         first = 'Y';
         last = 'Y';
         vector<char> tabtab = tabY[iY];
         for(int k = 0; k < tabtab.size(); ++k) {
            ans[j] = tabtab[k];
            j++;
         }
         iY--;
      }
      while(iR + iB + iY + 3 > 0) {
         if(last == 'R' && (iB > iY || (iB == iY && 'B' == first))) {
            if(iB < 0) break;
            vector<char> tabtab = tabB[iB];
            for(int k = 0; k < tabtab.size(); ++k) {
               ans[j] = tabtab[k];
               j++;
            }
            iB--;
         }
         else if(last == 'R')  {
            if(iY < 0) break;
            vector<char> tabtab = tabY[iY];
            for(int k = 0; k < tabtab.size(); ++k) {
               ans[j] = tabtab[k];
               j++;
            }
            iY--;
         }
         if(last == 'B' && (iR > iY || (iR == iY && 'R' == first))) {
            if(iR < 0) break;
            vector<char> tabtab = tabR[iR];
            for(int k = 0; k < tabtab.size(); ++k) {
               ans[j] = tabtab[k];
               j++;
            }
            iR--;
         }
         else if(last == 'B') {
            if(iY < 0) break;
            vector<char> tabtab = tabY[iY];
            for(int k = 0; k < tabtab.size(); ++k) {
               ans[j] = tabtab[k];
               j++;
            }
            iY--;
         }
         if(last == 'Y' && (iB > iR || (iB == iR && 'B' == first))) {
            if(iB < 0) break;
            vector<char> tabtab = tabB[iB];
            for(int k = 0; k < tabtab.size(); ++k) {
               ans[j] = tabtab[k];
               j++;
            }
            iB--;
         }
         else if(last == 'Y') {
            if(iR < 0) break;
            vector<char> tabtab = tabR[iR];
            for(int k = 0; k < tabtab.size(); ++k) {
               ans[j] = tabtab[k];
               j++;
            }
            iR--;
         }
         last = ans[j - 1];     
      }
      cout << "Case #" << test << ": ";
      if(j < N) cout << "IMPOSSIBLE" << endl;
      else if(is_ok(ans)) cout << ans << endl;
      else cout << "IMPOSSIBLE" << endl;
   }
}
