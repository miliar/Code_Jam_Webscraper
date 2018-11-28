#include <bits/stdc++.h>
using namespace std;

#define EPS      1e-9
#define F        first
#define S        second
#define pi       acos(-1)
#define ll       long long
#define inf      0x3f3f3f3f
#define sz(x)    (int)x.size()
#define sc(x)    scanf("%d",&x)
#define all(x)   x.begin(),x.end()
#define rall(x)  x.rbegin(),x.rend()

int T;
char s[1010];
int k;

int main() {
#ifndef ONLINE_JUDGE
  freopen("A-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  sc(T);
  for(int C=1;C<=T;++C){
    scanf("%s%d",s,&k);
    int out=0;
    for(int i=0;s[i+k-1];++i){
      if(s[i]=='+')continue;
      ++out;
      for(int j=i;j<i+k;++j)
        s[j]=(s[j]=='+'?'-':'+');
    }
    int bad=0;
    for(int i=0;s[i];++i)
      bad+=s[i]=='-';
    if(bad)printf("Case #%d: IMPOSSIBLE\n",C);
    else printf("Case #%d: %d\n",C,out);
  }
}
