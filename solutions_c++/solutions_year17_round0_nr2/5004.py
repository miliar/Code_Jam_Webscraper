#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t, z=0;
	scanf("%d", &t);
	while (t--)
	{
		string str;
		cin >> str;
		string ans = str;
		while (1)
		{
			int flag = 0;
			for (int i=0; i<str.size()-1; i++)
			{
				if(flag == 1) str[i] = '9';
				else if(str[i] > str[i+1]){
					str[i]--;
					flag = 1;
				}
			}
			if(flag == 1) str[str.size()-1] = '9';
			else break;
		}
		int flag = 0;
		cout << "Case #" << ++z << ": ";
		for (int i=0; i<str.size(); i++)
		{
			if(!flag && str[i] == '0') continue ;
			else {
				flag = 1;
				cout << str[i];
			}
		}
		cout << endl;
	}
}
