#include <iostream>
#include <vector>

using namespace std;

long long compute(long long value) {
  if (value < 10) {
    return value;
  }

  // Value is guaranteed to have two digits at least
  long long res = value;
  vector<int> a;

  while (value != 0) {
    a.emplace_back(value % 10);
    value /= 10;
  }

  reverse(a.begin(), a.end());
  bool check = true;
  for (int i = 0; i < a.size() - 1; ++i) {
    check = check & (a[i] <= a[i + 1]);
    if (!check) {
      break;
    }
  }

  if (check) {
    return res;
  } else {
    res = 0;
  }

  // cout << "HERE" << endl;
  bool found = false;
  int id = 0;
  for (int i = 0; i < a.size() - 1; ++i) {
    if (a[i] > a[i + 1])  {
      found = true;
      a[id] = a[id] - 1;
      for (int j = id + 1; j < a.size(); ++j) {
        a[j] = 9;
      }
      break;
    } else if (a[i] < a[i + 1]) {
      id = i + 1;
    }
  }

  // cout << "CHECK" << endl;
  int m = a.size();

  if (!found) {
    if (a[0] == 1) {
      // Lose a digit
      --m;
      for (int i = 0; i < m; ++i) {
        a[i] = 9;
      }
    } else {
      a[0] = a[0] - 1;
      for (int i = 1; i < m; ++i) {
        a[i] = 9;
      }
    }
  }

  for (int i = 0; i < m; ++i) {
    res = res * 10 + a[i];
  }

  return res;
}

int main () {
  // freopen("input.txt", "r", stdin);
  // freopen("output.txt", "w", stdout);
  int t;
  int cnt = 0;

  cin >> t;

  while (t > 0) {
    --t;
    ++cnt;
    long long val;
    cin >> val;
    cout << "Case #" << cnt << ": " << compute(val) << endl;
  }

  return 0;
}
