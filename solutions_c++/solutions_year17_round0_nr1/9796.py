#include <cstdio>
#include <string.h>
#include <iostream>

using namespace std;

char swap (char c) {
  if (c == '-') {
    return '+';
  } else if (c == '+') {
    return '-';
  }
}

int main() {
  bool check = true;
  int n, flipNum, length, count;
  char pancake[105];
  //char* ptr = pancake;

  count = 0;
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    //fgets(pancake, sizeof pancake, stdin);
    //scanf("%d", &n);
    cin >> pancake >> flipNum;
    length = (int) strlen(pancake);
    for (int j = 0; j < length; j++) {
      if (j <= length - flipNum) {
        if (pancake[j] == '-') {
          for (int k = j; k < j + flipNum; k++) {
            pancake[k] = swap(pancake[k]);
          }
          count++;
        }
      } else {
        if (pancake[j] == '-') {
          check = false;
          break;
        }
      }
    }

    if (check == true) {
      printf("Case #%d: %d\n", i+1, count);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", i+1);
    }

    count = 0;
    check = true;
  }
}
