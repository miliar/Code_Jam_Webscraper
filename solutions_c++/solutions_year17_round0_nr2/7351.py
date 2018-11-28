#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <string.h>
#include <functional>
#include <utility>
using namespace std;

const int infi = 2147483646;
const int null = -2147483646;

const int N = 30;

char num[N];

bool tidy(char num[], int sz) {
  bool good = true;
  for (int i = 0; i < sz-1; i++) {
    for (int j = i+1; j < sz; j++) {
      int a = num[i] - '0';
      int b = num[j] - '0';
      if (a > b) {
        good = false;
        goto ret;
      }
    }
  }

  ret:
  return good;
}

int main(){
  freopen("B-large.in","r",stdin);
  freopen("out.txt","w",stdout);

  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);

    // solution
    scanf("%s", num);

    int sz = strlen(num);

    if (tidy(num,sz)) {
      printf("%s\n", num);
    } else {
      if (num[sz-1] == '0') {
        for (int i = sz-1; i >= 0; i--) {
          if (num[i] == '0') {
            num[i] = '9';
          } else {
            int a = num[i] - '0';
            num[i] = '0' + (a-1);
            break;
          }
        }

        // reduce
        for (int i = sz-1; i > 0; i--) {
          int a = num[i] - '0';
          int b = num[i-1] - '0';
          if (a < b) {
            char c = '0' + (b-1);
            num[i] = '9';
            num[i-1] = c;

            for (int j = i+1; j < sz; j++) {
              num[j] = '9';
            }
          }
        }
      } else {
        // reduce
        for (int i = sz-1; i > 0; i--) {
          int a = num[i] - '0';
          int b = num[i-1] - '0';
          if (a < b) {
            char c = '0' + (b-1);
            num[i] = '9';
            num[i-1] = c;

            for (int j = i+1; j < sz; j++) {
              num[j] = '9';
            }
          }
        }
      }

      // leading zeros
      int zeros = 0;
      for (int i = 0; i < sz; i++) {
        if (num[i] == '0') {
          zeros++;
        } else {
          break;
        }
      }

      // output
      for (int i = zeros; i < sz; i++) {
        cout << num[i];
      }
      printf("\n");
    }
  }
}
