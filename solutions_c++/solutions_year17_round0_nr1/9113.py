#include <iostream>
#include <cstring>
using namespace std;
string seq;
int count;

void flip(int l,int n)
{

	for(int i=0;i<n;i++)
	{
		if(seq[i+l]=='-')
			seq[i+l]='+';
		else if(seq[i+l]=='+')
			seq[i+l]='-';
	}
	return;
}

int run(int n)
{
	int i,size2=seq.length()-n+1;
	for(int i=0;i<size2;i++)
		if(seq[i]=='-')
		{
			flip(i,n);
			count++;
		}
	for(;i<seq.length();i++)
		if(seq[i]=='-')
			return 0;
	return 1;
}

int main()
{
	int n,s,end,i;
	cin>>n;
	for(i=1;i<=n;i++)
	{
		cin>>seq;
		cin>>s;
		count=0;
		end=run(s);
		cout<<"Case #"<<i<<": ";
		if(end)
			cout<<count<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}