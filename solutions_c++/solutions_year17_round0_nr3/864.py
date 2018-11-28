#include <stdio.h>
#include <cstring>
#include <string>

typedef long long LL;
LL mx,mn;

void solve(LL n, LL k){
  LL cntl(0),cntr(1);
  LL pre_cntl(0),pre_cntr(1);
  LL ll(0),lr(n);
  LL pre_ll(0),pre_lr(n);
  while(1){
  //  printf("%lld %lld %lld %lld %lld\n",pre_ll,pre_cntl,pre_lr,pre_cntr,k);
    if(pre_cntr>=k){
      mn=(pre_lr-1)/2;
      mx=(pre_lr-1)/2 + (pre_lr-1)%2;
      return;
    }
    if(pre_cntr+pre_cntl>=k){
      mn=(pre_ll-1)/2;
      mx=(pre_ll-1)/2+ (pre_ll-1)%2;
      return;
    }
    if(pre_cntr>0){
      if(pre_lr%2==1){
        lr=(pre_lr-1)/2;
        cntr=2*pre_cntr;
        ll=lr-1;
        if(ll<0) ll=0;
        cntl=0;
      }else{
        lr=pre_lr/2;
        cntr=pre_cntr;
        ll=(pre_lr-1)/2;
        cntl=pre_cntr;
      }
    }
    if(pre_cntl>0){
      if(pre_ll%2==1){
        cntl += 2*pre_cntl;
      }else{
        lr=pre_ll/2;
        ll=lr-1;
        cntl = pre_cntl;
        cntr += pre_cntl;
      }
    }
    k -= pre_cntl + pre_cntr;
    pre_cntl=cntl;
    pre_ll =ll;
    pre_cntr=cntr;
    pre_lr = lr;
    while(pre_lr==0) ;
  }
}

int main()
{
  freopen("C-large.in","r",stdin);
//  freopen("c.in","r",stdin);
  freopen("C-large.out","w",stdout);
  int test,cas(1);
  LL n, k;
  scanf("%d",&test);
  while(test--){
    scanf("%lld%lld",&n,&k);
    solve(n,k);
    printf("Case #%d: %lld %lld\n",cas++,mx,mn); 
  }
  return 0;
}
/* sw=2;ts=2;sts=2;expandtab */
