//
// Created by Tinsley, Bryan on 4/7/17.
//
//
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



int l;
char s[2000];
int t;
int x;
int k;


bool isSmiley(int i){
    if(s[i] == '+')
        return true;
    else
        return false;
}

bool isAllSmiley(){
    for(int i =0; i<l;i++)
        if(s[i] != '+')
            return false;
    return true;
}

void flip(int b, int e){
    for(int i =b; i<e;i++)
        if(isSmiley(i))
            s[i] = '-';
        else
            s[i] = '+';
}
bool flipPancakes(){
    int b=0;
    int e=l;
    int c =0;
    while(e-b >= k){
        if(!isSmiley(b)){
            flip(b,b+k);
            c++;
        }
        if(!isSmiley(e-1)){
            flip(e-k,e);
            c++;
        }
        b++;
        e--;
    }

    printf("Case #%d: ", ++x);
    if(isAllSmiley())
        printf("%d", c);
    else
        printf("IMPOSSIBLE");
    printf("\n");
}

int apply() {
    scanf("%d", &t);
    while (t--) {
        scanf("%s", s);
        scanf("%d", &k);
        l = strlen(s);
        flipPancakes();

    }
}

int main() {
    apply();
    return 0;
}