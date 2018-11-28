#include<iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int r, c;
		cin >> r >> c;
		char a[r][c];
		for (int j = 0; j < r; j++)
		{
			for (int k = 0; k < c; k++)
			{
				cin >> a[j][k];
				if (a[j][k] == '?')
				{
					if (j >= 1)
						a[j][k] = a[j-1][k];
				}
			}
		}
		for (int j = 0; j < r; j++)
		{
			for (int k = 0; k < c; k++)
			{
				if (a[j][k] == '?')
				{
					int s;
					for ( s = 0; s < r; s++)
					{
						if (a[s][k]!='?')
							break;
					}
					if (s < r)
					{
						for (int w = 0; w<s;w++)
							a[w][k] = a[s][k];
					}
					
				}
			}
		}
		
		
		for (int j = 0; j < r; j++)
		{
			for (int k = 0; k < c; k++)
			{
				if (a[j][k] == '?')
				{
					int s;
					for ( s = k-1; s >= 0; s--)
					{
						if (a[j][s]!='?')
							break;
					}
					if (s >= 0)
					{
						for (int w = s+1; w<=k;w++)
							a[j][w] = a[j][s];
					}
					else
					{
						for (s = k+1; s < c; s++)
						{
							if (a[j][s]!='?')
								break;
						}
						if (s < c)
						{
							for (int w = k; w < s; w++)
								a[j][w] = a[j][s];
						}
					}
					
				}
			}
		}
		cout << "Case #" << i+1 << ": "<<endl;
		for (int j = 0; j < r;j++)
		{
			for (int k = 0; k <c; k++)
			cout << a[j][k];
			cout << endl;
		}
		
	}
}
