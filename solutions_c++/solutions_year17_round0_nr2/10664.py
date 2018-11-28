#include <iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;
		int l;
		int latest=n;
		int circle=0;
		while(n)
		{
			int last=n%10;
			n=n/10;
			if(circle==0)
			{
				l=latest%10;
				circle=1;
			}
			if(!(l>=last))
			{
				latest--;
				n=latest;
				circle=0;
			}
			l=last;
		}
		cout<<"case #"<<i+1<<": "<<latest<<endl;
	}
	return 0;
}