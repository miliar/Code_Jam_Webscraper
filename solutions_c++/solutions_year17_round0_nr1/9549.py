#include<iostream>
#include<string>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	int k;
	int t = 1;
	string s;
	int ans = 0;
	bool flag = 1;
	while (t<=T)
	{
		ans = 0;
		flag = 1;
		cin >> s >> k;
		int len = s.length();
		for (int i = 0; i < len - k + 1; i++)
		{
			if (s[i] == '-')
			{
				for (int j = 0; j < k; j++)
				{
					if (s[i + j] == '-')
						s[i + j] = '+';
					else
						s[i + j] = '-';
				}
				ans++;
			}
		}
		for (int i = len - k + 1; i < len; i++)
		{
			if (s[i] != '+')
				flag = 0;
		}
		cout << "Case #" << t << ": ";
		if (flag == 0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout<<ans << endl;
		t++;
	}
	return 0;
}

//int main()
//{
//	int T;
//	cin >> T;
//	int t = 1;
//	string s;
//	while (t <= T)
//	{
//		cin >> s;
//		int len = s.length();
//		if (s[len - 1]<s[len - 2])
//		{
//			s[len - 2]--;
//			s[len - 1] = '9';
//		}
//		for (int i = len - 2; i > 0; i--)
//		{
//			if (s[i] < '0'||s[i]<s[i-1])
//			{
//				s[i] = '9';
//				s[i - 1]--;
//			}
//			while (s[i]>s[i + 1])
//				s[i]--;
//		}
//		while (s[0]>s[1])
//			s[0]--;
//
//		if (s[0] != '0')
//			cout << s[0];
//		for (int i = 1; i < len; i++)
//			cout << s[i];
//		cout << endl;
//	}
//	return 0;
//}