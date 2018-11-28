#include <iostream>
#include <queue>
#include <cmath>
using namespace std;
priority_queue <int> q;
int main()
{
	int T;
	cin>>T;
	int k,i,j,n,a,l,r;
	for(i=1;i<=T;i++)
	{
		cin>>n>>k;
		while(!q.empty())
		{
			q.pop();
		}
		q.push(n);
		for(j=0;j<k;j++)
		{
			a=q.top();
			q.pop();
			if(a%2==1)
			{
				l=r=a/2;
				if(a/2!=0)
				{
					q.push(a/2);
					q.push(a/2);
				}
			}
			else
			{
				l=a/2-1;
				r=a/2;
				if(l!=0)
				{
					q.push(l);
				}
				q.push(r);
			}
		}
		cout<<"Case #"<<i<<": "<<max(l,r)<<" "<<min(l,r)<<endl;
	}
	return 0;
}
