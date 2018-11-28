//
//  main.cpp
//  2017_CodeJam
//
//  Created by mjbox on 2017. 4. 7..
//  Copyright © 2017년 mjbox. All rights reserved.
//
#include <stdio.h>
#include <iostream>

#define SUBMIT
#define MAX(a,b) (a) > (b) ? (a) : (b)

using namespace std;
struct RESULT {
     long long min;
     long long max;
};
int T = 0;
 long long stalls;
 long long people;

RESULT last( long long d,  long long p) {
    RESULT result = {0,0};
    
    if(d <= p)
        return result;
    
     long long data[2][2] = {{d,1},{0,0}};
     long long step = 1;
    
    while(p > step) {
         long long data2[2][2] = {{0,0}, {0,0}};
        
        for(int i = 0; i < 2; i++) {
            if(data[i][0] == 0) continue;
            
            if((data[i][0] & 1) == 1) {
                if(data2[0][0] <= (data[i][0] >> 1)) {
                    data2[0][0] = (data[i][0] >> 1);
                    data2[0][1] += data[i][1] * 2;
                } else{
                    data2[1][0] = (data[i][0] >> 1);
                    data2[1][1] += data[i][1] * 2;
                }
            } else {
                data2[0][0] = (data[i][0] >> 1);
                data2[0][1] += data[i][1];
                data2[1][0] = (data[i][0] >> 1)-1;
                data2[1][1] += data[i][1];
            }
        }
        
        p -= step;
        step *= 2;
        data[0][0] = data2[0][0];
        data[0][1] = data2[0][1];
        data[1][0] = data2[1][0];
        data[1][1] = data2[1][1];
    }
    
    //cout << data[0][0] << "," << data[0][1] << "," << data[1][0] << "," << data[1][1] << "," << p << endl;
    int c = data[0][0];
    if(data[0][1] < p)
        c = data[1][0];
    
    result.min = result.max = c / 2;
    if((c & 1) != 1)
        result.min = MAX(0, result.min-1);
        
    return result;
}

int main(){
    // insert code here...
#ifdef SUBMIT
    FILE *fp = fopen("/Users/mjbox/Desktop/Stalls/output.txt", "w");
#endif
    cin >> T;
    for(int t = 0; t < T; t++) {
        cin >> stalls >> people;
        
        RESULT result = last(stalls, people);
        
#ifdef SUBMIT
        fprintf(fp, "Case #%d: %lld %lld\n", t+1, result.max, result.min);
#else
        cout << stalls << ", " << people << " : " << result.max << " " << result.min << endl;
#endif
    }
    
#ifdef SUBMIT
    fclose(fp);
#endif
    return 0;
}
