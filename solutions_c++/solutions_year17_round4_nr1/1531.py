
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int tc=1; tc<=T; tc++) {
    int N, P, x;
    cin >> N >> P;
    vector<int> count(4, 0);
    for (int i=0; i<N; i++) {
      cin >> x;
      count[x % P]++;
    }
    int ans = count[0];
    if (P==2) ans += (count[1]+1)/2;
    else if (P==3) {
      ans += min(count[1], count[2]);
      x = (abs(count[1]-count[2])+2)/3;
      ans += x;
    } else if (P==4) {
      ans += min(count[1], count[3]);
      x = abs(count[1] - count[3]);
      count[2] += x/2; 
      ans += (count[2])/2;
      if ((x&1) || (count[2]&1)) ans++;
    } else {
      throw "Wrong number";
    }
    cout << "Case #" << tc << ": " << ans << endl;
  }
}
