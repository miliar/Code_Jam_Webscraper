#include <iostream>
#include <utility>
#include <queue>
#include <map>

using namespace std;
typedef unsigned long long int ull;

int main(int argc, char **argv)
{
	int t,k=1;
	ull i,n,p,a,b,y;
	pair<ull,ull> x;
	cin>>t;
	while(k<=t)
	{
		cin>>n>>p;
		priority_queue <ull> q;
		map<ull,ull> m;
		pair<ull,ull> temp(n,1);
		m.insert(temp);
		q.push(n);
		i=1;
		while(i<p)
		{
			y=q.top();
			q.pop();
			a=m[y];
			
			if(a>1)
			{
				m[y]--;
				q.push(y);
			}
			else
			{
				m.erase(y);
			}
			a=(y-1)/2;
			b=(y-1)-a;
			if(a==b)
			{
				if(m.find(b)!=m.end())
				{
					m[b]=m[b]+2;
				}
				else
				{
					q.push(b);
					m[b]=2;
				}
			}
			else
			{
				if(m.find(b)!=m.end())
				{
					m[b]=m[b]+1;
				}
				else
				{
					q.push(b);
					m[b]=1;
				}
				if(m.find(a)!=m.end())
				{
					m[a]=m[a]+1;
				}
				else
				{
					q.push(a);
					m[a]=1;
				}
			}
			i++;
		}
		y=q.top();
		q.pop();
		a=(y-1)/2;
		b=(y-1)-a;
		if(a>b)
		{
			i=b;
			b=a;
			a=i;
		}
		cout<<"Case #"<<k<<": ";
		cout<<b<<" "<<a<<endl;
		k++;
	}
}
