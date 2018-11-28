#include<iostream>
#include<string>
using namespace std;
void f(int t)
{
	string s;
	int K;
	int num = 0;
	cin >> s >> K;
	int len = s.size();
	int i;
	for (i = 0; i <= len-K; ++i)
	{
		if (s[i] == '-')
		{
			++num;
			for (int j = 0; j < K; ++j)
				s[i+j]=s[i + j] == '-' ? '+' : '-';
		}
	}
	for (; i < len; ++i)
	{
		if (s[i] == '-')
		{
			printf("Case #%d: IMPOSSIBLE\n", t);
			return;
		}
	}
	printf("Case #%d: %d\n", t, num);
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