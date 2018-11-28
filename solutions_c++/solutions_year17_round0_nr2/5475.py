#include <cstdio>
#include <string>

std::string solve() {
  long long int k;
  scanf("%lld", &k);

  std::string s = std::to_string(k);
  int n = (int)s.size();
  std::string gg = s;
  //printf("%s\n", gg.c_str());
  for (int i = n - 1; i >= 1; --i) {
    if (gg[i] < gg[i-1]) {
      gg[i] = '9';
      gg[i-1]--;
      for (int j = i; j < n; ++j)
        gg[j] = '9';
    }
    //printf("%s\n", gg.c_str());
  }
  std::string result;
  bool bartosz_kostka = false;
  for (auto it : gg) {
    if (it != '0') 
      bartosz_kostka = true;
    if (bartosz_kostka) 
      result.push_back(it);
  }
  return result;
}

int main() {
  int q;
  scanf("%d", &q);
  for (int i = 1; i <= q; ++i) {
    printf("Case #%d: %s\n", i, solve().c_str());
  }

  return 0;
}
