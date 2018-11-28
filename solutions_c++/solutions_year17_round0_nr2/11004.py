#include <bits/stdc++.h>
#define LL long long
using namespace std;
bool tidy(int n)
{
    int last=n%10;
    n/=10;
    while(n)
    {
        if(n%10>last)return 0;
        last=n%10;
        n/=10;
    }
    return 1;
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n,x=1; cin>>t;
    while(t--)
    {
        cin>>n;
        while(n)
        {
            if(tidy(n)){cout<<"Case #"<<x++<<": "<<n;break;}
            n--;
        }
        if(t)cout<<'\n';
    }
return 0;
}
