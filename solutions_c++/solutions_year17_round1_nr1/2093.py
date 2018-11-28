#include<bits/stdc++.h>

using namespace std;

char a[25][25];

int main()
{
	freopen("in1.txt","r",stdin);
	freopen("out1.txt","wb",stdout);
	int t;
	int test = 1;
	cin >> t;

	while(t--)
	{
		int n;
		int m;
		cin >> n;
		cin >> m;
		getchar();
		for(int i = 0;i < n;i++)
		{
			cin >> a[i];
		}

		for(int i = 1;i < n;i++)
		{
			for(int j = 0;j < m;j++)
			{
				if(a[i][j] == '?')
				{
					a[i][j] = a[i-1][j];
				}
			}
		}

		for(int i = n-2;i >= 0;i--)
		{
			for(int j = m-1;j >= 0;j--)
			{
				if(a[i][j] == '?')
				{
					a[i][j] = a[i+1][j];
				}
			}
		}

		for(int i = 1;i < m;i++)
		{
			for(int j = 0;j < n;j++)
			{
				if(a[j][i] == '?')
				{
					a[j][i] = a[j][i-1];
				}
			}
		}

		for(int i = m-2;i >= 0;i--)
		{
			for(int j = n-1;j >= 0;j--)
			{
				if(a[j][i] == '?')
				{
					a[j][i] = a[j][i+1];
				}
			}
		}


		printf("Case #");
		printf("%d",test);
		printf(":\n");
		for(int i = 0;i < n;i++)
		{
			for(int j = 0;j < m;j++)
			{
				cout << a[i][j];
			}
			cout << endl;
		}
		test++;
	}
	return 0;
}


