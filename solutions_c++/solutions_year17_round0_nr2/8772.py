#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;

const ll MAX_N = 1e18;
ll counter = 0;
vector<ll> tidy_numbers;

void dfs(ll n, int last_digit) {
  //cout << n << endl;
  if (n > 0) tidy_numbers.push_back(n);
  counter++;
  n *= 10;
  for (int i = last_digit; i <= 9; i++) {
    ll m = n + i;
    if (m < MAX_N) {
      dfs(m, i);
    }
  }
}

ll Solve(ll n) {
  ll ans = 0;
  for (int i = 0; i < tidy_numbers.size(); i++) {
    if (tidy_numbers[i] <= n) ans = tidy_numbers[i];
    else break;
  }
  return ans;
}

int main() {
  dfs(0, 1);
  //cout << counter << endl;
  sort(tidy_numbers.begin(), tidy_numbers.end());
  //for (int i = 0; i < tidy_numbers.size(); i++) {
  //  cout << i << ": " << tidy_numbers[i] << endl;
  //}
  
  int T;
  ll n;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cin >> n;
    cout << "Case #" << tt << ": " << Solve(n) << endl;
  }
  return 0;
}
