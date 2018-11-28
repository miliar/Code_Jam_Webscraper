#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;


int main() {
  int t, n, k;
  cin >> t;

  for (int i = 1; i <= t; i++) {
    cin >> n;
    cin >> k;

    vector<int> lengths;
    make_heap(lengths.begin(), lengths.end());
    int y, z;

    lengths.push_back(n);
    push_heap(lengths.begin(), lengths.end());

    for (int j = 0; j < k; j++) {
      int maxLength = lengths.front();
      pop_heap(lengths.begin(),lengths.end());
      lengths.pop_back();

      z = maxLength / 2 - (1 - maxLength % 2);
      y = maxLength - z - 1;

      if (z > 0) {
        lengths.push_back(z);
        push_heap(lengths.begin(), lengths.end());
      }
      if (y > 0) {
        lengths.push_back(y);
        push_heap(lengths.begin(), lengths.end());
      }
    }

    // if (k > n / 2 + sqrt(n / 2)) {
    //   y = 0;
    //   z = 0;
    // } else {
    //   for (int j = 0; j < k; j++) {
    //     int maxLength = lengths.front();
    //     pop_heap(lengths.begin(),lengths.end());
    //     lengths.pop_back();
    //
    //     z = maxLength / 2 - (1 - maxLength % 2);
    //     y = maxLength - z - 1;
    //
    //     if (z > 0) {
    //       lengths.push_back(z);
    //       push_heap(lengths.begin(), lengths.end());
    //     }
    //     if (y > 0) {
    //       lengths.push_back(y);
    //       push_heap(lengths.begin(), lengths.end());
    //     }
    //   }
    // }

    cout << "Case #" << i << ": " << y << " " << z << endl;
  }

  return 0;
}
