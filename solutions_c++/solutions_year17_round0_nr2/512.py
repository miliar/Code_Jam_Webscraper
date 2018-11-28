#include <cstdio>
#include <cstring>
char line[100];

int main() {
  int tests;
  int n;
  scanf(" %d", &tests);
  for(int test_number=1; test_number<=tests; ++test_number) {
    printf("Case #%d:", test_number);
    scanf(" %s", line);
    n = strlen(line);
    for(int i=1; i<n; ++i) {
      if (line[i]<line[i-1]) {
	int j=i-1;
	while(j>0&&line[j]==line[j-1])
	  --j;
	line[j]--;
	for(int k=j+1; k<n; ++k)
	  line[k]='9';
	break;
      }
    }
    for(int i=0; i<n; ++i)
      if (line[i]!='0') {
	printf(" %s\n", line+i);
	break;
      }
  }
  return 0;
}
