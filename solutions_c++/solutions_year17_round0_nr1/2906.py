#include <cstdio>
#include <cstring>

using namespace std;

const int maxl = 1000;
char str[maxl+5];
int k, l;

int main() {
  int tc;
  scanf("%d\n", &tc);
  for(int kase = 1; kase <= tc; kase++) {
    scanf("%s %d\n", str, &k);
    l = strlen(str);
    int ans = 0;
    int i;
    for(i = 0; i <= l - k; i++) {
      if(str[i] == '-') {
	for(int j = i; j < i + k; j++) {
	  str[j] = str[j] == '+' ? '-' : '+';
	}
	ans++;
      }
    }
    bool ok = true;
    for(; i < l; i++) {
      if(str[i] == '-') {
	ok = false;
	break;
      }
    }
    if(ok)
      printf("Case #%d: %d\n", kase, ans);
    else
      printf("Case #%d: IMPOSSIBLE\n", kase);
  }
  return 0;
}
