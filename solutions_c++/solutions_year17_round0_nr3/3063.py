#include <bits/stdc++.h>

using namespace std;

void solve() {
  long long n;
  long long k;
  cin >> n >> k;
  long long ind = k;
  int l = 0;
  while(ind!=1) {
    ind = ind / 2;
    l++;
  }
  long long a = n / 2;
  long long b = (n - 1) / 2;
  long long count_a = 1;
  long long count_b = 1;
  long long a1;
  long long a2;
  long long b1;
  long long b2;
  long long counter = 2;
  for(int i = l-2; i >= 0; i--) {
    a1 = a / 2; a2 = (a-1) / 2;
    b1 = b / 2; b2 = (b-1) / 2;
    if(a1==a2&&a1==b1&&b1==b2) {
      count_a = count_a * 2;
      count_b = count_b * 2;
    } else if(a1==a2&&a1==b1) {
      count_a = count_a * 2 + count_b;
    } else if(a1==b1) {
      count_a = count_a + count_b;
      count_b = count_a;
    } else {
      count_b = count_b * 2 + count_a;
    }
    a = a1; b = b2;
    counter = counter * 2;
  }
  if (k==1) {
    cout << n / 2 << " " << (n - 1) / 2;
  } else  if (k <= (counter - 1 + count_a)) {
    cout << a / 2 << " " << (a - 1) / 2;
  } else {
    cout << b / 2 << " " << (b - 1) / 2;
  }
}

int main() {
  int t; cin >> t;
  for(int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}
