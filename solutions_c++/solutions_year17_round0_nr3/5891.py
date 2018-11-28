#include <iostream>
#include <bitset>
#include <list>
#include <functional>

using namespace std;

int
msb_position(long n) {
  int pos = -1;
  if(n > 0) {
    int left = sizeof(long)*8;
    int right = -1;

    while(left > right) {
      int mid = (left+right)/2;
      long test = 1L << mid;

      if(n < test) {
        left = mid;
      } else {
        right = mid+1;
      }
    }
    pos = left-1;
  }

  return pos;
}

int
main() {
  int T;

  cin >> T;

  for(int c = 1; c <= T; c++) {
    long N, K;

    cin >> N >> K;
    list<int> ns;
    int y = 0, z = 0;

    while((K > 0) && (N > 0)) {
      K--;
      y = N/2;
      z = N/2-(1-N%2);
      ns.push_back(N/2);
      ns.push_back(N/2-(1-N%2));
      ns.sort(greater<int>());
      N = ns.front();
      ns.pop_front();
    }

    if(N == 0) {
      y = 0;
      z = 0;
    }

    cout << "Case #" << c << ": " << y << " " << z << endl;
  }
}
