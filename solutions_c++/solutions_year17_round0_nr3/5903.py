#include <iostream>
using namespace std;

int main() {
  int t;
  int n;
  int k;
  int y;
  int z;
  int currStall;
  cin >> t;

  for (int p = 1; p <= t; ++p) {
    cin >> n >> k;
    int stalls[n+2];
    int ls[n+2];
    int rs[n+2];
    stalls[0] = 1;
    stalls[n+1] = 1;
    ls[0] = 0;
    rs[0] = 0;
    ls[n+1] = 0;
    rs[n+1] = 0;
    for(int i=1; i< n+1; i++) {
      stalls[i] = 0;
      ls[i] = i-1;
      rs[i] = n-i;
    }

    for (int i=0; i<k; i++) {
      currStall = 0;
      for (int j=0; j<n+2; j++) {
        if (stalls[j] == 0) {
          if (min(ls[j], rs[j]) > min(ls[currStall], rs[currStall])) {
            currStall = j;
          } else if (min(ls[j], rs[j]) == min(ls[currStall], rs[currStall]) &&
            max(ls[j], rs[j]) > max(ls[currStall], rs[currStall])) {
            currStall = j;
          }
        }
      }

      y = max(ls[currStall], rs[currStall]);
      z = min(ls[currStall], rs[currStall]);

      stalls[currStall] = 1;
      int m = currStall - 1;
      int j = currStall + 1;
      int counter = 0;
      while (stalls[m] == 0) {
        rs[m] = counter;
        m--;
        counter ++;
      }
      counter = 0;
      while (stalls[j] == 0) {
        ls[j] = counter;
        j++;
        counter ++;
      }

    }

    cout << "Case #" << p << ": " << y << " " << z << endl;
  }

  return 0;
}