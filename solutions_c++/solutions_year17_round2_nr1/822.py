#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <cmath>
#include <climits>
#include <vector>
#include <queue>
#include <cstring>
#include <iterator>
#include <list>
#include <set>
#include <map>
#include <bitset>

using namespace std;

#define MEMSET(x,v) memset(x,v,sizeof(x))
template<class A, class B> inline bool mina(A &x, B y) {return (x > y)?(x=y,1):0;}
template<class A, class B> inline bool maxa(A &x, B y) {return (x < y)?(x=y,1):0;}
typedef long long int LL;

int Ks[1010];
int Ss[1010];

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        int D, N;
        scanf("%d %d", &D, &N);

        for(int i = 0; i < N; i++) {
            scanf("%d %d", Ks+i, Ss+i);
        }

        double maxT = -1;

        for(int i = 0; i < N; i++) {
            double time = (D-Ks[i])/(double)Ss[i];
            maxa(maxT, time);
        }

        printf("Case #%d: %lf\n", t, D/maxT);
    }
}
