#include <cstdio> // printf, scanf
#include <vector> // std::vector

void solution ()
{
  std::vector < char > v;
  int k;
  int result = 0;
  
  {
    char c;
    getchar();
    while ((c = getchar()) != ' ') v.push_back(c);
  }
  
  scanf("%d", &k);
  
  for (int i = 0; i <= v.size() - k; ++i) {
    if (v[i] == '-') {
      ++result;
      for (int j = 0; j < k; ++j) {
        v[i+j] = ((v[i+j] == '+') ? '-' : '+');
      }
    }
  }
  
  for (auto i : v) {
    if (i == '-') {
      printf("IMPOSSIBLE\n");
      return;
    }
  }
  
  printf("%d\n", result);
}

int main ()
{
  #ifdef DEBUG
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  #endif
  
  int t;
  scanf("%d", &t);
  
  for (int i = 1; i <= t; ++i) {
    printf("Case #%d: ", i);
    solution();
  }
  
  return 0;
}
