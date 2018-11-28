#include <bits/stdc++.h>

using namespace std;

int solveTwo(vector<int> tab) {
   int odd = 0;
   for(int x : tab) {
      if(x % 2 == 1) odd++;
   }
   return (tab.size() - odd) + (odd / 2);
}

int solveThree(vector<int> tab) {
   vector<int> modulo(3,0);
   for(int x : tab) modulo[x % 3]++;
   int m = min(modulo[1],modulo[2]);
   int M = max(modulo[1],modulo[2]);
   return modulo[0] + m + ((M - m) / 3);
}

int solveFour(vector<int> tab) {
   vector<int> modulo(4,0);
   for(int x : tab) modulo[x % 4]++;
   int m = min(modulo[1],modulo[3]);
   int M = max(modulo[1],modulo[3]);
   return modulo[0] + m + ((modulo[2] + M - m) / 2);
}

int finalSolveFour(vector<int> tab) {
   vector<vector<vector<vector<int>>>> mat(101,vector<vector<vector<int>>> (101, vector<vector<int>> (101, vector<int> (4,0))));
   for(int i = 0; i <= 100; ++i) {
   for(int j = 0; j <= 100; ++j) {
   for(int k = 0; k <= 100; ++k) {
   for(int l = 0; l < 4; ++l) {
      int ans = 0;
      if(i > 0)
         ans = max(ans, mat[i-1][j][k][(4+l-1) % 4] + (1 == l ? 1 : 0));
      if(j > 0)
         ans = max(ans, mat[i][j-1][k][(4+l-2) % 4] + (2 == l ? 1 : 0));
      if(k > 0)
         ans = max(ans, mat[i][j][k-1][(4+l-3) % 4] + (3 == l ? 1 : 0));
      mat[i][j][k][l] = ans;
   }
   }
   }
   }
   vector<int> modulo(4,0);
   for(int x : tab) modulo[x % 4]++;
   return modulo[0] + mat[modulo[1]][modulo[2]][modulo[3]][(modulo[1] + (2 * modulo[2]) + (3 * modulo[3])) % 4];
}

int finalSolveThree(vector<int> tab) {
   vector<vector<vector<int>>> mat(101, vector<vector<int>> (101, vector<int> (3,0)));
   for(int i = 0; i <= 100; ++i) {
   for(int j = 0; j <= 100; ++j) {
   for(int l = 0; l < 3; ++l) {
      int ans = 0;
      if(i > 0)
         ans = max(ans, mat[i-1][j][(3+l-1) % 3] + (1 == l ? 1 : 0));
      if(j > 0)
         ans = max(ans, mat[i][j-1][(3+l-2) % 3] + (2 == l ? 1 : 0));
      mat[i][j][l] = ans;
   }
   }
   }
   vector<int> modulo(3,0);
   for(int x : tab) modulo[x % 3]++;
   return modulo[0] + mat[modulo[1]][modulo[2]][(modulo[1] + (2 * modulo[2])) % 3];
}


int finalSolveTwo(vector<int> tab) {
   vector<vector<int>> mat(101, vector<int> (2,0));
   for(int i = 0; i <= 100; ++i) {
   for(int l = 0; l < 2; ++l) {
      int ans = 0;
      if(i > 0)
         ans = max(ans, mat[i-1][(2+l-1) % 2] + (1 == l ? 1 : 0));
      mat[i][l] = ans;
   }
   }
   vector<int> modulo(2,0);
   for(int x : tab) modulo[x % 2]++;
   return modulo[0] + mat[modulo[1]][modulo[1] % 2];
}

int main() {
   int T;
   cin >> T;
   for(int test = 1; test <= T; ++test) {
      int N, P;
      cin >> N >> P;
      vector<int> tab(N);
      for(int i = 0; i < N; ++i) cin >> tab[i];
      cout << "Case #" << test << ": ";
      if(P == 2) cout << finalSolveTwo(tab);
      else {
         if(P == 3) cout << finalSolveThree(tab);
         else cout << finalSolveFour(tab);
      }
      cout << endl;
   }
}
