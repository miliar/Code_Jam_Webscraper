#include<iostream>

using namespace std;

int tidy(int n)
{
	int t=n;
	int r=10,r1;
	int flag=0;
	while(t)
	{
		r1=t%10;
		t=t/10;
		if(r>=r1)
			r=r1;
		else 
		{
			flag=1;
			break;
		}
	}
	
	if(flag==1)
		return 0;
	else
		return 1;
}

int main()
{
	int t;
	cin>>t;
	int n;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		for(int j=n;j>0;j--)
		{
			if(tidy(j))
			{
				cout << "Case #" << i << ": ";
				cout<<j<<endl;
				break;
			}
		}
	}
}