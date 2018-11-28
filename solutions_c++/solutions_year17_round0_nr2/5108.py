//
// Created by Tinsley, Bryan on 4/7/17.
//


#include <cstdio>
#include <iostream>
#include <fstream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;

int t, x, l;
char n[20];

bool isTidy(long long num){


    int d1 = num % 10;
    num = (num - d1) / 10;
    int d2 = num % 10;
    num = (num - d2) / 10;

    while(d1 >= d2 && d2 != 0) {
        d1 = d2;
        d2 = num % 10;
        num = (num - d2) / 10;
    }

    return num==0;

}

string nextTidy(){
    if(l==1)
        return string(n);
    string sn;
    int e=l-2;
    sn = string(1, n[l-1]);
    while(e>=0) {
        if(n[e]>n[e+1]) {
            sn = string(1, n[e] - 1) + string((l - 1) - e, '9');
            n[e] -= 1;
        }else
            sn = string(1, n[e]) + sn;
        e--;
    }
    if(sn[0]=='0')
        sn.erase(0,1);
    return sn;
}

void apply() {
    scanf("%d", &t);
    while (t--) {
        scanf("%s", n);
        l = strlen(n);
        printf("Case #%d: ", ++x);
        printf("%s\n", nextTidy().c_str());


    }
}

int main() {
    apply();
    return 0;
}