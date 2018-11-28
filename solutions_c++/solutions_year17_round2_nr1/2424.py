#include <iostream>
#include<bits/stdc++.h>
using namespace std;
pair<long long , long long> pr[1100];
int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t;
    cin>>t;
    for(int k = 1 ; k<=t ; k++)
    {
        int n;
        long long d;
        scanf("%lld%d" , &d , &n);
        double ti = 0;
        for(int i = 0 ; i<n ; i++)
        {
            scanf("%lld%lld" , &pr[i].first, &pr[i].second);
        }
        sort(pr , pr+n);
        for(int i = 0 ; i<n ; i++)
        {
            double x = ((d-pr[i].first)*1.0) / (pr[i].second*1.0);
            if(x>ti) ti = x;
        }
        printf("Case #%d: %.6f\n" , k , d/ti);
    }
    return 0;
}
