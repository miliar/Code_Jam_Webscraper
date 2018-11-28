#include <iostream>
#include <vector>
#include <string>


int main() {
  int T;
  std::cin >> T;
  for (int t = 0; t < T; ++t) {
    long long n;
    std::cin >> n;
    std::string nstr = std::to_string(n);
    int m = nstr.size();
    char maxchr = '9';
    int idx = m;
    for (int i = m; i-->0; ) {
      if (nstr[i] > maxchr) {
        idx = i;
        maxchr = nstr[i]-1;
      }
      else
        maxchr = nstr[i];
    }
    std::string resstr = nstr;
    for (int i = 0; i < m; ++i) {
      if (i == idx)
        --resstr[i];
      else if (i > idx)
        resstr[i] = '9';
    }
    long long res = std::stoll(resstr);

    std::cout << "Case #" << t+1 << ": " << res << std::endl;
  }
  return EXIT_SUCCESS;
}
