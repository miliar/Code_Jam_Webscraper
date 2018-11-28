#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

#define D(x) cout << #x << " " << x << endl

void flipPancakes(string &x, int start, int end) {
  for(int i = start; i < end; ++i) {
    if(x[i] == '-') x[i] = '+';
    else x[i] = '-';
  }
}

int main() {
  int t;
  cin >> t;
  for(int x = 0; x < t; ++x){
    string row;
    int flip;
    cin >> row >> flip;
    bool can = true;
    int limit = row.size() - flip, ans = 0;
    for(int i = 0; i < row.size() && can; ++i) {
      if(i > limit && row[i] == '-') {
        can = false;
        continue;
      }
      if(row[i] == '-') {
        flipPancakes(row, i, i + flip);
        ans++;
      }
    }
    if(can) printf("Case #%d: %d\n", x + 1, ans);
    else printf("Case #%d: IMPOSSIBLE\n", x + 1);
  }
}
