#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#define Maxlen 18
using namespace std;

int t;
char num[Maxlen + 10];

void work();

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  scanf("%d", &t);
  for (int i = 1;i <= t;++ i) {
    printf("Case #%d: ", i);
    work();
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
void work() {
  int from = -1;
  bool turn = false;
  bool zero = false;
  getchar();
  scanf("%s", num);
  for (int i = strlen(num) - 1;i >= 1;-- i) {
    if (num[i] < num[i - 1]) {
      num[i] = '9';
      turn = true;
      -- num[i - 1];
      from = i;
    }
  }
  for (int i = 0;i < strlen(num);++ i) {
    if (!zero && num[i] == '0') continue;
    if (num[i] != '0')
      zero = true;
    printf("%c", (!turn || from > i) ? num[i] : '9');
  }
  printf("\n");
}
