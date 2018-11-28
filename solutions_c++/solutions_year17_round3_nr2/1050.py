#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int a, b;
    int arr[4];
    cin >> a >> b;
    for (int i = 0; i < 2 * (a + b); ++i)
      cin >> arr[i];
    sort(arr, arr + 2 * (a + b));
    cout << "Case #" << t << ": ";
    if (a != 2 && b != 2)
      cout << 2 << endl;
    else {
      int l1 = arr[3] - arr[0];
      int l2 = 1440 - (arr[2] - arr[1]);
      if (l1 > 720 && l2 > 720)
        cout << 4 << endl;
      else
        cout << 2 << endl;
    }
  }
  return 0;
}