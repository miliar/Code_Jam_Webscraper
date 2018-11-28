#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
int t,tmp,n,k,ans;
cin>>t;
for(int no = 1 ; no <=t ; no++)
{
priority_queue<int>pq;
cin>>n>>k;
pq.push(n);
for(int i=0;i<k-1;i++)
    {
        tmp=pq.top();
        pq.pop();
            if(tmp%2!=0)
            {
                pq.push(tmp/2);
                pq.push(tmp/2);
            }
            if(tmp%2==0)
            {
                pq.push(tmp/2);
                pq.push(tmp/2 - 1);                  
            }
        }
        ans=pq.top();
        if(ans%2!=0)
        {
            printf("Case #%d: %d %d\n",no,ans/2,ans/2);
        }
        if(ans%2==0)
        {
            printf("Case #%d: %d %d\n",no,ans/2,ans/2 - 1);
        }
    }
	return 0;
}
