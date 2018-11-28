#include <iostream>
#include <string>
#include <queue>

using namespace std;


bool good(int x) {
  int y = 10;
  while (x > 0) {
    int z = x % 10;
    if (z > y) return false;
    y = z;
    x /= 10;
  }
  return true;
}

int main() {
  int tc;
  cin >> tc;
  for (int t = 0; t < tc; ++t) {
    int n;
    cin >> n;
    int k = 0;
    int j = 0;
    while (j < n) {
      j++;
      if (good(j)) k = j;
    }
    cout << "Case #" << t + 1 << ": ";
    cout << k;
    cout << endl;
  }
}
