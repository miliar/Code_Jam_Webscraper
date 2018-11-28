#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

vector<ll>tidys;
void rec(ll n)
{
    if(n>1e18)return;

    tidys.push_back(n);
    for(int i=n%10;i<=9;i++)
    {
        rec(n*10+i);
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,t=0;
    ll val;
    for(int i=1;i<=9;i++)rec(i);
    sort(tidys.begin(),tidys.end());
    cin>>T;
    while(T--)
    {
        cin>>val;
        printf("Case #%d: %I64d\n",++t,*(upper_bound(tidys.begin(),tidys.end(),val)-1));

    }
    return 0;
}
