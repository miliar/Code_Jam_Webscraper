#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define sc(x) scanf("%d",&x)
#define scll(x) scanf("%lld",&x)
#define scs(x) scanf("%s",x)
#define fr(i,a,b) for(int i = a; i < b; i++)
#define fre(i,a,b) for(int i = a; i <= b; i++)
#define clr(a,v) memset(a,v,sizeof a)

#define N 112
int t,n,r,c;

char M[N][N];
bool mark[N][N];

void go(int i, int j){
    if (M[i][j] == '?' || mark[i][j]) return;

    int maxi = 1;
    int L,R,D,U;
    L = R = j;
    D = U = i;

    int cnt,can;
    fr(i1,0,r){
      if (i1 > i) break;
      fr(i2,i1,r){
        //printf("trying c:%c i1:%d i2:%d\n",M[i][j],i1,i2);
        if (i2 < i) continue;
        fr(j1,0,c){
          if (j1 > j) break;
          fr(j2,j1,c){
            if (j2 < j) continue;
            //printf("trying c:%c i1:%d i2:%d j1:%d j2:%d\n",M[i][j],i1,i2,j1,j2);
            cnt = 0;
            can = 1;
            fre(i3,i1,i2){
              if (!can) break;
              fre(j3,j1,j2){
                if (M[i3][j3] == '?') cnt++;
                else if (M[i3][j3] == M[i][j]) continue;
                else {
                  can = 0;
                  break;
                }
              }
            }
            if (can){
              //printf("can c:%c i1:%d i2:%d j1:%d j2:%d\n",M[i][j],i1,i2,j1,j2);
              if ((i2-i1+1)*(j2-j1+1) > maxi){
                maxi = (i2-i1+1)*(j2-j1+1);
                L = j1, R = j2;
                U = i1, D = i2;
              }
            }
          }
        }
      }
    }

    //printf("c:%c L:%d R:%d U:%d D:%d maxi:%d\n",M[i][j],L,R,U,D,maxi);

    fre(i2,U,D){
      fre(j2,L,R){
        M[i2][j2] = M[i][j];
        mark[i2][j2] = 1;
      }
    }

}

int main() {
    sc(t);
    fre(ca,1,t) {
      printf("Case #%d:\n",ca);
      sc(r), sc(c);
      fr(i,0,r) scs(M[i]);
      clr(mark,0);

      fr(i,0,r)
        fr(j,0,c)
          go(i,j);

      fr(i,0,r) puts(M[i]);


    }
    return 0;
}
