#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t,count=1;
    cin>>t;							// i am a boss
    while(t--)
    {
        priority_queue<int>pq1;
        int n,k,run;
        cin>>n>>k;
        pq1.push(n);
        for(int i=0;i<k-1;i++)
        {
            int monty;
            monty=pq1.top();				// similar to agressive cow
            pq1.pop();
            if(monty%2!=0)
            {
                pq1.push(monty/2);			// pushing in the priority queue
                pq1.push(monty/2);
            }
            if(monty%2==0)
            {
                pq1.push(monty/2);
                pq1.push(monty/2 - 1);                 // pushing in the priority queue
            }
          //  cout<<i<<" "<<pq.top()<<endl;
        }
        int answer=pq1.top();
       // cout<<ans<<endl;
        if(answer%2!=0)
        {
            printf("Case #%d: %d %d\n",count,answer/2,answer/2);		// printing the value
        }
        if(answer%2==0)
        {
            printf("Case #%d: %d %d\n",count,answer/2,answer/2 - 1);		// printing the value
        }
        count++;
    }
}
