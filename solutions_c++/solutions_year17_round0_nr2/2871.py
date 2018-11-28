#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 18;
char str[maxn+5];
int len;

void solve(int x) {
  if(x <= 1)
    return;
  int i;
  for(i = 1; i < x; i++) {
    if(str[i] < str[i-1]) {
      break;
    }
  }
  if(i == x)
    return;
  for(int idx = i; idx < x; idx++)
    str[idx] = '9';
  for(int idx = i - 1; idx >= 0; idx--) {
    if(str[idx] == '0') {
      str[idx] = '9';
    } else {
      str[idx]--;
      break;
    }
  }
  solve(i);
}

int main() {
  int tc;
  scanf("%d\n", &tc);
  for(int kase = 1; kase <= tc; kase++) {
    scanf("%s\n", str);
    len = strlen(str);
    solve(len);
    printf("Case #%d: %s\n", kase, str[0] == '0' ? str+1 : str);
  }
  return 0;
}
