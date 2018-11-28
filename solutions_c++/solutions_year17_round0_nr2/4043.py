#include<iostream>
#include<vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    long n;
    cin >> n;
    vector<int> v;
    long x = n;
    while (x != 0) {
      v.insert(v.begin(), x % 10);
      x /= 10;
    }
    for (int i = 0; i < v.size() - 1; i++) {
      if (v[i] > v[i + 1]) {
        bool carry = true;
        int j = i;
        while (carry && j > 0) {
          v[j]--;
          if (j != 0) {
            if (v[j] < v[j - 1]) {
              v[j] = 9;
            } else {
              carry = false;
            }
          }
          j--;
        }
        if (carry) {
          v[0]--;
        }
        for (int j = i + 1; j < v.size(); j++) {
          v[j] = 9;
        }
      }
    }
    long r = 0;
    for (int i = 0; i < v.size(); i++) {
      r *= 10;
      r += v[i];
    }
    cout << "Case #" << t << ": " << r << endl;
  }
}
