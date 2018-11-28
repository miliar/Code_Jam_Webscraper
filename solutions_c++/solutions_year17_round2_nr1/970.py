#include <bits/stdc++.h>
#define N 1005
using namespace std;

typedef pair<double,double> pii;
pii a[N];

void solve(int tc){
    printf("Case #%d: ",tc);
    int n; double d; scanf("%lf%d",&d,&n);
    for(int i=0;i<n;i++)
        scanf("%lf%lf",&a[i].first,&a[i].second);
    sort(a,a+n,greater<pii>());
    double t=(d-a[0].first)/a[0].second;
    for(int i=1;i<n;i++){
        t=max(t,(d-a[i].first)/a[i].second);
    }
    printf("%.10f\n",d/t);
}

int main()
{
    freopen("A-large.in","r",stdin); //freopen("out.txt","w",stdout);
    int tc; scanf("%d",&tc);
    for(int i=1;i<=tc;i++){
        solve(i);
    }
    return 0;
}
