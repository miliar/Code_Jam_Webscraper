#include<stdio.h>

int main(){
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  char str[100];
  char ans[100];
  int t;
  scanf("%d\n",&t);
  for(int tt=0;tt<t;tt++){
    int n,m;
    int nn=0;
    int mm=0;
    scanf("%d %d\n",&n,&m);
    printf("Case #%d:\n",tt+1);
    for(int i=0;i<n;i++){
      gets(str);
      char first='?';
      for(int j=0;j<m;j++){
        if (str[j]!='?'){
          if(first=='?'){
            first=str[j];
            for(int k=0;k<=j;k++){
              ans[k]=first;
            }
          }else{
            first=str[j];
            ans[j]=first;
        }}
        else{
          if (first!='?') ans[j]=first;
        }
      }
      ans[m]=0;
      if (first!='?'){
        for(int k=0;k<nn+1;k++){
          printf("%s\n",ans);
        }
        nn=0;
      }else nn++;
    }
    for(int k=0;k<nn;k++){
          printf("%s\n",ans);
        }
  }   
   fclose(stdin);
  fclose(stdout);
}