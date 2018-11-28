#include <stdio.h>

bool isTidy(char number[], int j) {
  for(int i=1; i<=j; ++i) {
    if (number[i] < number[i-1]) {
      return false;
    }
  }
  return true;
}

char* findLastTidy(char number[], int j) {
  if (isTidy(number, j))
    return number;

  // has more than one digit
  int i;
  // minus 1
  // j always points to the last digit
  while (j > 0 && !isTidy(number, j)) {
    // subtract one
    if (number[j] > '0') {
      number[j] = number[j] - 1;
    } else {
      i = j;
      while (number[i] == '0') {
        number[i] = '9';
        i--;
      }
      // i points to the first non-zero dig
      if (i == 0 && number[i] == '1') {
        // will change scale
        number[i] = '9';
        number[j] = '\0';
        j--;
        // all nines
        return number;
      } else {
        number[i] = number[i] - 1;
      }
    }
    //printf("number: %s\n", number);
  }
  return number;
}

int main() {

  int t, j;
  char number[20];
  char *lastTidy;

  scanf("%d\n", &t);
  for(int i=1; i<=t; ++i) {
    number[0] = '\0';
    j = 0;
    scanf("%s\n", number);
    while (number[++j] != '\0');
    j--;
    //printf("j=%d\n", j);
    lastTidy = findLastTidy(number, j);
    printf("Case #%d: %s\n", i, lastTidy);
  }
  return 0;
}
