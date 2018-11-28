#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
using namespace std;

#define fi first
#define se second

typedef long long int lli;

pair<int,int> pancakes[1001];

bool cmp(pair<int,int> a, pair<int,int> b) {
    lli ares = (lli)a.fi * (lli)a.se;
    lli bres = (lli)b.fi * (lli)b.se;
    return ares > bres;
}

long double eval(pair<int,int> *pancakes, int n, int k) {
    lli res = 0;
    for(int i = n-1;i>=k-1;i--) {
        lli tempRes = pancakes[i].fi * (lli) pancakes[i].fi;
        tempRes += pancakes[i].fi * (lli) pancakes[i].se * 2;
        pair<int,int> sorted_ones[1001];
        int l=0;
        for(int j=i-1; j>=0; j--, l++)
            sorted_ones[l] = pancakes[j];
        sort(sorted_ones, sorted_ones+l, cmp);
        for(int j=0;j<k-1;j++) tempRes += sorted_ones[j].fi * (lli)sorted_ones[j].se * 2;
        res = max(res, tempRes);
    }
    return res*M_PI;
}


int main() {
    int t;
    cin >> t;
    int cse = 1;
    while(t--) {
        int n,k;
        cin >> n >> k;
        for(int i=0;i<n;i++)
            cin >> pancakes[i].fi >> pancakes[i].se;
        sort(pancakes, pancakes+n);
        printf("Case #%d: %.9Lf\n", cse++, eval(pancakes, n, k));
    }

}
