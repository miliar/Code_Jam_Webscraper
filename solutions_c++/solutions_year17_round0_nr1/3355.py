#include <iostream>
#include <string>
#define MAXN 1005
std::string side;
int k, n;

void swap_sides(int pos) {
  for(int j = 0; j < k; j++) {
    side[pos+j] = side[pos+j] == '+' ? '-' : '+';
  }
}

int main() {
  int t;
  std::cin >> t;
  for(int ii = 0; ii < t; ii++) {
    std::cout << "Case #" << ii + 1 << ": ";
    std::cin >> side >> k;
    int res = 0;
    for(int i = 0; i + k <= side.length(); i++) {
      if (side[i] != '+') {
        swap_sides(i);
        res++;
      }
    }
    for(int i = side.length() - k; i < side.length(); i++) {
      if (side[i] == '-')
        res = -1;
    }
    if (res == -1)
      std::cout << "IMPOSSIBLE\n";
    else
      std::cout << res << "\n";
  }
}
