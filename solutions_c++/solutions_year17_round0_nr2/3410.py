#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

typedef unsigned long long ull;

void solve(ull n) {
  vector<int> v;

  while (n > 0) {
    v.push_back(n%10);
    n = n / 10;
  }

  for (int i = 1; i < v.size(); ++i) {
    if (v[i] > v[i-1]) {
      v[i]--;
      for (int j = i-1; j >= 0; --j)
        v[j] = 9;
    }
  }

  n = 0;
  for (int i = v.size()-1; i >= 0; --i) {
    n = 10 * n + v[i];
  }

  cout << n;
}

int main() {
  int T;
  cin >> T;
  
  for (int t = 0; t < T; ++t) {
    ull n;
    cin >> n;

    cout << "Case #" << t+1 <<": "; 
    solve(n);
    cout << '\n';
  }

  return 0;
}