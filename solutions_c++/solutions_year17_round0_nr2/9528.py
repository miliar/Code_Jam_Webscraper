#include <iostream>
#include <string.h>
#include <cmath>

using namespace std;

unsigned long long  LastTidy(unsigned long long  N){
    unsigned long long MAX= (unsigned long long int) pow(10, 18);
    unsigned long long  aux1;
    unsigned long long  aux2;
    while(MAX > 10){
        aux1 = (N%MAX)/(MAX/10);
        aux2 = (N%(MAX/10))/(MAX/100);
        if(aux1 > aux2){
            N = N - (N%(MAX/10)+1);
            MAX= (unsigned long long int) pow(10, 18);
        }
        else{
            MAX = MAX / 10;
        }
    }

    return N;
}
int main(){
    int T;
    unsigned long long N;
    scanf("%d", &T);
    int i =1;
    while (i <= T) {
        scanf("%llu",&N);
        unsigned long long  r = LastTidy(N);
        printf("Case #%d: %llu\n",i, r);
        i++;
    }
    return 0;
}