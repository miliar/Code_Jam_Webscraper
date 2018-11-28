#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

long long transform(long long n){
  char s[30];
  if(n < 10){
    return n;
  }
  sprintf(s, "%lld", n);
  int i, len = strlen(s);
  for(i = 0; i < (len-1) && s[i] <= s[i+1]; i++);
  if(i == (len-1)){
    return n;
  }
  s[i]--;
  for(int j = i+1; j < len; j++){
    s[j] = '9';
  }
  long long answer;
  sscanf(s, "%lld", &answer);
  return answer;
}

bool isTidy(long long n){
  char s[30];
  sprintf(s, "%lld", n);
  int len = strlen(s);
  for(int i = 1; i < len; i++){
    if(s[i] < s[i-1]){
      return false;
    }
  }
  return true;
}

long long tidyNumbers(long long n){
  int times = 0;
  while(isTidy(n) == false){
    n = transform(n);
    times++;
  }
//  printf("times %d\n", times);
  return n;
}

int main() {
  long long n;
  int cases;
  while(cin >> cases){
    for(int i = 1; i <= cases; i++){
      cin >> n;
      printf("Case #%d: %lld\n", i, tidyNumbers(n));
    }
  }
  return 0;
}
