/**
 * Problem: Problem B (GCJ Qualifications 2017)
 * Author: babhishek21
 * Lang: C++11
 */

#include <bits/stdc++.h> // using GCC/G++
#include "custom/prettyprint.hpp" // G++11 only
using namespace std;

static const int MOD = 1000000007;
static const int INF = 0x3f3f3f3f;
static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
#define pb push_back
#define eb emplace_back
#define mp make_pair

#define debug(x) cerr << #x << " : " << x << endl;
#define whole(func, x, ...) ([&](decltype((x)) var) { return (func)(begin(var), end(var), ##__VA_ARGS__); })(x)

int t;
long long n;
vector<int> nums;

void solve() {
  nums.clear();

  cin >> n;

  if(n < 10) {
    cout << n;
    return;
  }

  while(n > 0) {
    nums.pb(n%10);
    n /= 10;
  }

  // debug(nums)

  int i = 1, inv = -1;
  while(i < nums.size()) {
    if(nums[i] <= nums[i-1]) {
      i++;
      continue;
    }

    // found inversion
    inv  = i;
    nums[i++] -= 1;

    // debug(nums)
  }

  // fix tail
  for(int j = 0; j<inv; j++)
    nums[j] = 9;

  // output
  auto it = nums.rbegin();
  while(it != nums.rend() && *it == 0)
      ++it;
  while(it != nums.rend()) {
    cout << *it;
    ++it;
  }
}

int main() {
  ios_base::sync_with_stdio(false); // for fast I/O

  cin >> t;

  for(int tc=0; tc<t; tc++) {
    cout << "Case #" << tc+1 << ": ";
    solve();
    cout << endl;

    debug(tc+1) // debug
  }

  return 0;
}
