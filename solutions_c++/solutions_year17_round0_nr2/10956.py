#include <iostream>
using namespace std;
int main() {
  int tt;
  cin >> tt;
  for (int ii = 1; ii <= tt; ii++) {
    int n;
    cin >> n;

    int i;
    for (i = n; i > 0; i--) {
      int t = i, max = t%10;
      bool ok = true;
      while (t) {
	if (t%10 > max) {
	  ok = false;
	  break;
	} else 
	  max = t%10;
	t /= 10;
      }
      if (ok)
	break;
    }

    cout << "Case #" << ii << ": ";
    cout << i << endl;
  }
  return 0;
}
