#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int tt,n;
string s;
int k;

int main() {
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);

  cin >> tt;
  for (int ii=1;ii<=tt;++ii) {
    cin >> s >> k;
    n=s.size();
    int cnt=0;
    for (int i=0;i<=n-k;++i)
      if (s[i]=='-') {
        cnt++;
        for (int j=i;j<i+k;++j)
          if (s[j]=='-') s[j]='+';
          else s[j]='-';
      }
    bool flag=true;
    for (int i=0;i<n;++i)
      if (s[i]=='-') {
        flag=false;
        break;
      }
      
    printf("Case #%d: ",ii);
    if (flag) printf("%d\n",cnt);
    else printf("IMPOSSIBLE\n");
  }
}