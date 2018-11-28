#include<stdio.h>

void solve(){
  char n[20];
  scanf("%s", n);
  int pos = 1;
  while(n[pos]!=0){
    if(n[pos-1]>n[pos]){
      int p = pos-1;
      n[p--]--;
      while(p>=0 && n[p] > n[p+1]){
        n[p]--;
        n[p+1] = '9';
        p--;
      }
      while(n[pos]!=0)
        n[pos++] = '9';
      
    }else{
      pos++;
    }
  }
  int fi = (n[0]=='0' ? 1 : 0);
  printf("%s\n", n+fi);
}

int main(int argc, char *argv[]){
  int T; scanf("%d ", &T);
  for(int tc=1; tc<=T; tc++){
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
