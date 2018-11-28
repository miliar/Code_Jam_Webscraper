#include <iostream>
#include <queue>
using namespace std;

int main()
{
	long long t,k,n,c=1,a,l,r;
	
	cin>>t;
	while(t--)
	{
		cin>>n>>k;
		priority_queue<long long>q;
		q.push(n);
		for(long long i=0;i<k-1;i++)
		{
			a=q.top();
			q.pop();
			if(a%2==0)		//even
			{
				q.push(a/2);
				q.push(a/2 -1);
				}	
			else		//odd
			{
				q.push(a/2);
				q.push(a/2);
			}
		}
	
	a=q.top();
	l=a/2;
	r=a-l-1;
	
	cout<<"Case #"<<c++<<": "<<l<<" "<<r<<endl;
	}
	return 0;

}
