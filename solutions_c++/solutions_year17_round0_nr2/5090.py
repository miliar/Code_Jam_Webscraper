#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int T;

char buf[100];
char ans[100];

int solve() {
  int len = strlen(buf);
  //printf("%d %s\n", len, buf);
  if (len == 1) {
    strcpy(ans, buf);
    return 0;
  }
  
  int flag = 0;
  for (int i = 0; i < len; ++i) {
    // printf("%d\n",i);
    if (flag) {
      ans[i] = '9';
    } else {
      if (buf[i+1] != '\0' && buf[i] > buf[i+1]) {
	char c = buf[i];
	int j = i;
	while (j >= 0 && buf[j] == c) {
	  --j;
	}
	i = j+1;
	ans[i] = buf[i]-1;
	flag = 1;
      } else {
	ans[i] = buf[i];
      }
    }
  }
  ans[len] = '\0';
  int cnt = 0;
  for (int i = 0; i < len; ++i) {
    if (ans[i] != '0') break;
    ++cnt;
  }
  return cnt;
}

int main() {
  scanf("%d",&T);
  for (int i = 1; i <= T; ++i) {
    scanf("%s",buf);
    int k = solve();
    printf("Case #%d: %s\n", i, ans+k);
  }
  return 0;
}
