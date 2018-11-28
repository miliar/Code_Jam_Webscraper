#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> ii;
typedef pair<int,int> dd;

#define sc(x) scanf("%d",&x)
#define scs(x) scanf("%s",x)
#define fr(i,a,b) for(int i = a; i < b; i++)
#define fre(i,a,b) for(int i = a; i <= b; i++)
#define clr(a,v) memset(a,v,sizeof a)
#define F first
#define S second

#define N 112
int t,c,j,st,en,ans;
ii C[N], J[N];

int main(){
    sc(t);
    fre(ca,1,t){
      printf("Case #%d: ",ca);
      sc(c), sc(j);
      fr(i,0,c){
        sc(st), sc(en);
        C[i] = ii(st,en);
      }
      sort(C,C+c);
      fr(i,0,j){
        sc(st), sc(en);
        J[i] = ii(st,en);
      }
      sort(J,J+j);

      int tot = c+j;
      if (tot == 1){
        ans = 2;
      } else if (c == 2){
        tot = 0;
        tot += C[0].S - C[0].F;
        tot += C[1].S - C[1].F;
        if (tot + C[1].F - C[0].S <= 720) ans = 2;
        else if (tot + (1440-C[1].S) + C[0].F <= 720) ans = 2;
        else ans = 4;
      } else if (j == 2){
        tot = 0;
        tot += J[0].S - J[0].F;
        tot += J[1].S - J[1].F;
        if (tot + J[1].F - J[0].S <= 720) ans = 2;
        else if (tot + (1440-J[1].S) + J[0].F <= 720) ans = 2;
        else ans = 4;
      } else {
        ans = 2;
      }


      printf("%d\n",ans);

    }
    return 0;
}
