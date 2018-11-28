#include <cstdio>
#include <iostream>
#include <string.h>

using namespace std;

int main() {
  bool foundNine = false;
  int n;
  char number[1005];

  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    //fgets(number, sizeof number, stdin);
    cin >> number;

    for (int j = strlen(number) - 1; j >= 1; j--) {
      if (number[j] < number[j-1]) {
        number[j-1] -= 1;
        number[j] = '9';
      }
    }
    printf("Case #%d: ", i+1);

    if (number[0] == '0') {
      for (int j = 1; j < strlen(number); j++) {
        if (!foundNine) {
          if (number[j] != '9') {
            printf("%c", number[j]);
          } else {
            printf("9");
            foundNine = true;
          }
        } else {
          printf("9");
        }
      }
    } else {
      for (int j = 0; j < strlen(number); j++) {
        if (!foundNine) {
          if (number[j] != '9') {
            printf("%c", number[j]);
          } else {
            printf("9");
            foundNine = true;
          }
        } else {
          printf("9");
        }
      }
    }
    printf("\n");
    foundNine = false;
  }

  return 0;
}
