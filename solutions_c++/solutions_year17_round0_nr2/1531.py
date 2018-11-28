#include <bits/stdc++.h>
using namespace std;

vector<int> to_digits(long long x) {
  vector<int> d;
  while (x) {
    d.push_back(x % 10);
    x /= 10;
  }
  reverse(d.begin(), d.end());
  return d;
}

long long to_number(const vector<int>& d) {
  long long num = 0;
  for (int x : d) {
    num *= 10;
    num += x;
  }
  return num;
}

bool cmp(const vector<int>& d1, const vector<int>& d2) {
  if (d1.size() != d2.size()) {
    return d1.size() < d2.size();
  }
  for (int i = 0; i < d1.size(); ++i) {
    if (d1[i] != d2[i]) {
      return d1[i] < d2[i];
    }
  }
  return false;
}

int T;
long long N;

long long solve() {
  cin >> N;
  vector<int> dN = to_digits(N);  
  vector<int> best;
  for (int len = 1; len <= dN.size(); ++len) {
    if (len < dN.size()) {
      vector<int> cur(len, 9);
      if (cmp(best, cur)) {
        best = cur;
      }
      continue;
    }

    vector<int> cur;
    for (int i = 0; i < dN.size(); ++i) {
      for (int j = 0; j < dN[i]; ++j) {
        vector<int> next = cur;
        if (!(cur.empty() || cur.back() <= j)) {
          continue;
        }
        next.push_back(j);
        while (next.size() != dN.size()) {
          next.push_back(9);
        }
        if (cmp(best, next)) {
          best = next;
        }
      }
      if (cur.empty() || cur.back() <= dN[i]) {
        cur.push_back(dN[i]);
      } else {
        break;
      }
    }
    if (cmp(best, cur)) {
      best = cur;
    }
  }
  return to_number(best);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> T;
  for (int test = 1; test <= T; ++test) {
    cout << "Case #" << test << ": " << solve() << endl;
  }
}
