#include <iostream>
#include <queue>
#include <list>

using namespace std;

typedef unsigned long long ull;

int main() {
  int t;
  cin >> t;
  int cas = 0;
  while(t--) {
    ++cas;
    cout << "Case #" << cas << ": ";
    ull n, k;
    cin >> n >> k;
    ull piece1 = n, piece2 = n, pieces = 1, change = 0;
    while(k > pieces) {
      // cout << pieces << " " << k << " " << change << " " << piece1 << " " << piece2 << endl;
      k -= pieces;
      pieces *= 2;
      change *= 2;
      change = piece1%2 == 0 ? pieces - (pieces - change)/2 : change/2;
      ull piece = piece1%2 ? piece2 : piece1;
      piece -= 1;
      piece1 = piece/2;
      piece2 = piece1 + piece%2;
    }
    // cout << pieces << " " << k << " " << change << " " << piece1 << " " << piece2 << endl;
    ull piece;
    if(k <= change) piece = piece2;
    else piece = piece1;
    piece -= 1;
    cout << (piece/2 + piece%2) << " " << (piece/2) << endl;
  }
  return 0;
};
