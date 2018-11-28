#include<bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

ull ten[19];
ull num;

ull solve(ull cur,ull ten,int lst)
{
    if(ten==0)
        return cur;
    for(int i=9;i>=lst;i--)
        if(cur*ten*10 + (ten*10-1)/9*i<=num)
            return solve(cur*10+i,ten/10,i);
    return -1;
}

inline int countDigits(ull x)
{
    if(x==0)
        return 1;
    int ret=0;
    while(x)
        x/=10,ret++;
    return ret;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("2017-B-large.in","r",stdin);
    freopen("2017-B-large.out","w",stdout);
    ten[0]=1;
    for(int i=1;i<=18;i++)
        ten[i]=ten[i-1]*10;
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";

        cin>>num;
        cout<<solve(0,ten[countDigits(num)-1],0)<<"\n";
    }
    return 0;
}
