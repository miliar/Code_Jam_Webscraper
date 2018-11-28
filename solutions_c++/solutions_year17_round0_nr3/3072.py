#include <iostream>
#include <ctime>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <cctype>
#include <list>
#include <bitset>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef pair<ll,ll> pll;

#define pb push_back
#define mp make_pair

pll solve(ll N, ll K) {
  ll L = (N-1)/2;
  ll R = (N)/2;
  assert(L+R+1 == N);
  assert(abs(L-R) <= 1);
  if (K == 1) return { max(L,R), min(L,R) };
  if (N%2 == 0) {
    // even, so do R first (because it's bigger)
    assert(L == R-1);
    if (K%2 == 0) return solve(R, K/2);
    else return solve(L, K/2);
  } else {
    // odd, so do L first (because they are the same, and left-most first)
    assert(L == R);
    if (K%2 == 0) return solve(L, K/2);
    else return solve(R, K/2);
  }
}

int main() {
  int TEST;
  ll N,K;
  cin >> TEST;
  FOR(test,TEST) {
    cin >> N >> K;
    pll ans = solve(N,K);
    cout << "Case #" << (test+1) << ": " << ans.first << " " << ans.second << endl;
  }
}






