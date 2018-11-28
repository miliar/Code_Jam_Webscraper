//
//  main.cpp
//  17_round_1B_C
//
//
//
//

#include <iostream>
#include <cstdio>
#include <cmath>

int t, n, q, maxdist[1005], speed[1005], city[1005], o, u, v;
double ans;

double f(int citynow, int ponynow, int distleft){
    if(citynow==n-1) return 0.0;
    if(distleft<=city[citynow]){
        ponynow=citynow;
        distleft=maxdist[citynow];
        return (double)city[citynow]*1.0/(double)(speed[ponynow]*1.0)+f(citynow+1, ponynow, distleft-city[citynow]);
    }
    return fmin((double)city[citynow]*1.0/(double)(speed[ponynow]*1.0)+f(citynow+1, ponynow, distleft-city[citynow]), (double)city[citynow]*1.0/(double)(speed[citynow]*1.0)+f(citynow+1, citynow, maxdist[citynow]-city[citynow]));
}

int main() {
    freopen("C-small-attempt0.in.txt", "r", stdin);
    freopen("C-small-attempt0.out.txt", "w", stdout);
    scanf("%d", &t);
    for(int i=1; i<=t; i++){
        scanf("%d %d", &n, &q);
        for(int j=0; j<n; j++) scanf("%d %d", &maxdist[j], &speed[j]);
        for(int j=0; j<n; j++){
            for(int k=0; k<n; k++){
                scanf("%d", &o);
                if(k==j+1) city[j]=o;
            }
        }
        scanf("%d %d", &u, &v);
        printf("Case #%d: %.6lf\n", i, f(0, 0, 0));
    }
    return 0;
}
