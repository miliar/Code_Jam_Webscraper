#include <cstdio>
#include <cstring>
using namespace std;

int T;
char num[18 + 7];

void solve() {
  int pos = 0, len = strlen(num);
  for (int i = 1; i < len; i ++)
    if (num[i] < num[i - 1]) {
      pos = i;
      break;
    }
  if (pos <= 0) return;
  for (int i = pos; i < len; i ++) num[i] = '9';
  for (int i = pos - 1; i >= 0; i --)
    if (num[i] == '0') {
      num[i] = '9';
    } else {
      num[i] = (char)((int)num[i] - 1);
      if (i > 0 && num[i] < num[i - 1]) {
        num[i] = '9';
      } else {
        break;
      }
    }
}

int main()
{
  scanf("%d", &T);
  for (int cou = 1; cou <= T; cou ++) {
    scanf("%s", num);
    printf("Case #%d: ", cou);
    solve();
    printf("%s\n", num + (num[0] == '0' ? 1 : 0));
  }
}
