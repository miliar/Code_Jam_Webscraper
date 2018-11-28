#include<stdio.h>

int main(){
  freopen("p20.in","r",stdin);freopen("p20.out","w",stdout);
  int n;
  scanf("%d",&n);
  int i;
  int a[30];
  for(i=0;i<n;i++){
    long long t;
    printf("Case #%d: ",i+1);
    scanf("%I64d",&t);
    int k=0;
    while(t!=0){
      a[k++]=t % 10;
      t=t/10;
    }
    k--;
    int l=k;
    while(k>=1 && a[k]<=a[k-1]){
      k--;
    }
    if (k==0){
      int j;
      for(j=l;j>=0;j--) printf("%d",a[j]);
      printf("\n");
    }else{
      int j;
      for(j=0;j<k;j++) a[j]=9;
      a[k]--;
      while(k<l && a[k]<a[k+1]){
        a[k++]=9;
        a[k]--;
      }
      while(l>0&&a[l]==0) l--;
      for(j=l;j>=0;j--) printf("%d",a[j]);
      printf("\n");
    }
  }
  fclose(stdin);
  fclose(stdout);
}
    
    
    