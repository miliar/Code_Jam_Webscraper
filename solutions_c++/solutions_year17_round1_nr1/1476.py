#include<iostream>
#include<fstream>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int main()
{
	int T;
	in >> T;
	for (int t = 0; t < T; t++)
	{
		int n, m;
		in >> n >> m;
		char Data[31][31] = { 0, };
		for (int i = 0; i < n; i++)
			in >> Data[i];

		int flag = 0;
		for (int i = 0; i < m; i++)
		{
			char now='?';
			for (int j = 0; j < n; j++)
			{
				
				if (Data[j][i] != '?') {
					now = Data[j][i];
				}
				else
					Data[j][i] = now;
			}
		}
		for (int i = 0; i < m; i++)
		{
			char now='?';
			for (int j = n-1; j >=0; j--)
			{

				if (Data[j][i] != '?') {
					now = Data[j][i];
				}
				else
					Data[j][i] = now;
			}
		}
		int notfound[31] = { 0, };
		
		for (int j = 0; j < m; j++)
		{
			for (int i = 0; i < n; i++)
			{
				if (Data[i][j] == '?') {
					notfound[j] = 1;
					break;
				}
			}
		}
		for (int j = 0; j < m; j++)
		{
			if (notfound[j])
			{
				int flag = 0;
				for (int k = j - 1; k >= 0; k--)
				{
					if (!notfound[k])
					{
						for (int i = 0; i < n; i++)
						{
							Data[i][j] = Data[i][k];
						}
						flag = 1;
						notfound[j] = 0;
						break;
					}
				}
				if (!flag)
				{
					for (int k = j + 1; k < m; k++)
					{
						if (!notfound[k]) {
							for (int i = 0; i < n; i++)
							{
								Data[i][j] = Data[i][k];
							}
							notfound[j] = 0;
							break;
						}
					}
				}
			}
		}
		out << "Case #" << t + 1 << ":\n";
		for (int i = 0; i < n; i++)
			out << Data[i] << endl;
	}
	return 0;
}