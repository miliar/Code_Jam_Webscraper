#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <fstream>
#include <cstdio>
#include <set>
#include <map>
#include <array>
#include <climits>
#include <unordered_map>
#include <unordered_set>
#include <cstring>
#include <stack>
#include <queue>

using namespace std;


int main() {
  int t;
  cin >> t;

  for (int i_test = 0; i_test < t; ++i_test) {

    string d;
    cin >> d;

    for (int i = d.size() - 2; i >= 0; --i) {
      if (d[i] > d[i + 1]) {
        --d[i];
        for (int j = i + 1; j < d.size(); ++j) d[j] = '9';
      }
    }
    if (d[0] == '0') d.erase(0, 1);

    cout << "Case #" << i_test + 1 << ": " << d << endl;
  }

  return 0;
}
