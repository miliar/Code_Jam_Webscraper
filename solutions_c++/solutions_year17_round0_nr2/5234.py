#include <bits/stdc++.h>
using namespace std;

int i, test, tests;
long long rp[20][10], pw[25], x;

bool check(long long x) {
  vector<int> v;

  while(x) v.push_back(x % 10), x /= 10;

  for(int i = 1; i < v.size(); ++i)
    if(v[i] > v[i - 1]) return 0;

  return 1;
}

void init() {
  for(int i = 1; i < 10; ++i) rp[0][i] = i;

  for(int i = 1; i < 20; ++i)
    for(int j = 1; j < 10; ++j)
      rp[i][j] = rp[i - 1][j] * 10 + j;
  pw[0] = 1;
  for(int i = 1; i < 25; ++i) pw[i] = pw[i - 1] * 10;
}

int brute(int x) {
  while(!check(x)) --x;
  return x;
}

long long solve(long long x) {
  if(x < 1e2) return brute(x);

  long long ans = 0;
  int len = 0, last = 0;
  bool next = 0;
  while(pw[len] * 10 < x) ++len;

  for(int poz = len; poz >= 0; --poz) {
    int who = 9;
    while(who >= last && ans + rp[poz][who] > x) --who;

    if(who <= 0) {
      --len; next = 1;
      break;
    }

    ans += who * pw[poz]; last = who;
  }

  if(!next) return ans;

  ans = 0;
  for(int poz = len; poz >= 0; --poz) {
    int who = 9;
    while(who >= last && ans + rp[poz][who] > x) --who;

    if(who <= 0) {
      --len;
      break;
    }

    ans += who * pw[poz]; last = who;
  }

  return ans;
}

int main() {
  ifstream cin("test.in");
  ofstream cout("test.out");
  ios_base::sync_with_stdio(0);

  cin >> tests; init();
  for(test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";

    cin >> x;
    cout << solve(x) << '\n';
  }

  return 0;
}