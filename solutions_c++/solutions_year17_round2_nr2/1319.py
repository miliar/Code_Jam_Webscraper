#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct color {
  string name;
  int freq;
  bool operator<(const color &c) const {
    return freq > c.freq;
  }
};

color arr[3];

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int tmp;
    cout << "Case #" << t << ": ";
    cin >> tmp >> arr[0].freq >> tmp >> arr[1].freq >> tmp >> arr[2].freq >> tmp;
    arr[0].name = "R";
    arr[1].name = "Y";
    arr[2].name = "B";
    sort(arr, arr + 3);
    if (arr[0].freq > arr[1].freq + arr[2].freq)
      cout << "IMPOSSIBLE";
    else {
      for (int i = 0; i < arr[0].freq; ++i) {
        cout << arr[0].name;
        if (arr[1].freq > arr[2].freq) {
          cout << arr[1].name;
          arr[1].freq--;
        }
        else {
          cout << arr[2].name;
          arr[2].freq--;
        }
      }
      while (arr[1].freq + arr[2].freq) {
        if (arr[1].freq > arr[2].freq) {
          cout << arr[1].name;
          arr[1].freq--;
        }
        else {
          cout << arr[2].name;
          arr[2].freq--;
        }
      }
    }
    cout << endl;
  }
  return 0;
}