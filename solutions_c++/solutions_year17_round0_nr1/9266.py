#include<iostream>
#include<conio.h>
#include<string>
#include<stdio.h>
using namespace std;
bool checktrue(string t)
{
	int sum = 0;
	int len = t.length();
	for (int j = 0; j < len; j++)
	{
		sum += (int)t[j];
	}
	if (sum % (int)t[0] == 0)
		return true;
	else
		return false;
}
void main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output_file_name.out", "w", stdout);
	int t =0, k = 0;
	string s;
	cin >> t;
	int cnt = 1;
	while(cnt<=t)
	{
		cin >> s;
		cin >> k;
		int len = s.length();
		int n = k;
		int sum = 0, count = 0;
		bool checkzero = false;
		string temps = s;
		for (int j = 0; j < len; j++)
		{
			sum += (int)s[j];
		}
		if ((sum % (int)s[0]) == 0)
		{
			checkzero = true;
		}
		for (int i = 0; i < len; i++)
		{
			if (temps[i] == '-')
			{
				for (int l = 0; l < k; l++)
				{
					if (len - i < k)
						break;
					if (temps[i + l] == '-')
						temps[i + l] = '+';
					else
						temps[i + l] = '-';
					n--;
					if (n == 0)
						n = k;
				}
				count++;

			}
		}
		if (checktrue(temps) == true && count >> 0)
		{
			
			cout << "Case #" << cnt << ": "<<count<<endl;
		}
		else if (checktrue(temps))
		{
			cout << "Case #"<<cnt<<": "<<count<<endl;
		}
		else
		{
			cout << "Case #" << cnt << ":" << " Impossible"<<endl;
		}
		cnt++;
	}
		
		
		

}