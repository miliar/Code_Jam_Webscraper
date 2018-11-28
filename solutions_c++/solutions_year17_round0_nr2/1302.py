#include <bits/stdc++.h>
using namespace std;
int T, M, Q;
string N;
void ini(void){
  cin>>N;
  M = N.length();
}

void sol(void){
  char X;
  int f = M;
  for(int i = M - 2; i >= 0; i--){
    if(f == i + 1) X = N[i + 1] - 1;  //不可能有 0 變 -1 的
    else X = N[i + 1];
    if(N[i] > X){
      f = i;
    }
    //printf("N[%d] = %c vs %c => f = %d\n", i, N[i], X, f);
  }
  for(int i = 0; i < M; i++){
    if(i == f){
      N[i]--;
      if(!i && N[i] == '0') continue;
      else cout<<N[i];
    }else if(i > f) cout<<'9';
    else cout<<N[i];
  }
  cout<<endl;
}

int main(void){
  int i, j;
  cin>>T;
  for(i = 1; i <= T; i++){
    ini();
    cout<<"Case #"<<i<<": ";
    sol();
  }
}
