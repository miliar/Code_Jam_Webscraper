#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
using namespace std;
char arr[30][30];
int r, c;
ofstream out("output.txt");
void f()
{
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			out << arr[i][j] ;
		}
			out << endl;
	}

}
int main()
{
	int j = 1;
	ifstream inp  ("input.txt");
	
	int t;
	inp >> t;
	
	bool x;
	while (t != 0)
	{
		inp >> r >> c;
		
		for (int i = 0; i <r; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				inp>> arr[i][j];
			}
			
		}
		for (int j = 0; j < c; ++j)
		{
			for (int i = 0; i < r; ++i)
			{
				if (arr[i][j] != '?')
				{
					for (int k = 0; k < i; ++k)
					{
						if (arr[k][j] == '?')
						{
							arr[k][j] = arr[i][j];
							
						}
					}
				}
			}

		}
		for (int j = 0; j < c; ++j)
		{
			for (int i = 0; i < r; ++i)
			{
				if (arr[i][j] != '?')
				{
					for (int k = i + 1; k < r; ++k)
					{
						if (arr[k][j] == '?')
						{
							arr[k][j] = arr[i][j];

						}
						else
							break;
					}
				}
			}

		}

		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				if (arr[i][j] != '?')
				{
					for (int k = j + 1; k < c; ++k)
					{
						if (arr[i][k] == '?')
							arr[i][k] = arr[i][j];
						else
							break;
					}

					for (int k = j-1; k >=0; --k)
					{
						if (arr[i][k] == '?')
							arr[i][k] = arr[i][j];
						else
							break;
					}

				}
			}

		}
	
			out << "Case #" << j << ": "  << endl;
			f();

		++j;
		--t;
	}
	

}