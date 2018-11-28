#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("oneA.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int a = 1 ; a <= t ;a++){
        int n,d;
        scanf("%d%d",&d,&n);
        double x[n];
        for(int i = 0 ; i < n ; i++){
            double q,w;
            scanf("%lf%lf",&q,&w);
            x[i] = (d-q) / w;
        }
        sort(x,x+n);
        double las = x[n-1];
        double ans = d/las;
        printf("Case #%d: %6f\n",a,ans);

    }


}
