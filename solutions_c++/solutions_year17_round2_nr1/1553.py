#include<cstdio>


using namespace std;

int testy, cel, konie, pocz, pr;

int main() {

    scanf("%d", &testy);


    for (int licz=1; licz<=testy; ++licz) {
        scanf("%d", &cel);
        scanf("%d", &konie);
        double czas = (double)0.0;
        for (int i=0; i<konie; ++i) {
            scanf("%d", &pocz);
            scanf("%d", &pr);
            if ( czas<(double)(cel-pocz)/(double)pr ) czas = (double)(cel-pocz)/(double)pr;
        }
        double odp = (double)cel/(double)czas;
        printf("Case #%d: %.6lf\n", licz, odp);
    }


    return 0;
}
