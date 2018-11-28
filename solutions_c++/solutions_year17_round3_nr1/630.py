//
//  main.cpp
//  17_round_1C_A
//
//
//
//

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    freopen("A-large.in.txt", "r", stdin);
    freopen("A-large.out.txt", "w", stdout);
    int t, n, k;
    long long ans=0, ans1;
    pair<long long, long long> pancake[1005];
    scanf("%d", &t);
    for(int i=1; i<=t; i++){
        memset(pancake, 0, sizeof(pancake));
        ans=ans1=0;
        scanf("%d %d", &n, &k);
        for(int j=0; j<n; j++){
            scanf("%lld %lld", &pancake[j].first, &pancake[j].second);
            pancake[j].second*=(2ll*pancake[j].first);
            pancake[j].first*=pancake[j].first;
        }
        sort(pancake, pancake+n);
        pancake[n].first=0;
        pancake[n].second=0;
        for(int j=n-1; j>=k-1; j--){
            if(pancake[j].first!=pancake[j+1].first){
                for(int l=0; l<j; l++) swap(pancake[l].first, pancake[l].second);
                sort(pancake, pancake+j);
                ans1=pancake[j].first+pancake[j].second;
                for(int l=1; l<k; l++) ans1+=pancake[j-k+l].first;
                if(ans1>ans) ans=ans1;
                for(int l=0; l<j; l++) swap(pancake[l].first, pancake[l].second);
                sort(pancake, pancake+j);
            }
        }
        printf("Case #%d: %.6lf\n", i, ans*M_PI);
    }
    return 0;
}
