#include <iostream>
using namespace std;

bool tidy(int x)
{
	int l=x;
	int p;
	
	do
	{
		p=l%10;
		l=l/10;
		if(l%10>p)
		return false;
	} while(l!=0);
	
	return true;
}

int t(int n)
{
	if (n<10)
	return n;
	
	for(int x=n; x>8; x--)
	{
		if(tidy(x)==1)
		{
			return x;
		}
	}
}

int main()
{
	int m;
	cin>>m;
	for(int x=0; x<m; x++)
	{
		int n;
		cin>>n;
	
		cout<<"Case #"<<x+1<<": "<<t(n)<<endl;
	}
	
	return 0;
}
