#include <iostream>
using namespace std;
int main()
{
	
	int t;
	cin >> t;
	
	for (int tc = 1; tc <= t; tc++)
	{
		char ch[50][50];
		int r, c;
		cin >> r >> c;
		
		
		for (int i = 0; i<r; i++)
		{
			for (int j = 0; j<c; j++)
			{
				cin >> ch[i][j];

			}
		}
		cout << "Case #" << tc << ":" << endl;		
		for (int i = 0; i<r; i++)
		{
			for (int j = 0; j<c; j++)
			{
				if (ch[i][j] == '?')
				{
					int flag = 0;
					for (int i1 = j - 1; i1 >= 0; i1--)
					{
						if (ch[i][i1] != '?')
						{
							ch[i][j] = ch[i][i1];
							flag = 1;
							break;
						}
					}
					if (!flag)
					{
						for (int i1 = j + 1; i1<c; i1++)
						{
							if (ch[i][i1] != '?')
							{
								ch[i][j] = ch[i][i1];
								flag = 1;
								break;
							}
						}

					}
				}
			}
		}
		int mark = 0;
		for (int i = 0; i<r; i++)
		{
			for (int j = 0; j<c; j++)
			{
				if (ch[i][j] == '?')
				{
					mark = 0;
					for (int k = i + 1; k<r; k++)
					{
						if (ch[k][0] != '?'){
							mark = 1;
							for (int j = 0; j<c; j++) ch[i][j] = ch[k][j];
							break;
						}
					}
					if (mark == 0)
					{
						for (int k = i - 1; k >= 0; k--)
						{
							if (ch[k][0] != '?'){
								mark = 1;
								for (int j = 0; j<c; j++) ch[i][j] = ch[k][j];
								break;
							}
						}
					}
				}
			}
		}

		for (int i = 0; i<r; i++)
		{
			for (int j = 0; j<c; j++) cout << ch[i][j];
			cout << endl;
		}
	}
	return 0;
}