#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <queue>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

vector<int> processDis(int n, int k)
{
  vector<int> result(2, 0);
  int sideA = n/2;
  int sideB = n - 1 - n/2;
  if (k == 1) {
    result[0] = sideA;
    result[1] = sideB;
    return result;
  }
  priority_queue<int> spotPicker;
  spotPicker.push(sideA);
  spotPicker.push(sideB);
  for (int i = 1; i < k; i++) {
    int side = spotPicker.top();
    spotPicker.pop();
    if (side == 1) {
      return vector<int>(2, 0);
    }
    sideA = side/2;
    sideB = side - 1 - side/2;
    spotPicker.push(sideA);
    spotPicker.push(sideB);
  }

  result[0] = sideA;
  result[1] = sideB;
  return result;
}

int main() {
  int t, n, k;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; i++) {
    cin >> n;
    cin >> k;  // read n and then m.
    vector<int> result = processDis(n, k);
    int max = result[0] > result[1] ? result[0] : result[1];
    int min = result[0] < result[1] ? result[0] : result[1];
    cout << "Case #" << i << ": " << max << " " << min << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}