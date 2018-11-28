#include <iostream>
#include <queue>
using namespace std;

int main() {
int t,tt;
cin>>t;
tt=t;
while(tt--)
{
	long long n,k;
	priority_queue<int> qu;
	cin>>n>>k;
	long long j=1,l,r,z=n;
	while(j<=k && z)
	{
		if(!qu.empty())
		{
			z=qu.top();
			qu.pop();
		}
		if(z)
			if(!(z%2))
			{
				r=z/2;
				l=r-1;
			}
			else
				l=r=(z-1)/2;
		qu.push(l);
		qu.push(r);
		j++;
	}
	cout<<"Case #"<<t-tt<<": "<<r<<" "<<l<<endl;
}
return 0;
}