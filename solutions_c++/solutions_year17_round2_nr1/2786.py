#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define s(x) scanf("%lld" , &x)

double k[10000] , s1[10000];

int main()
{
    ll p = 0;
    freopen("in1.txt" , "r" , stdin);
    freopen("out1.txt" , "w" , stdout);
    ll t;
    s(t);
    while(t--){
        p ++;
        ll n , i;
        double d , mx1;
        scanf("%lf" , &d);
        s(n);
        mx1 = 0;
        for(i = 0; i < n; i ++){
            scanf("%lf" , &k[i]);
            scanf("%lf" , &s1[i]);
            if((d-k[i])/s1[i] > mx1){
                mx1 = (d-k[i])/s1[i];
            }
        }
        //cout << mx1 << endl;
        printf("Case #%lld: %.7lf\n" , p , d/mx1);
       // cout << "Case #" << p <<": " << d/mx1 << endl;
    }
    return 0;
}
