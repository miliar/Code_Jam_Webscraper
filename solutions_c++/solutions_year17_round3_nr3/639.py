//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>
#include<cassert>

using namespace std;

#define For(i, n) for(int i = 0; i<int(n); ++i)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


int extra() {
    int n,k;
    long double P[55], Z[55], u;
    scanf("%d%d", &n,&k);
    assert(n==k);
    scanf("%Lf", &u);
    For(i, n) {
        scanf("%Lf", P+i);
    }
    sort(P, P+n);
    P[n] = 1;
    For(i, n+1) Z[i] = P[i];
    int rovnake = 1;
    while(u > eps) {
        long double dam = min(u/rovnake, Z[rovnake] - Z[rovnake-1]);
        For(i, rovnake) {
            Z[i] += dam;
            u -= dam;
        }
        if (rovnake < n) rovnake++;
        //printf("%lf %lf\n", double(dam), double(u));
    }
    long double vysledok = 1;
    For(i, n) vysledok *= Z[i];
    printf("%.10Lf\n", vysledok);
}

int main() {
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
