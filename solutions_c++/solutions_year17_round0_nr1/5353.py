#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i = 0; i<t; i++)
	{
		char a[2000];
		int k, p = 0, flag = 0;
		cin>>a>>k;
		int h = strlen(a);
		for(int j = 0; j<h; j++)
		{
			if(a[j] == '-' && (j + k)>h)
			{
				flag = 1;
				break;
			}
			else if(a[j] == '-')
			{
				for(int y = 0; y<k; y++)
				{
					if(a[j + y] == '-')
						a[j + y] = '+';
					else
						a[j + y] = '-';
				}
				p++;
			}
		}
		cout<<"Case #"<<i + 1<<": ";
		if(flag == 1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<p<<endl;
	}
}
