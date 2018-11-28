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

using namespace std;

int T = 0;
int N = 0;
int M = 0;
char Data[1001];

int FlipCount(char* p, int m) {
    int count = 0;
    int c = 0;
    int d = 0;
    
    int len = strlen(p);
    bool pattern = false;
    int pc = 0;
    
    int i = 0;
    while(i < len) {
        if(p[i] == '-') {
            if(i + m <= len) {
                for(int j = 0; j < m; j++) {
                    p[j+i] = p[j+i] == '+' ? '-' : '+';
                }
                count++;
                
            }
            else return -1;
        }
        
        i++;
    }
    return count;
}

int main(){
    // insert code here...
#ifdef SUBMIT
    FILE *fp = fopen("/Users/mjbox/Desktop/Pancake2/output.txt", "w");
#endif
    
    cin >> T;
    for(int t = 0; t < T; t++) {
        cin >> Data >> M;
        
        int result = FlipCount(Data, M);
#ifdef SUBMIT
        if(result >= 0)
            fprintf(fp, "Case #%d: %d\n", t+1, result);
        else
            fprintf(fp, "Case #%d: IMPOSSIBLE\n", t+1);
#else
        cout << result << endl;
#endif
    }
    
#ifdef SUBMIT
    fclose(fp);
#endif
    return 0;
}
