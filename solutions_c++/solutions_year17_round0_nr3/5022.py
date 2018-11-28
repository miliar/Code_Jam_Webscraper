#include <iostream>
#include <queue>
using namespace std;
int main()
{
	int t,e,n,k,ans;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		priority_queue<int> pq;
		cin>>n>>k;
		pq.push(n);
		for(int i=0;i<k-1;i++)
		{
			e=pq.top();
			pq.pop();
			if(e%2!=0)
			{
                pq.push(e/2);
                pq.push(e/2);
            }
            else
            {
                pq.push(e/2);
                pq.push(e/2 - 1);                  
            }
        }
        ans=pq.top();
        if(ans%2!=0)
        	printf("Case #%d: %d %d\n",j,ans/2,ans/2);
        else
        	printf("Case #%d: %d %d\n",j,ans/2,ans/2-1);
    }
}