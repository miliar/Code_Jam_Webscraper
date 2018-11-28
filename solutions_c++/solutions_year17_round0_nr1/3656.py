#include<iostream>
//#include<fstream>
#include<string.h>
#include<algorithm>
using namespace std;
//ifstream cin("input.txt");
//ofstream cout("output.txt");
int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		char Data[1010] = { 0, };
		cin >> Data;
		int K;
		cin >> K;
		int len = strlen(Data);
		int ans = 0;
		for (int i = 0; i <= len - K; i++)
		{
			if (Data[i] == '-')
			{
				ans++;
				for (int j = i; j < i + K; j++)
				{
					if (Data[j] == '-')
						Data[j] = '+';
					else
						Data[j] = '-';
				}
			}
		}
		int flag = 0;
		for (int i = 0; i < len; i++)
			if (Data[i] == '-')
				flag = 1;
		if (flag)
			cout << "Case #" << t + 1 << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}