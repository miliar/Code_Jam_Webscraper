#include <iostream>
#include <bitset>
#include <vector>

using namespace std;

typedef vector<int > vi;

vi to_digits(long x) {
  vi xs;
  while (x > 0) {
    xs.insert(xs.begin(), (int)(x % 10));
    x /= 10;
  }
  return xs;
}

vi iter(vi xs, bool &changed) {
  for (int i = 0; i < xs.size() - 1; i++) {
    if (xs[i] > xs[i+1]) {
      xs[i] -= 1;
      for (int j = i+1; j < xs.size(); j++) {
        xs[j] = 9;
      }

      changed = 1;
      return xs;
    }
  }

  changed = 0;
  return xs;
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {

    long x;
    cin >> x;
    vi xs = to_digits(x);
    bool changed = 1;
    while (changed) {
      xs = iter(xs, changed);
    }

    cout << "Case #" << (t + 1) << ": ";
    int k = 0;
    while (xs[k] == 0) k++;
    for (; k < xs.size(); k++) {
      cout << xs[k];
    }
    cout << endl;
  }

  return 0;
}
