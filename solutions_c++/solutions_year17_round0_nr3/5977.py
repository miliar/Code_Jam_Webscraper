#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t,q=1;
    cin>>t;
    while(t--)
    {
        priority_queue<int>pq;
        int n,k,run;
        cin>>n>>k;
        pq.push(n);
        for(int i=0;i<k-1;i++)
        {
            int x;
            x=pq.top();
            pq.pop();
            if(x%2!=0)
            {
                pq.push(x/2);
                pq.push(x/2);
            }
            if(x%2==0)
            {
                pq.push(x/2);
                pq.push(x/2 - 1);                  
            }
          //  cout<<i<<" "<<pq.top()<<endl;
        }
        int ans=pq.top();
       // cout<<ans<<endl;
        if(ans%2!=0)
        {
            printf("Case #%d: %d %d\n",q,ans/2,ans/2);
        }
        if(ans%2==0)
        {
            printf("Case #%d: %d %d\n",q,ans/2,ans/2 - 1);
        }
        q++;
    }
}