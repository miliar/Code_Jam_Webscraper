#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <list>

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " << 

using namespace std;

long long solve(long long n, long long k) {
  map<long long, long long> x;
  x[n] = 1;
  long long last = -1;
  while (k > 0) {
    long long m = x.rbegin()->first;
    long long cnt = x.rbegin()->second;
    x.erase(m);
    last = m;
    long long a = m/2;
    long long b = (m-1)-a;
    // TRACE(m _ a _ b);
    long long delta = min(k, cnt);
    x[a] += delta;
    x[b] += delta;
    k -= delta;
  }
  return last;
}

int main() {
  int t;
  cin >> t;
  for (int tt=0; tt<t; tt++) {
    long long n, k;
    cin >> n >> k;
    long long s = solve(n, k);
    long long a = s/2;
    long long b = (s-1)-a;
    cout << "Case #" << tt+1 << ": " << a << " " << b << endl;
  }
  return 0;
}
