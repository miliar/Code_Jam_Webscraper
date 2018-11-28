//
//  main.cpp
//  17_round_1B_A
//
//
//
//

#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    freopen("A-small-attempt0.in.txt", "r", stdin);
    freopen("A-small-attempt0.out.txt", "w", stdout);
    int t, d, n;
    double m1, m2, ans;
    scanf("%d", &t);
    for(int i=1; i<=t; i++){
        scanf("%d %d", &d, &n);
        pair<double, double> horse[1005];
        for(int j=0; j<n; j++){
            scanf("%lf %lf", &horse[j].first, &horse[j].second);
        }
        horse[n].first=d*1.0;
        horse[n].second=0.0;
        sort(horse, horse+n);
        ans=0.0;
        while(abs(horse[0].first-d*1.0)>1e-6){
            m1=999999999.0;
            for(int j=0; j<n; j++){
                if(abs(horse[j].first-horse[j+1].first)<1e-6) horse[j].second=horse[j+1].second;
                else if(horse[j].second>horse[j+1].second){
                    m2=(horse[j+1].first-horse[j].first)/(horse[j].second-horse[j+1].second);
                    if(m2<m1) m1=m2;
                }
            }
            ans+=m1;
            for(int j=0; j<n; j++) horse[j].first+=m1*horse[j].second;
        }
        printf("Case #%d: %.6lf\n", i, d*1.0/ans);
    }
    return 0;
}
