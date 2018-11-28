#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;
typedef long long LL;
const int N = 1e2+5;
char s[N];
int T,n,kase,a[N];
bool judge(){
  for(int i=2;i<=n;++i)if(a[i]<a[i-1])return false;
  return true;  
}
int main(){
    freopen("E:\\workspace\\B-large.in","r",stdin);
    freopen("E:\\out.txt","w",stdout);
    scanf("%d",&T);
    while(T--){
      printf("Case #%d: ",++kase);
      scanf("%s",s+1);
      n=strlen(s+1);
      for(int i=1;i<=n;++i)a[i]=s[i]-'0';
      if(judge()){
         printf("%s\n",s+1);
         continue;
      }
      LL ret = 0,p = 0,tmp=0;
      int k=n-1;
      while(k--)tmp=tmp*10+9;
      ret=tmp;
      for(int i=1;i<=n;++i){
        int j=a[i-1];
        if(i==1)j=1;
        for(;j<a[i];++j){
           tmp=p*10+j;
           int k=n-i;
           while(k--)tmp=tmp*10+9;
           ret=max(ret,tmp);
        }
        if(a[i]<a[i-1])break;
        p=p*10+a[i];
      }
      cout<<ret<<endl;
    }
    return 0;
}