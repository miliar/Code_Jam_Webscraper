#include <bits/stdc++.h>
#include <math.h>
using namespace std;
long long meh[1050][2];
int eendex[1050];
bool cmp(int x, int y){
    return meh[x][0] > meh[y][0];
}
int main(){
    freopen("A-large (1).in","r",stdin);
    freopen("A-large.txt", "w", stdout);
    int t, n, k,  tpem;
    long long arns, magx, sigh, temp, tmep,hem;
    double realarns;
    scanf("%d", &t);
    for(int ads = 0; ads<t; ads++){
        memset(meh, 0, sizeof(meh));
        scanf("%d%d", &n, &k);
      //  printf("%d\n", k);
        for(int i=0; i<n; i++){
            eendex[i] = i;
            scanf("%lld%lld", &temp, &tmep);
            meh[i][0] = temp * tmep * 2;
            meh[i][1] = temp * temp;
          //  printf("%lld %lld", meh[i][0], meh[i][1]);
        }
        sort(eendex, eendex+n, cmp);
        magx = 0;
        sigh = 0;
        arns = 0;
        for(int i=0; i<k-1; i++){
            arns+=meh[eendex[i]][0];
            if(meh[eendex[i]][1]>magx){
                magx = meh[eendex[i]][1];
                tpem = eendex[i];
            }
        }
        for(int i=k-1; i<n; i++){
            hem = meh[eendex[i]][0] + max(magx, meh[eendex[i]][1]);
         //   printf("%d %lld %lld %lld %lld\n", eendex[i], meh[eendex[i]][0], magx, meh[eendex[i]][1], hem);
            if(hem>sigh){
                sigh = hem;
            }
        }
        arns+=sigh;
        realarns = 3.141592653589793238462643383279 * arns;
        printf("Case #%d: %.9f\n",ads+1, realarns);
    }
}
