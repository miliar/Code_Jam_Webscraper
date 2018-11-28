#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cmath>

using namespace std;

int step[100], len;
double MAX, MIN, people;

void recursive (double num, int digit)
{   
    //printf("%lf %d\n", num, step[digit+1]);

    if(digit+1 == len) {
        if(abs(fmod(num, 2) - 1) < 0.01) {
            MAX = floor(num/2);
            MIN = MAX;
        } else {
            MAX = floor(num/2);
            MIN = floor(num/2)-1;
        }
        return;
    }
    
    if(abs(fmod(num, 2) - 1) < 0.01) //odd
        recursive(floor(num/2), digit+1);
    else { //even
        if(step[digit+1] == 0) 
            recursive(floor(num/2), digit+1);
        else
            recursive(floor(num/2)-1, digit+1);
    }
}

int main()
{
    int test;
    double stall, tmp;

    while(scanf("%d", &test) == 1) {
        for(int i = 1; i <= test; ++i) {
            memset(step, 0, sizeof(step));
            scanf("%lf %lf", &stall, &people);

            len = (int)floor(log2(people))+1;
            tmp = people;

            for(int j = len-1; j >= 0; --j) {
                if(tmp - (pow(2, j) + pow(2, j-1) - 1) < 0.1) {
                    step[j] = 0;
                    tmp = pow(2, j-1) + (tmp - pow(2, j));
                } else {
                    step[j] = 1;
                    tmp -= pow(2, j-1);
                    tmp = pow(2, j-1) + (tmp - pow(2, j));
                }
            }

            recursive(stall ,0);
            printf("Case #%d: %.0lf %.0lf\n", i, MAX, MIN);   
        }
    }

    return 0;
}