#include <bits/stdc++.h>
using namespace std;

#define sc(x) scanf("%d",&x)
#define scs(x) scanf("%s",x)
#define fr(i,a,b) for(int i = a; i < b; i++)
#define fre(i,a,b) for(int i = a; i <= b; i++)
#define clr(a,v) memset(a,v,sizeof a)

#define N 1123
int t,n,k;
bool up[N];
char str[N];

int main(){
    sc(t);
    fre(ca,1,t){
      printf("Case #%d: ",ca);
      scs(str);
      n = strlen(str);
      sc(k);

      fr(i,0,n) up[i] = (str[i] == '+');

      int ans = 0;

      fr(i,0,n-k+1){
        if (!up[i]){
          ans++;
          fr(j,i,i+k) up[j] = !up[j];
        }
      }

      bool ok = 1;
      fr(i,0,n) ok &= up[i];

      if (ok) printf("%d\n", ans);
      else puts("IMPOSSIBLE");

    }
    return 0;
}
