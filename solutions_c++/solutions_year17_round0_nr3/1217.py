
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

using pll = pair<long long, long long>;

struct Solver {
  //map<pll, pll> dp;

  pll solve(long long n, long long k) {
    long long m = (n-1) / 2;
    pll ans {m,n-m-1}; // place one already in the middle
    if (k==1) return ans;
    long long k_big_half=k/2;
    if (k & 1) {
      return solve(ans.first, k_big_half);
    } else {
      return solve(ans.second, k_big_half);
    }
  }
};

int main() {
  int T;
  cin >> T;
  Solver s;
  for (int tc=1; tc<=T; tc++) {
    long long int N, K;
    cin >> N >> K;
    cout << "Case #" << tc << ": ";
    auto ans = s.solve(N,K);
    cout << max(ans.first, ans.second) << " " << min(ans.first, ans.second) << endl;
  }
}
