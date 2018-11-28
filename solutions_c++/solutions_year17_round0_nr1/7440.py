#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main() {
  int t;

  cin >> t;

  for (int i = 0; i < t; ++i) {
    string n;
    int k;
    cin >> n >> k;

    std::cout << "Case #" << i + 1 << ": ";

    int answer = 0;
    for (int j = 0; j < n.size() - k + 1; ++j)
      if (n[j] == '-') {
        answer++;
        for (int l = 0; l < k; ++l)
          n[l + j] = n[l + j] == '-' ? '+' : '-';
      }

    bool ok = true;
    for (int j = 0; j < n.size(); ++j)
      if (n[j] == '-')
        ok = false;

    if (ok)
      std::cout << answer << std::endl;
    else
      std::cout << "IMPOSSIBLE" << std::endl;
  }

  return 0;
}
