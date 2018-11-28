#include <cstdio>
#include <cstring>

inline char flip(char c) {
  if (c=='+')
    return '-';
  else
    return '+';
}
char line[1024];
int main() {
  int tests;
  int answer;
  bool possible;
  int k, n;
  scanf(" %d", &tests);
  for(int test_number=1; test_number<=tests; ++test_number) {
    printf("Case #%d:", test_number);
    scanf(" %s %d", line, &k);
    n = strlen(line);
    answer = 0;
    possible = true;
    for(int i=0; i<=n-k; ++i) {
      if (line[i]=='-') {
	for(int j=i; j<i+k; ++j)
	  line[j]=flip(line[j]);
	++answer;
      }
      //printf("\n%s\n", line);
    }
    for(int i=n-k; i<n; ++i)
      if (line[i]=='-')
	possible=false;
    if (!possible)
      printf(" IMPOSSIBLE\n");
    else
      printf(" %d\n", answer);
  }
  return 0;
}
