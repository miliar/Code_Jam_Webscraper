#include <iostream>
#include <map>


void solve(int test_id) {
  long long N, K;
  std::cin >> N >> K;
  std::map<long long, long long> mp;
  mp[N] = 1;
  while (1) {
    std::map <long long, long long>::reverse_iterator it = mp.rbegin();
    K -= (it->second);
    if (it->first & 1){
      mp[it->first / 2 ] += (it->second * 2);
      if (K <= 0){
        std::cout << "Case #" << test_id << ": " << it->first / 2 << " " << it->first / 2 << "\n";
        return;
      }
    }
    else {
      mp[it->first / 2] += it->second;
      mp[it->first / 2 - 1] += it->second;
      if (K <= 0) {
        std::cout << "Case #" << test_id << ": " << it->first / 2 << " " << it->first / 2 - 1<< "\n";
        return;
      }
    }
    if (K < 0){

    }
    mp.erase(it->first);
  }
}

int main() {
  int tests;
  std::cin >> tests;
  for (int i = 1; i <= tests; ++i) {
    solve(i);
  }
}
