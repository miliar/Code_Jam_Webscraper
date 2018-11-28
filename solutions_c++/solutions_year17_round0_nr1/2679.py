#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char str[1055];

int main(){
  freopen("A-large.in","r",stdin);
  freopen("p1large.out","w",stdout);
  gets(str);
  int t=atoi(str);
  for(int i=0;i<t;i++){
    int k;
    scanf("%s%d",str,&k);
    int l=strlen(str);
    int flag=1;
    int ans=0;
    for(int j=0;j<l;j++)
      if(str[j]!='+'){
        if((j+k)>l){
          flag=0;
          break;
        }
        ans++;
        for(int jj=0;jj<k;jj++)
          if(str[j+jj]!='+') str[j+jj]='+';
          else str[j+jj]='-';
      }
    if (flag==1){
      printf("Case #%d: %d\n",i+1,ans);
    }
    else printf("Case #%d: IMPOSSIBLE\n",i+1);
  }
  
  fclose(stdin);
  fclose(stdout);
}
    
    
    