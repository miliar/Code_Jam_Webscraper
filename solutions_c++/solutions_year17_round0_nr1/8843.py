#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#define forn(n) for(int i=0;i<n;i++)
typedef long long LL;
int pie[1000];
int flip[1000];
int N;
using namespace std;
void setPie(int i, char sign) {
  if (sign == '+') {
    pie[i] = 1;
  } else {
    pie[i] = -1;
  }
  N++;
}
void init() {
  forn(1000) {
    pie[i] = 0;
    flip[i] = 1;
  }
  N = 0;
}
void flip_k(int i, int K) {
  for(int j=i; j<i+K; j++) {
    flip[j] *= -1;
  }
}
void print_array(int a[], int n) {
  forn(n) {
    cout << a[i] << ' ';
  }
  cout <<endl;
}
int solve(int case_num){
  init();
  //int flip = 1;
  char plus_or_minus;
  int index = 0;
  //char current = plus_or_minus;
  int result = 0;

  while ((plus_or_minus=getchar()) != ' '){
    setPie(index, plus_or_minus);
    index++;
  }
  int K;
  cin >> K;
  // cout << "N : " << N << ", K: " << K << endl;
  for(int i=0; i < N-K+1; i++) {
    // cout << "pie:" <<endl;
    // print_array(pie, N);
    // cout << "flip:" <<endl;
    // print_array(flip, N);

    if (pie[i]*flip[i] == -1) {
      flip_k(i,K);
      result++;
    }
  }
  plus_or_minus=getchar();

  for(int i=N-K+1; i<N; i++) {
    if (pie[i]*flip[i] == -1) {
      printf("Case #%d: IMPOSSIBLE\n", case_num);
      return 0;
    }
  }
  printf("Case #%d: %d\n", case_num, result);
  return 0;
}

int main(){
  int T, i;
  scanf("%d", &T);
  getchar();
  for (i = 1; i<=T; ++i )
    solve(i);
  return 0;
}
