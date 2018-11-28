#include "bits/stdc++.h"
using namespace std;
typedef long long ll;

int main()
{
	int t;
	cin>>t;
	for(int case1=1;case1<=t;case1++)
	{
		int n,k;
		scanf("%d %d",&n,&k);
		priority_queue<int>pq;
		printf("Case #%d: ",case1);
		/*if(k>n/2)
		{
			printf("0 0\n");
			continue;
		}*/
		pq.push(n);
		int m1,m2;
		while(k--)
		{
			n=pq.top();
			pq.pop();
			if(n%2==0)
			{
				int mid=n/2;
				m1=mid,m2=mid-1;
				pq.push(m1);
				if(m2>=0)
				pq.push(m2);
			}
			else
			{
				int mid=n/2;
				m1=mid,m2=mid;
				pq.push(m1);
				pq.push(m2);
			}
		}
		printf("%d %d\n",m1,m2);
	}

	return 0;
}
