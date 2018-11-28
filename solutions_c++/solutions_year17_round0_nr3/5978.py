#include <bits/stdc++.h>
using namespace std;
int main()
{
    int test,w;
    cin>>test;
    for(w=1;w<=test;w++)
    {
        priority_queue<int>pq;//priority queue taken
        int num,k;
        cin>>num>>k;
        pq.push(num);
        for(int i=0;i<k-1;i++)
        {
            int rex;
            rex=pq.top();
            pq.pop();
            if(rex%2!=0)
            {
                pq.push(rex/2);
                pq.push(rex/2);
            }
            if(rex%2==0)
            {
                pq.push(rex/2);
                pq.push(rex/2 - 1);                 
            }
          //  cout<<i<<" "<<pq.top()<<endl;
        }
        int ans=pq.top();
       // cout<<ans<<endl;
        if(ans%2!=0)
        {
            printf("Case #%d: %d %d\n",w,ans/2,ans/2);
        }
        if(ans%2==0)
        {
            printf("Case #%d: %d %d\n",w,ans/2,ans/2 - 1);
        }
        
    }
}
