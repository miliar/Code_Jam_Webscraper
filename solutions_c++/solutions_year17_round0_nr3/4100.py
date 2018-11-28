#include<bits/stdc++.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("3.in","r",stdin);
    freopen("3.out","w",stdout);
    ll t,j=1;
    cin>>t;
    while(j<=t)
    {
        ll n,i,p,q,r,k;
        cin>>n>>k;
        priority_queue<ll> qu;
        qu.push(n);

        for(i=0;i<k;i++)
        {

            r=qu.top();
            //cout<<r<<endl;
            qu.pop();
            qu.push(r/2);
            p=r/2;q=r/2;
            if(r%2==0)
            {
                qu.push((r/2)-1);
                q=(r/2)-1;
            }
            else
            {
                qu.push(r/2);
                p=r/2;
            }
        }
        cout<<"Case #"<<j<<": "<<p<<" "<<q<<endl;
        j++;
}
}
