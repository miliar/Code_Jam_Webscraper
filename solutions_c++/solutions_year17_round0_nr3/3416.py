#include <iostream>
#include <set>
std::multiset<int> sizes;
int t, k, n;
int main() {
  std::ios::sync_with_stdio(false);
  std::cin >> t;
  for(int i = 0; i < t; i++) {
    sizes.clear();
    std::cin >> n >> k;
    int groups = k - 1;
    sizes.insert(n);
    while(groups--) {
      int top = *sizes.rbegin();
      sizes.erase(sizes.find(top));
      sizes.insert(top/2);
      sizes.insert((top-1)/2);
    }
    int last = *sizes.rbegin();
    std::cout << "Case #" << i + 1 << ": " <<
      last/2 << " " << (last-1)/2 << std::endl;
  }
}
