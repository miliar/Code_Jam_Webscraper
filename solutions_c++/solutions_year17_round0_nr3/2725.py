#include<stdio.h>


long long p[5000],q[5000];
int main(){
  freopen("C-large.in","r",stdin);freopen("C2.out","w",stdout);
  int t;
  scanf("%d",&t);
  int tt=0;
  while(t--){
    tt++;
    long long n,k;
    scanf("%I64d %I64d",&n,&k);
    int h=0;
    int t=0;
    q[h]=n;p[h]=1;
    long long ans=-1;
    while(h<=t){
      long long n=q[h];
      long long m=p[h];
      if(k<=m || n==0){
        ans = n;
        break;
      }
      h++;
      if (n % 2==1){
        n=n-1;
        k=k-m;
        int i=t;
        while(i>=h && q[i]<(n/2)) i--;
        if (q[i]==(n/2)) p[i]+=m*2;
        else{
          q[++t]=n/2;
          p[t]=m*2;
        }
      }else{
        long long x1=n/2;
        long long x2=n/2-1;
        k=k-m;
        int i=t;
        while(i>=h && q[i]<x1) i--;
        if (q[i]==x1) p[i]+=m;
        else{
          q[++t]=x1;
          p[t]=m;
        }
        i=t;
        while(i>=h && q[i]<x2) i--;
        if (q[i]==x2) p[i]+=m;
        else{
          q[++t]=x2;
          p[t]=m;
        }
      }
    }
    if(ans % 2==1){
      printf("Case #%d: %I64d %I64d\n",tt,(ans-1)/2,(ans-1)/2);
    }else{
      printf("Case #%d: %I64d %I64d\n",tt,ans/2,ans/2-1);
    }
  }
    fclose(stdin);
  fclose(stdout);
}
        