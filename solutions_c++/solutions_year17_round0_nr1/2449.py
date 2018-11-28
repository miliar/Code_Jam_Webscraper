#include<iostream>
#include<cstdio>

using namespace std;


int main(){
  ios_base::sync_with_stdio(true);
  int t; cin >> t;
  for (int caseIdx = 1; caseIdx <= t; caseIdx ++) {
    int n; string s; cin >> s; n = s.length();
    int k; cin >> k;
    int changes[1000]; int changeCount = 0; int changesMade = 0;
    for (int j = 0; j < k; j++) changes[j] = 0;
    bool wrong = false;
    for (int i = 0; i < n; i++) {
      int side;
      if (s[i] == '+') {
        side = 1;
      } else if (s[i] == '-'){
        side = 0;
      }
      side = (side + changeCount) % 2;
      int pos = i % (k-1);
      // pos == 0, side == 0 -> pos = 1, changeCount ++
      // pos == 0, side == 1 -> pos = 0, 
      // pos == 1, side == 0 -> pos = 1, 
      // pos == 1, side == 1 -> pos = 0, changeCount -- / ++
      if (changes[pos] == side) changeCount = (changeCount+1) % 2;
      if (side == 0) {
        if (n-i < k) {
          cout << "Case #" << caseIdx << ": IMPOSSIBLE\n";
          wrong = true;
          break;
        }
        changesMade ++;
        changes[pos] = 1;
      } else {
        changes[pos] = 0;
      }
    }
    if (!wrong) {
      cout << "Case #" << caseIdx <<": " << changesMade <<"\n";
    }
  }

}
