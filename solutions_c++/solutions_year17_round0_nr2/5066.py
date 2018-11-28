#include <cstdio>
#include <cstring>
#include <cmath>

#define REP(i,a,b) for(int i = (a); i < (b); ++i)
#define TAM 32

typedef unsigned long long ull;
using namespace std;


ull potencia (ull a, int b) {

    ull res = 1;

    REP(i,0,b)
        res*= a;

    return res;

}


int main () {


    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int TC;
    int k = 0;
    scanf("%d",&TC);

    while (TC--) {

        ull numero1;
        ull solucion = 0;
        char sol_temp[TAM];

        scanf("%llu",&numero1);

        int cifras, cp_cifras;
        cifras = log10(numero1) + 1;
        cp_cifras = cifras;
        cifras--;


        int anterior = 666;
        int flag = 1;

        int i = 0;
        int sol[cp_cifras];
        memset(sol,0,cp_cifras*sizeof(int));

        while (flag) {

            int actual = numero1 % 10;
            if (actual <= anterior) {
                sol_temp[i] = actual;
            }else{
                REP(j,0,i) {
                    if (sol[i])
                        break;
                    sol[j] = 1;
                    sol_temp[j] = 9;
                }
                actual--;
                sol_temp[i] = actual;
            }
            anterior = actual;
            numero1/= 10;
            i++;

            if (i > cifras)
                break;
        }

//        REP(i,0,cp_cifras){
//            printf("%d ",sol_temp[i]);
//        }

//        printf("\n");

        REP(i,0,cp_cifras) {
            solucion += sol_temp[i] * potencia(10,i);
        }

        printf("Case #%d: %llu\n",++k,solucion);

    }


return 0;
}
