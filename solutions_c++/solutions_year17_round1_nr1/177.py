#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

string a[30];

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	cin>>T;
	for (int t = 1; t <= T; t++)
	{
		int n, m;
		cin>>n>>m;
		for (int i = 0; i < n; i++)
			cin>>a[i];
		for (int i = 0; i < n; i++)
			for (int j = 1; j < m; j++)
				if (a[i][j]=='?' && a[i][j-1] != '?')
					a[i][j] = a[i][j-1];
		for (int i = 0; i < n; i++)
			for (int j = m-2; j >= 0; j--)
				if (a[i][j]=='?' && a[i][j+1] != '?')
					a[i][j] = a[i][j+1];
		for (int i = 1; i < n; i++)
			for (int j = 0; j < m; j++)
				if (a[i][j]=='?' && a[i-1][j] != '?')
					a[i][j] = a[i-1][j];
		for (int i = n-2; i >= 0; i--)
			for (int j = 0; j < m; j++)
				if (a[i][j]=='?' && a[i+1][j] != '?')
					a[i][j] = a[i+1][j];
		cout<<"Case #"<<t<<": "<<endl;
		for (int i = 0; i < n; i++)
			cout<<a[i]<<endl;
	}
	return 0;
}