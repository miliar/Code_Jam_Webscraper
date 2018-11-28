#include <bits/stdc++.h>
using namespace std;

int i, x, y, n, p, rs, freq[10], gmb;
vector<int> a;

int solve3(int fq1, int fq2, int now = 0) {
  if(!fq1 && !fq2) return 0;

  if(!now) {
    if(fq1) return 1 + solve3(fq1 - 1, fq2, 1);
    else return 1 + solve3(fq1, fq2 - 1, 2);
  }

  if(now == 1) {
    if(fq2) return solve3(fq1, fq2 - 1, 0);
    else return solve3(fq1 - 1, fq2, 2);
  }

  if(fq1) return solve3(fq1 - 1, fq2, 0);
  return solve3(fq1, fq2 - 1, 1);
}

int solve4(int f1, int f2, int f3, int now = 0) {
  return 0;
}

int main() {
  ifstream cin("file.in");
  ofstream cout("file.out");
  ios_base::sync_with_stdio(0);

  int test, tests;
  cin >> tests;
  for(test = 1; test <= tests; ++test) {
    cout << "Case #"<< test << ": ";
    memset(freq, 0, sizeof(freq));

    cin >> n >> p; a.clear(); rs = 0;
    for(i = 0; i < n; ++i) {
      cin >> x;
      if(x % p == 0) {
        ++rs;
        continue;
      }

      a.push_back(x);
      ++freq[x % p];
    }

    if(p == 2) {
      rs += (a.size() - 1) / 2 + 1;
      cout << rs << '\n';
      continue;
    }

    if(p == 3) {
      cout << rs + solve3(freq[1], freq[2]) << '\n';
      continue;
    }
  }

  return 0;
}