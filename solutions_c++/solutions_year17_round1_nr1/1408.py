#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i = 0; i<t; i++)
	{
		int r, c;
		cin>>r>>c;
		char a[30][30];
		for(int j = 0; j<r; j++)
			for(int k = 0; k<c; k++)
				cin>>a[j][k];
		for(int j = 0; j<r; j++)
		{
			for(int k = 0; k<c; k++)
			{
				if(a[j][k]!='?')
				{
					for(int p = k + 1; p<c; p++)
						if(a[j][p] == '?')
							a[j][p] = a[j][k];
						else
							break;
					for(int p = k - 1; p>=0; p--)
						if(a[j][p] == '?')
							a[j][p] = a[j][k];
						else
							break;
				}
			}
		}
		for(int j = 0; j<(r - 1); j++)
		{
			for(int k = 0; k<c; k++)
				if(a[j][k] != '?' && a[j + 1][k] == '?')
					a[j + 1][k] = a[j][k];
		}
		for(int j = r - 1; j>0; j--)
		{
			for(int k = 0; k<c; k++)
				if(a[j][k] != '?' && a[j - 1][k] == '?')
					a[j - 1][k] = a[j][k];
		}
		cout<<"Case #"<<i + 1<<":"<<endl;
		for(int j = 0; j<r; j++)
		{
			for(int k = 0; k<c; k++)
				cout<<a[j][k];
			cout<<endl;
		}
	}
}
