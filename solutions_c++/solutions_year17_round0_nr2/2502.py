#include <iostream>
#include <string>
#include <vector>
#define ll long long
using namespace std;
bool work(ll &n) {
  vector<int> a;
  ll n1 = n;
  while (n1) {
    a.push_back(n1 % 10);
    n1 /= 10;
  }
  for (int i = 0; i < a.size() - 1; i++) {
    if (a[i] < a[i + 1] || a[i] == 0) {
      a[i] = 9;
      int idx = i + 1;
      a[idx]--;
      while (idx < a.size() && a[idx] < 0) {
        a[idx] = 9;
        idx++;
        a[idx]--;
      }
      for (int j = 0; j < i; j++) {
        a[j] = 9;
      }
      break;
    }
  }
  ll now = 1, res = 0;
  bool flag = true;
  for (int i = 0; i < a.size(); i++) {
    res += now * a[i];
    now *= 10;
    if (i < a.size() - 1 && a[i] < a[i + 1]) {
      flag = false;
    }
  }
  n = res;
  return flag;
}
bool ordered(ll n) {
  vector<int> a;
  ll n1 = n;
  while (n1) {
    a.push_back(n1 % 10);
    n1 /= 10;
  }
  for (int i = 0; i < a.size() - 1; i++) {
    if (a[i] < a[i + 1]) {
      return false;
    }
  }
  return true;
}
int main() {
  int tk;
  cin >> tk;
  for (int tk1 = 1; tk1 <= tk; tk1++) {
    ll n;
    cin >> n;
    bool finished = false;
    do {
      finished = work(n);
    } while (!finished);
    // while (!ordered(n)) {
    //   n--;
    // }
    cout << "Case #" << tk1 << ": ";
    cout << n << endl;
  }
  return 0;
}
