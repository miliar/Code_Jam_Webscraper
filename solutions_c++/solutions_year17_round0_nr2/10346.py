#include<iostream>
using namespace std;

bool order(long long int n)
{
	long long int last,cur;
	if(n<10) return true;
	last=n%10;
	n=n/10;
	while(n)
	{
		cur=n%10;
		if(cur>last) return false;
		n=n/10;
		last=cur;
	}
	return true;
}

long long int smallesttidy(long long int n)
{
	for(long long int i=n;i>0;i--)
	{
		if (order(i)) return i;
	}
	
}

int main()
{
	long long int i,t,n;
	
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		cout<<"Case #"<<i<<": "<<smallesttidy(n);
		cout<<endl;
	}
}
