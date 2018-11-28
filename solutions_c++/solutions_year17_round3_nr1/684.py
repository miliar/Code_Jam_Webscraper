#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>

#define MAXN 1005
#define M_PI 3.1415926535898
using namespace std;

struct Pan
{
    double r;
    double h;

    bool operator <(const Pan& rhs)const{
        return r<rhs.r;
    }
};

Pan pan[MAXN];
int n, k;

bool comp(const Pan& elem1, const Pan& elem2)
{
    return elem1.h*elem1.r>elem2.h*elem2.r;
}

void solve()
{
    scanf("%d%d", &n, &k);
    for(int i=0;i<n;i++){
        scanf("%lf%lf", &pan[i].r, &pan[i].h);
    }
    sort(pan, pan+n);

    double ans=0, temp;
    for(int i=k;i<=n;i++){
        temp=pan[i-1].r*pan[i-1].r*M_PI+pan[i-1].h*pan[i-1].r*M_PI*2.0;
        sort(pan, pan+i-1, comp);
        for(int j=0;j<k-1;j++){
            temp+=pan[j].h*pan[j].r*M_PI*2.0;
        }
        ans=max(ans, temp);
    }

    printf("%.9lf\n", ans);
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
