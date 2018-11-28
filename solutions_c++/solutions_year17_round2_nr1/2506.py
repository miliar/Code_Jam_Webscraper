#include <iostream>
#include <cstdio>
#define MAXN 1010
using namespace std;



int posIni;
int velocidade;

double maisLento;

int main (){
    int teste;
    cin >> teste;


    for(int t=1;t<=teste;t++){
        int d,n;

        cin >> d >> n;

        maisLento = -1;
        double atual;

        for(int i=0;i<n;i++){
            cin >> posIni >> velocidade;
            atual = (double)(d-posIni)/velocidade;
            if(atual > maisLento)maisLento = atual;
        }

        double resp = d/maisLento;

        cout << "Case #" << t << ": ";
        printf("%lf\n",resp);
    }

    return 0;
}
