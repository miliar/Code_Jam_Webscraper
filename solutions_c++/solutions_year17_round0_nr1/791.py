#include<cstdio>
#include<cstring>
int T,C,n,m,i,j,ans;char a[111111];
int main(){
  scanf("%d",&T);
  for(C=1;C<=T;C++){
    printf("Case #%d: ",C);
    scanf("%s%d",a+1,&m);
    n=strlen(a+1);
    for(i=1;i<=n;i++)a[i]=a[i]=='+';
    ans=0;
    for(i=1;i+m-1<=n;i++)if(!a[i]){
      ans++;
      for(j=0;j<m;j++)a[i+j]^=1;
    }
    for(i=1;i<=n;i++)if(!a[i])ans=-1;
    if(ans>=0)printf("%d\n",ans);else puts("IMPOSSIBLE");
  }
}