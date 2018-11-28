#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;
const int N = 1005;
long long n;
int a[100],cnt;
int res[100];
int main(){
  freopen("in","r",stdin);
  freopen("out","w",stdout);
  int T;scanf("%d",&T);
  int cas = 1;
  while(T--){
      scanf("%lld",&n);
     // cout<<n<<endl;
      cnt = 0;
      while(n>0){
          a[++cnt] = n%10;
          n/=10;
         // cout<<cnt<<endl;
      }
      bool eq = true;
      for(int i=cnt;i;i--){
          res[i] = 0;
          if(!eq){
              res[i] = 9;
              //printf("res[%d]:%d\n",i,res[i]);
              continue;
          }
          for(int j=9;j>0;j--){
              bool ok = true;
              for(int k = i;k;k--){
                  if(a[k]>j) break;
                  else if(a[k]<j) {
                      ok = false;
                      break;
                  }
              }
              if(ok){
                  res[i] = j;
                  break;
              }
          }
          eq&=(res[i]==a[i]);
         // printf("res[%d]:%d\n",i,res[i]);
      }
      while(res[cnt]==0) cnt--;
      printf("Case #%d: ",cas++);
      for(int i=cnt;i;i--){
          printf("%d",res[i]);
      }
      puts("");
  }
  return 0;
}
