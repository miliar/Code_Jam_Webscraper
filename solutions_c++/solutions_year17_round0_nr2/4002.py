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

int T = 0;
int N = 0;
int M = 0;
char Data[2][20];


int main(){
    // insert code here...
#ifdef SUBMIT
    FILE *fp = fopen("/Users/mjbox/Desktop/Tidy/output.txt", "w");
#endif
    cin >> T;
    for(int t = 0; t < T; t++) {
        cin >> Data[0];
        
        int len = strlen(Data[0]);
        for(int i = 0; i <20; i++) {
            Data[1][i] = 0;
        }
        
        bool retry = true;
        while(retry) {
            retry = false;
            for(int i = 1; i < len; i++) {
                if(Data[0][i-1] > Data[0][i]) {
                    if(Data[1][i-1] == 0) Data[0][i-1]--;
                    Data[0][i] = MAX('1',Data[0][i-1]);
                    Data[1][i] = '9';
                    retry = true;
                    break;
                }
            }
        }
        bool up = false;
        for(int i = 0; i < len; i++) {
            if(up) {
                Data[0][i] = '9';
            } else {
                if(Data[1][i] != 0) {
                    Data[0][i] = '9';
                    up = true;
                }
            }
        }
        
        char* p = Data[0][0] == '0' ? &Data[0][1] : &Data[0][0];
        
#ifdef SUBMIT
        fprintf(fp, "Case #%d: %s\n", t+1, p);
#else
        cout << p << endl;
#endif
    }
    
#ifdef SUBMIT
    fclose(fp);
#endif
    return 0;
}
