#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

bool isTidy(ll N) {
 ll n = N;
 vector<int> dig;
 while (n) {
   dig.push_back(n % 10);
   n /= 10;
 }
 for (int i = 1; i < dig.size(); i++)
   if (dig[i] > dig[i-1]) return false;
 return true;
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  vector<int> ans(1000);
  for (int i = 1; i <= 1000; i++) {
    for (int j = i; j >= 1; j--) {
      if (isTidy(j)) {
        ans[i] = j;
        break;
      }
    }
  }

  int T; cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    cout << "Case #" << tc << ": ";
    ll N; cin >> N;
    cout << ans[N] << endl;
  }
}
