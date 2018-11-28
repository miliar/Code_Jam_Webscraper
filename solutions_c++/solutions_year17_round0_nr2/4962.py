#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t, i, flag, j, k;
	//cout <<"hello0" << endl;
	string num;
	cin >> t;
	//cout <<"hello00" << endl;
	char store[t][20];
	for(i = 0; i < t; i++)
		for(j = 0; j < 20; j++)
			store[i][j] = '\0';
	//cout <<"hello0" << endl;
	for(i = 0; i < t; i++)
	{
		flag = 0;
		cin >> num;
		//cout <<"hello1" << endl;
		for(j = 0; j < num.length() - 1; j++)
		{
			if(num[j] > num[j + 1])
			{
				if(j == 0 && num[j] == '1')
				{
					num[0] = 0;
					flag = 1;
					for(k = j + 1; k < num.length(); k++)
						num[k] = '9';
					break;
				}
				num[j]--;
				for(k = j + 1; k < num.length(); k++)
					num[k] = '9';
				if(j - 2 >= -1) j = j - 2;
			}
		}
		//cout <<"hello2" << endl;
		if(flag == 0)
		{
			for(j = 0; j < num.length(); j++)
				store[i][j] = num[j];
		}
		else
		{
			for(j = 1; j < num.length(); j++)
				store[i][j-1] = num[j];
		}
		//cout << "Case #" << i + 1 << ": " << store[i] << endl;
	}
	for(i = 0; i < t; i++)
		cout << "Case #" << i + 1 << ": " << store[i] << endl;
	return 0;
}