#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <map>

using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)
#define PATH "C:\\Users\\Valentin\\Desktop\\cpp\\"

template<typename T>
int sz(const T& t) {
  return static_cast<int>(t.size());
}

int digit_count(uint64_t x) {
  int res = 0;
  while (x) {
    res++;
    x /= 10;
  }
  return res;
}

uint64_t ones(int digit_count) {
  uint64_t res = 0;
  while (digit_count--) {
    res = res * 10U + 1U;
  }
  return res;
}

uint64_t nines(int digit_count) {
  return ones(digit_count) * 9U;
}

uint64_t power_of_ten(int power) {
  uint64_t res = 1;
  while (power--) {
    res *= 10;
  }
  return res;
}
  
void solve() {
  uint64_t n;
  cin >> n;
  int len = digit_count(n);
  if (n < ones(len)) {
    cout << nines(len - 1) << endl;
    return;
  }
  uint64_t ans = 0;
  for (int pos = len - 1; pos >= 0; --pos) {
    for (int num = 9; num >= 0; --num) {
      if (ans + ones(pos + 1) * static_cast<uint64_t>(num) <= n) {
        ans += power_of_ten(pos) * static_cast<uint64_t>(num);
        break;
      }
    }
  }
  cout << ans << endl;
}

int main() {
  freopen(PATH"in.txt", "r", stdin);
  freopen(PATH"out.txt", "w", stdout);

  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int t;
  cin >> t;
  forn (i, t) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }  
  
  cout.flush();
  return 0;
}