#include <iostream>
#include <stdio.h>

using namespace std;

int T, nflip, psize;
char x[100000];

int main() {
    //freopen("/Users/Tata201201/Documents/Fld_Programming/CodeJam2017/Qualification/A_Oversized\\ Pancake\\ Flipper/A-small-attempt0.in.txt","r",stdin);
    //freopen("/Users/Tata201201/Documents/Fld_Programming/CodeJam2017/Qualification/A_Oversized\\ Pancake\\ Flipper/A-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    for(int TC = 1; TC <= T; TC++){
        scanf("%s %d",x,&psize);
        int i=0;
        nflip = 0;
        for(i=0; x[i+psize-1]; i++){
            if(x[i] == '-'){
                for(int j=0;j<psize;j++){
                    x[i+j] = (x[i+j] == '-' ? '+' : '-');
                }
                nflip ++;
            }
        }
        for(;x[i];i++){
            if(x[i] != '+') nflip = -99;
        }
        if(nflip >= 0 ) printf("Case #%d: %d\n",TC,nflip);
        else printf("Case #%d: IMPOSSIBLE\n",TC);
    }
    return 0;
}