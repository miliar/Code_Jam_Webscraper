#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int T ;
    cin >> T;

    for (int t = 1 ; t<= T; t++){


        int N , C ,M;
        cin >> N;
        cin >> C;
        cin >> M;

        //int T[1111][1111] = {};
        int B[1111] = {};
        int P[1111] = {};
        for (int i = 0 ; i < M ; i++){

            int p,b;
            cin >> p;
            cin >> b;
            //T[p-1][b-1]++;
            B[b-1]++;
            P[p-1]++;
        }
        int maxB = 0;
        for (int i = 0 ; i < C ; i++){
            //printf("B[%d] = %d\n",i,B[i]);
            if (B[i] > maxB) {
                maxB = B[i];
            }
        }
        //printf("maxB = %d\n",maxB);
        int sumP = 0;
        for (int i = 0 ; i < N ; i++) {
            //printf("P[%d] = %d\n",i,P[i]);
            sumP += P[i];
            int aP = sumP / (i+1);
            aP += (sumP%(i+1) > 0)?1:0;
            if (aP > maxB) {
                maxB = aP;
            }
        }
        int ans2= 0;
        for (int i = 0 ; i < N; i++){
            if (P[i] > maxB){
                ans2 += P[i] - maxB;
            }
        }

        printf("Case #%d: %d %d\n",t,maxB,ans2);
    }

}
