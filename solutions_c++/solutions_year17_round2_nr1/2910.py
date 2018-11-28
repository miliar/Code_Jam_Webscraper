//
//  CodeJamRound1B.cpp
//  GoogleCodeJam2017
//
//  Created by Aniket p Ghanawat on 22/04/17.
//  Copyright © 2017 Aniket P Ghanawat. All rights reserved.
//

#include "main.h"
using namespace std;

void solution1BA(){
    int T,N;
    ul D,K[1001],S[1001];
    double curr,V,max;
    cin >> T;
//    cout.precision(6);
//    cout.setf(ios::fixed, ios::floatfield );
    for(int i = 1; i <= T; i++){
        cin >> D >> N;
        max = 0;
        for(int j = 1; j <= N; j++){
            cin >> K[j] >> S[j];
            if( max < (D-K[j])/double(S[j]))
                max = (D-K[j])/double(S[j]);
        }
        printf("Case #%d: %.6f\n",i,D/max);
    }
}

void solution1BB(){

}

void solution1BC(){

}
