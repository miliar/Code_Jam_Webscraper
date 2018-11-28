#include <iostream>
using namespace std;

int main() {
  int T;
  char number[20];
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    scanf("%s", number);
    int l = strlen(number);
    int index = -1;
    for (int j = 0; j < (l - 1); j++) {
      if (number[j + 1] < number[j]) {
        index = j + 1;
        break;
      }
    }
    if (index != -1) {
      for (int j = index + 1; j < l; j++) number[j] = '9';
      for (int j = index; j > 0; j--) {
        if (number[j] < number[j - 1]) {
          number[j] = '9';
          number[j - 1]--;
        }
      }
    }
    long long answer;
    sscanf (number,"%lld", &answer);
    printf("Case #%d: %lld\n", i + 1, answer);
  }
  return 0;
}