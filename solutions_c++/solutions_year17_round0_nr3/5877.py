#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef unsigned long long int size;
size l=0,r=0,E;
void check(size,size);
int main(){
  int p;
  size n,k;
  scanf("%d",&p);
  for(int ctr_p=0;ctr_p<p;ctr_p++){
    scanf("%llu %llu",&n,&k);
    check(n+2,k);
    printf("Case #%d: %llu %llu\n",ctr_p+1,(l>r)?l:r,(l>r)?r:l);
  }
  return 0;
}
void check(size n,size k){
  int *a=(int *)malloc(sizeof(size)*n);
  for(size i=1;i<n+1;i++)
    a[i]=0;
  a[0]=a[n-1]=1;
  while(k){
      size pmin=0,pmax,min,max;
      for(size i=pmin+1;i<n;i++)
        if(a[i]){
          pmax=i;
          break;
        }
        min=pmax;	//
        for(max=min+1;max<n;max++){
          if(a[max]){
            if(pmax-pmin<max-min){
              pmin=min;
              pmax=max;
            }
            min=max;
          }
        }
        E=(pmin+pmax)/2;
        a[E]=1;
        l=E-pmin-1;
        r=pmax-E-1;
    --k;
  }
//  sleep(5);
  free(a);
}
