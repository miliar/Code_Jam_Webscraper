#include <cstdio>
#include <string>
#include <string.h>

using namespace std;

void flip(char* pancake, int k) {
  for (int i=0; i<k; i++) {
    if (*(pancake+i) == '+') {
      *(pancake + i) = '-';
    } else {
      *(pancake + i) = '+';
    }
  }
}
bool is_all_happyside(char* pancake, int size) {
  for (int i=0; i<size; i++) {
    if (*(pancake+i) == '-') {
      return false;
    }
  }
  return true;
}

int main() {
  int t;
  scanf("%d", &t);

  for (int i=0; i<t; i++) {
    char pancake[1000];
    int k;
    scanf("%s %d", pancake, &k);

    int num = strlen(pancake);
    int j = 0;
    int cnt = 0;

    while (j < num-k+1) {
      if (pancake[j] == '-') {
        flip(pancake+j, k);
        ++cnt;
      }
      ++j;
    }
    if (is_all_happyside(pancake, num)) {
      printf("Case #%d: %d\n", i+1, cnt);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", i+1);
    }
  }
}
