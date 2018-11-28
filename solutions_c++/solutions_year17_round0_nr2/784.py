#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long ll;
int T,C,m,i,j,k;ll a[222],b[222],ans,n;
bool check(){
  for(int k=m-1;k;k--)if(b[k]<b[k+1])return 0;
  return 1;
}
void cal(){
  ll now=0;
  for(int k=m;k;k--)now=now*10+b[k];
  ans=max(ans,now);
}
int main(){
  scanf("%d",&T);
  for(C=1;C<=T;C++){
    printf("Case #%d: ",C);
    scanf("%I64d",&n);
    m=0;
    while(n)a[++m]=n%10,n/=10;
    ans=0;
    for(i=m;i;i--){
      for(j=0;j<a[i];j++){
        for(k=m;k>i;k--)b[k]=a[k];
        b[i]=j;
        for(k=i-1;k;k--)b[k]=9;
        if(check())cal();
      }
    }
    for(i=1;i<=m;i++)b[i]=a[i];
    if(check())cal();
    printf("%I64d\n",ans);
  }
}