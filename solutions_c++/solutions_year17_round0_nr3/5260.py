#include <cstdio>
#include <queue>

#define REP(i,a,b) for (int i = (a); i < (b); ++i)

typedef unsigned long long ull;

using namespace std;



int main () {

    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);


    int TC;
    int it = 0;
    scanf("%d",&TC);



    while (TC--) {

        ull N, K;

        priority_queue<int>espera;

        scanf("%llu %llu",&N,&K);

        espera.push(N);
        ull disp = 0, rest = 0;

        REP(i,0,K) {

            ull maximo  = espera.top();
            espera.pop();
            disp = maximo / 2;
            rest = maximo - disp;

            rest--;

            espera.push(disp);
            espera.push(rest);

        }

        printf("Case #%d: %llu %llu\n",++it,disp,rest);




    }


return 0;

}
