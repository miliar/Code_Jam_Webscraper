#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    //freopen("C-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ll t, tt, n, k, i, j, p, q, r, s, x, y, a, b, ca, cb;
    cin>>t;
    for(tt = 1; tt <= t; tt++)
    {
        cin>>n>>k;
        a = n, b = 0, ca = 1, cb = 0;
        x = 0;
        while(2*x+1 < k)
        {
            if(a == b)
            {
                p = a/2;
                q = a-p-1;
                a = p, b = q;
                ca = cb = ca+cb;
                x += x+1;
                continue;
            }
            p = a/2;
            q = a-p-1;
            if(b)
            {
                r = b/2;
                s = b-r-1;
            }
            if(!b)
            {
                a = p, b = q, ca = cb = ca;
                x += x+1;
                continue;
            }
            if(p == q)
                a = p, b = s, ca += ca+cb;
            else
                a = p, b = q, cb += ca+cb;
            x += x+1;
        }
        x = k-x;
        printf("Case #%lld: ", tt);
        if(x <= ca)
            printf("%lld %lld\n", a/2, a-a/2-1);
        else
            printf("%lld %lld\n", b/2, b-b/2-1);
    }
    return 0;
}
