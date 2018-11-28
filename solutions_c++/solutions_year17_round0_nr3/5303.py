//
// Created by Tinsley, Bryan on 4/7/17.
//


#include <cstdio>
#include <iostream>
#include <fstream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <math.h>

using namespace std;

void solve(long long n, long long k, long long &mn, long long &mx){

    priority_queue<long long> q;
    long long l;
    long long r;
    q.push(n);

    while(k > 0){
        n = q.top();
        q.pop();
        l = (n-1) / 2;
        r = (n-1) - l;
        q.push(max(r,l));
        q.push(min(r,l));
        k--;
        mn=min(r,l);
        mx=max(r,l);
    }
}

int apply() {
    int t, c;
    long long mn, mx;
    long long n, k;
    scanf("%d", &t);
    while (t--) {
        scanf("%lld", &n);
        scanf("%lld", &k);
        printf("Case #%d: ", ++c);
        solve(n, k, mn, mx);
        printf("%lld %lld\n", mx, mn);
    }
}


int main() {
    apply();
    return 0;
}