#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define sc(x) scanf("%d",&x)
#define scs(x) scanf("%s",x)
#define fr(i,a,b) for(int i = a; i < b; i++)
#define fre(i,a,b) for(int i = a; i <= b; i++)
#define fred(i,a,b) for(int i = a; i >= b; i--)
#define clr(a,v) memset(a,v,sizeof a)

#define N 1123
int t,n;
ll ans;

char str[N], temp[N];

int main(){
    sc(t);
    fre(ca,1,t){
      printf("Case #%d: ",ca);
      scs(str);
      n = strlen(str);

      fred(i,n-2,0){
        if (str[i] > str[i+1]){
          str[i]--;
          fr(j,i+1,n) str[j] = '9';
        }
      }

      sscanf(str,"%lld",&ans);

      printf("%lld\n", ans);

    }
    return 0;
}
