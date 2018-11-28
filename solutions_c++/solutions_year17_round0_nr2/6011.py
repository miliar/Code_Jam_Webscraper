#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	int T,flag,flag1;
	string in;
	ifstream st("in.in");
	ofstream write;
	write.open("out.expect");
	//cin >> T;
	st >> T;
	for (int i = 1; i <= T; i++)
	{
		//cin >> in;
		st >> in;
		flag = 0;
		flag1 = 0;
		for (int j = 1; j < in.length(); j++)
		{
			if (flag == 0)
			{
				if (in[j] < in[j - 1])
				{
					in[j - 1]--;
					in[j] = '9';
					flag = 1;
				}
			}
			else
			{
				in[j] = '9';
			}
		}
		flag = 0;
		for (int j = in.length() - 2; j >= 0; j--)
		{
			if (flag == 0)
			{
				if (in[j] > in[j + 1])
				{
					if (j != 0)
						in[j] = '9';
					else
						in[j]--;
					in[j + 1] = '9';
					flag = 1;
				}
			}
			else
			{
				if (in[j] == '1')
					in[j] = '0';
				else
					in[j] = '9';
			}
		}
		cout << "Case #" << i << ": ";
		write << "Case #" << i << ": ";
		for (int j = 0; j < in.length(); j++)
		{
			if (in[j] != '0')
				flag1 = 1;
			if (flag1 == 1)
			{
				cout << in[j];
				write << in[j];
			}
		}
		cout << endl;
		write << endl;
	}
}