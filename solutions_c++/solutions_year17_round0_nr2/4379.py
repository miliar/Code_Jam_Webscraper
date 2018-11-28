#include <bits/stdc++.h>
using namespace std;
#define ll long long
bool ok(ll a)
{
    int temp = a%10;
    a/=10;
    while (a)
    {
        if(a%10>temp) return 0;
        temp = a%10;
        a/=10;
    }
    return 1;
}
int main()
{
        freopen("in.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    int T;
    cin>>T;
    int caseno = 0;
    while (T--)
    {
        ll a;
        scanf("%I64d",&a);
        printf("Case #%d: ",++caseno);
        for (;;a--)
        {
            if (ok(a))
            {
                cout<<a<<endl;
                break;
            }
        }
    }
    return 0;
}
