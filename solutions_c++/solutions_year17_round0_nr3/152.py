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
  
void solve() {
  uint64_t n, k;
  cin >> n >> k;
  
  std::map<uint64_t, uint64_t, std::greater<uint64_t>> queue;
  queue[n] = 1;
  uint64_t last = n;
  while (k > 0) {
    auto top = *queue.begin();
    queue.erase(top.first);
    if (top.second == 0) {
      continue;
    }
    last = top.first;
    auto count = std::min(top.second, k);
    k -= count;
    
    uint64_t l = (last - 1) / 2;
    uint64_t r = last - 1 - l;
    queue[l] += count;
    queue[r] += count;
  }
  cout << last / 2 << ' ' << (last - 1) / 2 << endl;
  
  
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