#include<stdio.h>

void solve(int t) {
  long long n, ones, ans=0;
  scanf("%lld",&n);
  for(int i=1;i<=9;i++) {
    for(ones=1;ans+ones<= n;ones=ones*10+1);
    ans += ones/10;
    
  }
  printf("Case #%d: %lld\n",t,ans);
}

int main() {
  int t,T;
  scanf("%d",&T);
  for(t=1;t<=T;t++) solve(t);
  return 0;
}
