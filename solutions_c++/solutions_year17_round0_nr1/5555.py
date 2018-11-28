#include <iostream>
#include <string.h>
using namespace std;
const int INF = 20000000;
#define FOR(i,n) for(int i=0,_n=n; i<_n; ++i)
int flips(char a[], int M, int N, int want) {
  int s[M];
  memset(s,0,M);
  int sum=0, ans=0;
  FOR(i,M) {
  	int k=a[i]=='+'?1:0;
    s[i] = (k+sum)%2 != want;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    ans += s[i];
    if(i>M-N and s[i]!=0) return INF;
  }
  return ans;
}
int main() {
  int  N;
  char a[1000];
  int t;
  cin>>t;
  for(int i=1;i<=t;i++)
  {
      scanf("%s",a);
      int M=strlen(a);
      scanf("%d",&N);
      if(flips(a, M, N, 1)==INF)
      printf("Case #%d: IMPOSSIBLE\n",i);
      else
      printf("Case #%d: %d\n",i,flips(a, M, N, 1));
  }
}