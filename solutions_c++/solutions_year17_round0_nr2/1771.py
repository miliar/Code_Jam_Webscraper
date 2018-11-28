#include <bits/stdc++.h>

using namespace std;

string ans;
string num;

void read_input() {
    cin >> num;
}

void solve() {
  for (int i = num.length() - 2; i >= 0; --i) {
      if (num[i] > num[i + 1]) {
        num[i] = num[i] - 1;
        for (int j = i + 1; j < num.length(); ++j) {
            num[j] = '9';
        }
        if (num[i] < '0') {
            num[i] = '9';
            if (i > 0) num[i - 1] = num[i - 1] - 1;
        }
      }
  }
}

void write_output(int test) {
    while (num[0] == '0') {
        num.erase(0, 1);
    }
    cout << "Case #" << test << ": ";
    cout << num << endl;
}

void clear_data() {
}

int cases;
int main() {
    ios_base::sync_with_stdio(false);

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    cin >> cases;
    for (int test = 1; test <= cases; ++test) {
        read_input();
        solve();
        write_output(test);
        clear_data();
    }
    return 0;
}
