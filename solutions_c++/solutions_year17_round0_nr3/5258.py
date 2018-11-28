#include <iostream>
#include <set>

using namespace std;

int main() {
  int count;
  cin >> count;
  for (int i = 1; i <= count; ++i) {
    int n;
    int k;
    cin >> n;
    cin >> k;
    multiset<int, std::greater<int> > spaces;
    spaces.insert(n);
    int left;
    int right;
    for (;k >= 1; k--) {
      auto last = spaces.begin();
      int max = *last;
      left = (max - 1) / 2;
      right = max / 2;
      spaces.erase(last);
      spaces.insert(left);
      spaces.insert(right);
    }
    cout << "Case #" << i << ": " << right << " " << left << endl;
  }
  return 0;
}

