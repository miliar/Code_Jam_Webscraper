#include <cstdio>
using namespace std;
//             0    1    2    3    4    5
char ch[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
int T, N, num[6];

void cir(int x, int y) {
  for (; num[y] > 0; num[y] --) printf("%c%c", ch[x], ch[y]);
  printf("%c", ch[x]);
}

void feed(int x) {
  num[x] --;
  if (x == 0) cir(0, 3);
  if (x == 2) cir(2, 5);
  if (x == 4) cir(4, 1);
}

bool spec(int x, int y) {
  for (int i = 0; i < 6; i ++)
    if (num[i] > 0 && i != x && i != y) return false;
  for (int i = 0; i < num[x]; i ++) printf("%c%c", ch[x], ch[y]);
  return true;
}

bool solve() {
  if (num[3] > 0) {
    if (num[0] < num[3]) return false;
    if (num[0] == num[3]) return spec(0, 3);
  }
  if (num[5] > 0) {
    if (num[2] < num[5]) return false;
    if (num[2] == num[5]) return spec(2, 5);
  }
  if (num[1] > 0) {
    if (num[4] < num[1]) return false;
    if (num[4] == num[1]) return spec(4, 1);
  }

  num[0] -= num[3], num[2] -= num[5], num[4] -= num[1];

  if (num[0] + num[2] < num[4]) return false; 
  if (num[2] + num[4] < num[0]) return false; 
  if (num[4] + num[0] < num[2]) return false; 

  int i, t;
  if (num[0] > num[2]) i = 0; else i = 2;
  if (num[4] > num[i]) i = 4;

  t = num[0] + num[2] + num[4] - num[i] - num[i];
  
  // printf("%d %d %d\n", num[0], num[2], num[4]);
  for (int j = 0; num[i] > 0; j ++) {
    feed(i);

    bool st = false;
    for (int k = 0; k <= 4; k += 2)
      if (k != i && num[k] > 0) {
        if (st && j >= t) continue;
        feed(k), st = true;
      }
  }

  return true;
}

int main()
{
  scanf("%d", &T);
  for (int cou = 1; cou <= T; cou ++) {
    scanf("%d", &N);
    for (int i = 0; i < 6; i ++) scanf("%d", &num[i]);
    printf("Case #%d: ", cou);
    if (!solve()) printf("IMPOSSIBLE");
    printf("\n");
  }
}
