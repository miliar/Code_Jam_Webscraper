#include <iostream>
#include <string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for (int i = 1; i <=t; ++i)
	{
		int r,c;
		cin>>r>>c;
		char **input=new char*[r];
		int* ps=new int[r];
		for (int j = 0; j < r; ++j)
		{
			input[j]=new char[c];
			cin>>input[j];
		}
		for (int j = 0; j < r; ++j)
		{
			int p=0;
			for (int k = 0; k < c; ++k)
			{
				if(input[j][k]=='?')
					continue;
				else
				{
					for (int l = p; l < k; ++l)
					{
						input[j][l]=input[j][k];
					}
					p=k+1;
				}
			}
			if(p<=c)
			{
				for (int k = p; k < c; ++k)
				{
					input[j][k]=input[j][p-1];
				}
			}
			ps[j]=p;
		}
		int x=0;
		for (int j = 0; j < r; ++j)
		{
			if(ps[j]==0)
				continue;
			else
			{
				for (int k = x; k < j; ++k)
				{
					input[k]=input[j];
				}
				x=j+1;
			}
						
		}
		if(x==1)
		{
			for (int j = 1; j < r; ++j)
			{
				input[j]=input[0];
			}
		}
		else
		{
			for (int j = x; j < r; ++j)
			{
				input[j]=input[x-1];
			}
		}
		cout<<"Case #"<<i<<":\n";
		for (int j = 0; j < r; ++j)
		{
			cout<<input[j]<<endl;
		}
	}
}