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

void solve() {
   int r, c;
   string str;
   vector<string> cake;
   cin >> r >> c;
   for (int i = 0; i < r; i++) {
      cin >> str;
      cake.push_back(str);
   }

   char rep = '?';

   for (int i = 0; i < r; i++) {
      rep = '?';
      for (int j = 0; j < c; j++) {
         if (cake[i][j] == '?') {
            cake[i][j] = rep;
         } else {
            rep = cake[i][j];
         }
      }
   }

   for (int i = 0; i < r; i++) {
      rep = '?';
      for (int j = c-1; j >= 0; j--) {
         if (cake[i][j] == '?') {
            cake[i][j] = rep;
         } else {
            rep = cake[i][j];
         }
      }
   }

   string reps = "?";
   for (int i = 0; i < r; i++) {
      if (cake[i][0] == '?') cake[i] = reps;
      else reps = cake[i];
   }

   reps = "?";
   for (int i = r-1; i >= 0; i--) {
      if (cake[i][0] == '?') cake[i] = reps;
      else reps = cake[i];
   }

   for (int i = 0; i < r; i++) cout << cake[i] << endl;
}

int main() {
   int t; int tc = 1;
   cin >> t;
   while (t--) {
      cout << "Case #" << tc++ << ": " << endl;
      solve();
   }
}
