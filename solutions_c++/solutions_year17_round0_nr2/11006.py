#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <sstream>
#include <math.h>

using namespace std;

long long isTidy(long long t){
    unsigned int diglen = 0;
    long long x = 0;
    long long n = t;
    do{
        diglen++;
        n /= 10;
    } while (n);
    int arr[diglen];
    for(int i = diglen-1; i >= 0; i--){
        arr[i] = t % 10;
        t /= 10;
    }
    int prevint = 0;
    for(int j = 0; j < (diglen); j++){
        if(arr[j] < prevint){
            long long xx = 1;
            for(int k = j; k < diglen; k++) xx += arr[k]*pow(10, diglen-(k+1));
            return xx;
        }
        prevint = arr[j];
    }
    return 0;
}

int main(){
    ofstream out("out.out");
    std::cout.rdbuf(out.rdbuf());

    ifstream is("b.in");
    string a;
    getline(is, a);
    int t = atoi(a.c_str());
    for(int i = 1; i <= t; i++){
        string sx; getline(is, sx);
        long long k = atoll(sx.c_str());
        //cout << "k = " << k << endl;
        long long l;
        long long sum = 1;
        for(l = k; l > 0; l-= sum){
            long long kxk = isTidy(l);
            if(kxk != 0) sum = kxk;
            else break;
        }
        cout << "Case #" << i << ": " << l << endl;
    }
}