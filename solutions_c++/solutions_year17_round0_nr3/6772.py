#include <bits/stdc++.h>
using namespace std;
int main() {
    long long n,k,y,ans,t,i,x;
    cin>>t;
    for(x=1;x<=t;x++) {
        cin>>n>>k;
        priority_queue<long long> p;
        p.push(n);
        for(i=0;i<k-1;i++)
        {
            y=p.top();
            p.pop();
            if(y%2!=0)
            {
               p.push(y/2);
               p.push(y/2);
            }
            if(y%2==0)
            {
                p.push(y/2);
                p.push(y/2 - 1);                  
            }
        }
        ans=p.top();
        cout<<"Case #"<<x<<": ";
        if(ans%2==0)
        {
            printf("%lld %lld\n",ans/2,ans/2 - 1);
        }
        else
        {
            printf("%lld %lld\n",ans/2,ans/2);
        }
    }
    return 0;
}
