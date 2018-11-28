#include <iostream>
#include <utility>
#include <queue>
using namespace std;


int main(int argc, char **argv)
{
        int t,k=1;
        unsigned long long int i,n,p,a,b;
	pair<unsigned long long int,unsigned long long int> x;
	cin>>t;
	while(k<=t)
	{
		cin>>n>>p;
		priority_queue <pair<unsigned long long int,unsigned long long int> > q;
		pair<unsigned long long int,unsigned long long int> temp(n,1);
		q.push(temp);
		i=1;
		while(i<p)
		{
		        x=q.top();
			q.pop();
			a=(x.first-1)/2;
			b=(x.first-1)-a;
			if(x.second>1)
			{
				x.second--;
				q.push(x);
			}
			if(a==b)
				q.push(make_pair(a,2));
			else
			{
				q.push(make_pair(a,1));
				q.push(make_pair(b,1));
			}
			i++;
		}
		x=q.top();
		q.pop();
		a=(x.first-1)/2;
		b=(x.first-1)-a;
		if(a>b)
		{
			i=b;
			b=a;
			a=i;
		}
		printf("Case #%d: ",k);
		cout<<b<<" "<<a<<endl;
		k++;
	}
}
