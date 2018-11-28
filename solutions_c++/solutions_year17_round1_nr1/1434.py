#include <bits/stdc++.h>
using namespace std;


char arr[26][26];
// vector<char> vec;

// char checkleft(int i, int j)
// {

// }

int main()
{
	int t,cs=1;
	cin>>t;
	while(t--)
	{
		int r,c;
		cin>>r>>c;
		string str;
		for(int i=0;i<r;i++)
		{
			cin>>str;
			for(int j=0;j<c;j++)
			{
				arr[i][j] = str[j];
				// if(str[j]!='?')vec.push_back(str[j]);
			}
		}

		// int it=0, len = vec.size();
		for(int i=0;i<r;i++)
		{
			for(int j=1;j<c;j++)
			{
				if(arr[i][j]=='?')
				{
					arr[i][j] = arr[i][j-1];
				}
			}
		}

		for(int i=0;i<r;i++)
		{
			for(int j=c-2;j>=0;j--)
			{
				if(arr[i][j]=='?')
					arr[i][j] = arr[i][j+1];
			}
		}

		for(int i=0;i<c;i++)
		{
			for(int j=1;j<r;j++)
			{
				if(arr[j][i]=='?')
					arr[j][i] = arr[j-1][i];
			}
		}

		for(int i=0;i<c;i++)
		{
			for(int j=r-2;j>=0;j--)
			{
				if(arr[j][i]=='?')
					arr[j][i] = arr[j+1][i];
			}
		}

		cout<<"Case #"<<cs++<<":\n";
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)cout<<arr[i][j];
				cout<<endl;
		}
	}
	return 0;
}