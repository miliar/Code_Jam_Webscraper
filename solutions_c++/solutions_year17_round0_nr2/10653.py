#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

vector<int> v = { 1,2,3,4,5,6,7,8,9 };

int check(string s)
{
	int i, f = 0;
	
	for (i = 1; i<s.length(); i++)
	{
		//cout << s << endl;
		//cout << "(int)(s[i]) : " << (int)(s[i]) << "(int)(s[i - 1]) : " << (int)(s[i - 1]) << endl;
		//cout << "Diff : " << ((int)(s[i]) - (int)(s[i - 1])) << endl<<endl;
		
		if (0<= ((int)(s[i]) - (int)(s[i - 1])) )
		{
			continue;
		}
		else
		{
			f = 1;
			break;
		}
	}
	if (f == 1)
		return 0;
	else
		return 1;

}
int main()
{
	int t = 0, n = 0, i = 10,len;
	string s;
	while (v.size() / sizeof(int) != 1000)
	{
		if (i % 10 == 0)
		{
			i++;
			continue;
		}	
		else
		{
			s = to_string(i);
			if (check(s) && i%10!=0) 
				v.push_back(i);
			i++;
		}
	}
	/*for (i = 0; i < 200; i++)
		cout << v[i] << endl;
		*/
	len = v.size() / sizeof(int);
	cin >> t;
	for (int j = 1; j <= t; j++)
	{
		cin >> n;
		for (i = 0; i < len; i++)
		{
			if (v[i] > n)
			{
				cout << "Case #" << j << ": " << v[i-1] << endl;
				break;
			}
			else if(v[i]==n)
			{
				cout << "Case #" << j << ": " << v[i] << endl;
				break;
			}
		}
	}
/*	for (i = 0; i <= t;i++)
	{
		cin >> n;
		cout << "Case #" << i << ": " << v[n - 1]<<endl;
	}*/
}
