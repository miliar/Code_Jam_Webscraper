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
#define MAXN 1010

using namespace std;

char vet[MAXN];

int main() {
//    freopen("oversized_pancake_flipper_large.txt", "r", stdin);
//    freopen("oversized_pancake_flipper_large_out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int caso;
    for (caso=1; caso<=t; caso++) {
        int n;
        int k;
        scanf("%s %d", vet+1, &k);
        n=strlen(vet+1);
        int i, j;
        int res=0;
        for (i=1; i+k-1<=n; i++) {
            if (vet[i]=='-') {
                res++;
                for (j=1; j<=k; j++) {
                    if (vet[i+j-1]=='-') {
                        vet[i+j-1]='+';
                    }
                    else {
                        vet[i+j-1]='-';
                    }
                }
            }
        }
        int pode=1;
        for (i=1; i<=n; i++) {
            if (vet[i]=='-') {
                pode=0;
            }
        }
        //printf("** %s\n", vet+1);
        if (pode==1) {
            printf("Case #%d: %d\n", caso, res);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n", caso);
        }
    }
    return 0;
}










