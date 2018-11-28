#include <iostream>
using namespace std;
bool isTidy(int n)
{
	while(n>0)
	{
		int last=n%10;
		int slast=(((n%100)-last)/10);
		if(last>=slast)
			n=n/10;
		else
			return false;
	}
	return true;
}
int main()
{
	int t;
	cin>>t;
	int arr[t];
	for(int i=0;i<t;i++)
		cin>>arr[i];
	//cout<<"ANSWER"<<endl;
	for(int i=0;i<t;i++)
	{
		for(int j=arr[i];j>0;j--)
		{
			if(isTidy(j))
			{
				cout<<"Case #"<<i+1<<": "<<j<<endl;
				break;
			}
		}
	}
	return 0;
}
