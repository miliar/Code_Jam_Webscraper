#include<stdio.h>
int a[100];
int main(){
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  int t;
  scanf("%d",&t);
  int tt=1;
  while(t--){
    int n,p;
    scanf("%d %d",&n,&p);
    for(int i=0;i<5;i++){
      a[i]=0;
    }
    for(int i=0;i<n;i++){
      int x;
      scanf("%d",&x);
      a[x % p]++;
    }
    int ans=a[0];
    int tmp=0;
    if (p==3){
      if(a[1]<a[2]) tmp=a[1]; else tmp=a[2];
      ans=ans+tmp;
      a[1]=a[1]-tmp;
      a[2]=a[2]-tmp;
      for(int j=1;j<p;j++){
        if(a[j] % p!=0) ans++;
        ans+=a[j]/3;
      }
    }
    if (p==2){
      ans+=a[1]/2;
      if (a[1]% 2==1) ans++;
    }
    if (p==4){
      if(a[1]<a[3]) tmp=a[1]; else tmp=a[3];
      ans=ans+tmp;
      a[1]=a[1]-tmp;
      a[3]=a[3]-tmp;      
      ans+=a[2]/2;
      
      int dd=a[1]+a[3];
      if (a[2]%2==1) dd+=2;
      if (dd % 4>0) ans++;
      ans+=dd/4;
    }
    printf("Case #%d: %d\n",tt,ans);
    tt++;
    
  }
 
  fclose(stdin);
  fclose(stdout);
}