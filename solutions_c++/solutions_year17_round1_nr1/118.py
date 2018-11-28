#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

#define cin fin
#define cout fout

ifstream fin("a.in");
ofstream fout("a.out");

char a[30][30];

int main()
{
	int Test;
	cin >> Test;
	for(int t = 1; t <= Test; t++)
	{
		int ans = 0;
		int n, m;
		cin >> n >> m;
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				cin >> a[i][j];
		
		for(int i = 1; i <= n; i++)
			for(int j = 2; j <= m;j++)
				if(a[i][j - 1] != '?' && a[i][j] == '?')
					a[i][j] = a[i][j - 1];
		for(int i = 1; i <= n; i++)
			for(int j = m - 1; j >= 1; j--)
				if(a[i][j + 1] != '?' && a[i][j] == '?')
					a[i][j] = a[i][j + 1];
		for(int i = 1; i <= m; i++)
			for(int j = 2; j <= n;j++)
				if(a[j - 1][i] != '?' && a[j][i] == '?')
					a[j][i] = a[j - 1][i];
		for(int i = 1; i <= m; i++)
			for(int j = n - 1; j >= 1; j--)
				if(a[j + 1][i] != '?' && a[j][i] == '?')
					a[j][i] = a[j + 1][i];
		
		cout << "Case #" << t << ":" << endl;
		for(int i = 1; i <= n; i++)
		{
			for(int j = 1; j <= m; j++)
				cout << a[i][j];
			cout << endl;
		}
	}
	
	return 0;
}

