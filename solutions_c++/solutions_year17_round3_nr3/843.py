#include <bits/stdc++.h>
using namespace std;
#define eps 0.00000001
int t,n,k;
double res,u,xin,temp,prob;
vector<double> v;

void cari(double a, double b){
    double mid = (a+b)/2;
    double sisa = u;
    for (int i = 0; i < v.size(); i++){
        if (v[i] >= mid) continue;
        sisa -= (mid-v[i]);
    }
    if (sisa < 0){
        if (b-a <= eps) return;
        cari(a,mid);
    } else {
        res = max(res,mid);
        if (b-a <= eps) return;
        cari(mid,b);
    }
}

int main(){
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        scanf("%d %d", &n, &k);
        scanf("%lf", &u);
        xin = 0;
        v.clear();
        for (int j = 0; j < n; j++){
            scanf("%lf", &temp);
            v.push_back(temp);
            xin += (1-temp);
        }
        if (xin <= u){
            printf("Case #%d: 1\n",i);
            continue;
        }
        res = 0;
        cari(0,1);
        prob = 1;
        for (int j = 0; j < k; j++){
            prob *= max(res,v[j]);
        }
        printf("Case #%d: %lf\n", i,prob);
    }
}
