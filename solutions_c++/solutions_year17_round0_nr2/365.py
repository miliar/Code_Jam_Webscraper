#include<iostream>
#include<string>
using namespace std;
void f(int t)
{
	string s;
	cin >> s;
	for (int i = s.length() -2; i >= 0; --i)
	{
		if (s[i] > s[i + 1])
		{
			for (int j = i + 1; j < s.length(); ++j)
				s[j] = '9';
			--s[i];
		}
	}
	int x = 0;
	if (s[0] == '0')++x;
	printf("Case #%d: %s\n", t, s.c_str()+x);
}
int main()
{
	
	freopen("file.txt", "w", stdout);
	int T;
	
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		f(t);
	}

}