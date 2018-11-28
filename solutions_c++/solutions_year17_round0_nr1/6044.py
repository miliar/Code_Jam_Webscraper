#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	ifstream st("in.in");
	ofstream write;
	write.open("out.expect");
	int T, a, ans, mi, pl, tmp, flag;
	string in;
	//cin >> T;
	st >> T;
	for (int i = 1; i <= T;i++)
	{
		pl = 0;
		mi = 0;
		ans = 0;
		flag = 0;
		//cin >> in >> a;
		st >> in >> a;
		for (int j = 0; j < in.length(); j++)
		{
			if (in[j] == '+')
				pl++;
			else
				mi++;

		}
		if (in.length() == 2)
		{
			if (mi == 1)
			{
				cout << "Case #" << i << ": IMPOSSIBLE" << endl;
				write << "Case #" << i << ": IMPOSSIBLE" << endl;
				continue;
			}
			else if (mi == 2)
			{
				ans = 1;
			}
			else
			{
				ans = 0;
			}
		}
		else
		{
			if (mi == 1)
			{
				cout << "Case #" << i << ": IMPOSSIBLE" << endl;
				write<< "Case #" << i << ": IMPOSSIBLE" << endl;
				continue;
			}
			else
			{
				tmp = 0;
				for (int j = tmp; j < in.length(); j++)
				{
					if (in[j] == '-')
					{
					
						for (int k = j; k < j + a; k++)
						{
							if (k >= in.length())
							{
								flag = 1;
								break;
							}
							if (in[k] == '-')
								in[k] = '+';
							else
								in[k] = '-';
						}
						if (flag == 1)
							break;
						ans++;
					}
				}
			}
		}

		if (flag == 1)
		{
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
			write << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}
		else
		{
			cout << "Case #" << i << ": " << ans << endl;
			write << "Case #" << i << ": " << ans << endl;
			continue;
		}
	}
}