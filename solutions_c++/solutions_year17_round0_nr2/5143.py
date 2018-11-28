#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <stack>
#include <queue>
using namespace std;

int table[20];

int main() {
  int TC;
  scanf("%d", &TC);
  for(int t = 1; t <= TC; ++t) {
    for(int i = 0; i <  20; ++i) {
      table[i] = 0;
    }

    long long int N;
    scanf("%lld", &N);
    int counter = 0;
    while(N > 0) {
      table[counter] = N % 10;
      counter++;
      N /= 10;
    }

    for(int i = counter-1; i > 0; --i) {
      if(table[i] > table[i-1]) {
        for(int j = i; j < counter; ++j) {
          if(table[j] > table[j+1]) {
            table[j]--;
            for(int k = j-1; k >= 0; --k) {
              table[k] = 9;
            }
            break;
          }
        }
        break;
      }
    }

    long long int ans = 0;
    for(int i = counter; i >= 0; --i) {
      ans *= 10;
      ans += table[i];
    }

    printf("Case #%d: %lld\n", t, ans);
  } 
}