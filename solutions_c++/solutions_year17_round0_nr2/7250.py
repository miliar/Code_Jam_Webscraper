#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>

#define INF 1000000007

using namespace std;

unsigned long long converter(char *vet) {
    unsigned long long val;
    val=0;
    int i;
    for (i=0; vet[i]!='\0'; i++) {
        val=val*10+(vet[i]-'0');
    }
    return val;
}

int main() {
    //freopen("tidy_numbers_large.txt", "r", stdin);
    //freopen("tidy_numbers_large_out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    char aux[30];
    int caso;
    for (caso=1; caso<=t; caso++) {
        unsigned long long res=0;
        char vet[30];
        scanf("%s", vet+1);
        int tam=strlen(vet+1);
        int i, j;
        for (i=1; i<=tam+1; i++) {
            int dec=0;
            strcpy(aux+1, vet+1);
            for (j=2; j<i; j++) {
                if (vet[j]<vet[j-1]) {
                    dec=1;
                    break;
                }
            }
            if (dec==0) {
                if (i==1 || (i<=tam && vet[i]-1>=vet[i-1])) {
                    aux[i]--;
                    for (j=i+1; j<=tam; j++) {
                        aux[j]='9';
                    }
                    if (converter(aux+1)>res) {
                        res=converter(aux+1);
                    }
                   // printf("---- %s\n", aux+1);
                }
                else if (i==tam+1) {
                    if (converter(aux+1)>res) {
                        res=converter(aux+1);
                    }
                }
            }
        }
        printf("Case #%d: %llu\n", caso, res);
    }
    return 0;
}










