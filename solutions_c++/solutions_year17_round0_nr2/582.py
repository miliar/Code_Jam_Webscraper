#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
using namespace std;

typedef pair<int, int> P;
#define rep(i, n) for (int i=0; i<(n); i++)
#define all(c) (c).begin(), (c).end()
#define uniq(c) c.erase(unique(all(c)), (c).end())
#define _1 first
#define _2 second
#define pb push_back
#define INF 1145141919
#define MOD 1000000007

int T;
int A[19], B[19];
long long f() {
  long long x = 0;
  for (int i=18; i>=0; i--) x = 10LL*x + A[i];
  return x;
}

long long solve(long long n) {
  rep(i, 19) A[i] = 0, B[i] = 0;
  for (int i=18; i>=0; i--) {
    for (int j=18; j>i; j--) A[j] = B[j];
    for (int k=1; k<=9; k++) {
      for (int j=i; j>=0; j--) A[j] = k;
      if (f() > n) break;
      B[i] = k;
    }
  }
  rep(i, 19) A[i] = B[i];
  return f();
}

signed main() {
  ios::sync_with_stdio(false); cin.tie(0);
  cin >> T;
  rep(i, T) {
    long long n;
    cin >> n;
    cout << "Case #"<<i+1<<": "<< solve(n) << "\n";
  }
  return 0;
}
