#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <string>

#define MAXN 1005
using namespace std;

struct Horse
{
    double k;
    double s;
    double t;

    bool operator<(const Horse& rhs)const{
        return k<rhs.k;
    }
};

Horse h[MAXN];
int n, d;

void solve()
{
    scanf("%d%d", &d, &n);
    for(int i=0;i<n;i++){
        scanf("%lf%lf", &h[i].k, &h[i].s);
    }

    sort(h, h+n);
    for(int i=n-1;i>=0;i--){
        h[i].t=(d-h[i].k)/h[i].s;
        if(i<n-1&&h[i].t<h[i+1].t){
            h[i].t=h[i+1].t;
        }
    }

    printf("%.6lf\n", d/h[0].t);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;  cin >> t;
    for(int i=1;i<=t;i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
