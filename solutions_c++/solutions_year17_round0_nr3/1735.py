#include <stdio.h>
#include <iostream>

using namespace std;

int main(){
 int T ;
 cin >> T;

 for (int t= 1; t<= T ;t++) {

    long long N,K;
    cin >> N;
    cin >> K;

    //cout << N << " " << K << "\n";
    long long M,m,cM,cm,y,z,cy,cz;

    m = N;
    cm = 1;
    cM = 0;

    while (1) {
        cy = 0;
        cz = 0;

        if (cM > 0) {
            K -= cM;
            if ( K <= 0 ){
                break;
            }


            M--;

            if (M%2 == 1){
                z = M/2;
                y = z+1;
                cy = cz = cM;
            } else {
                y = M/2;
                cy += cM*2;
            }
        }

        if (cm > 0) {

            M = m;
            cM = cm;

            K -= cM;
            if ( K <= 0 ){

                break;
            }

            M--;

            if (M%2 == 1){
                z = M/2;
                y = z+1;
                cy += cM;
                cz += cM;
            } else {
                z = M/2;
                cz += cM*2;
            }
        }

        M = y;
        cM = cy;
        m = z;
        cm = cz;
    }

    printf("Case #%d: ",t);

    M--;
    z = M/2;
    y = z + (M%2);
    cout << y << " " << z << "\n";
 }



}
