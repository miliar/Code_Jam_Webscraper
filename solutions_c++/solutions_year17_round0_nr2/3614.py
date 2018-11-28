#include<iostream>
#include<string.h>
//#include<fstream>
using namespace std;
//ifstream cin("input.txt");
//ofstream cout("output.txt");
int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		char Data[20] = { 0, };
		cin >> Data;
		int len = strlen(Data);
		for (int q = 0; q < len; q++)
		{
			for (int i = 1; i < len; i++)
			{
				if (Data[i] < Data[i - 1])
				{
					for (int j = i; j < len; j++)
						Data[j] = '9';
					Data[i - 1]--;
					break;
				}
			}
		}


		int flag = 1;
		cout << "Case #" << t + 1 << ": ";
		for (int i = 0; i < len; i++)
		{
			if (Data[i] == '0' && flag)continue;
			flag = 0;
			cout << Data[i];
		}
		cout << endl;
	}
	return 0;
}