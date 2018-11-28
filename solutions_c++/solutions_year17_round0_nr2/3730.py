#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std;

char s[100];
int len;

long long get_ans()
{
	char pre = s[0];
	long long ans = 0;
	for (int i = 0;i < len;++ i)
	{
		if (s[i] < pre)
		{
			-- ans;
			for (int j = i-1;j >= 0;-- j)
			{
				s[j] = ans % 10 + '0';
				ans /= 10;
			}
			for (int j = i;j < len;++ j)
				s[j] = '9';
			return get_ans();
		}
		ans = ans * 10 + s[i] - '0';
		pre = s[i];
	}
	return ans;
}

int main(int argc, char *argv[])
{	
	if (argc == 1)
	{
		freopen("in", "r", stdin);
		freopen("out","w",stdout);
	}
	else
	{
		if (freopen(argv[1], "r",stdin) == NULL)
		{
			cerr << "open file failed" << endl;
			return 0;
		}
		freopen("ans","w",stdout);
	}
	int n;
	cin >> n;
	for (int T = 1;T <= n;++ T)
	{
		cin >> s;
		len = strlen(s);
		long long ans = get_ans();
		cout << "Case #" << T << ": ";
		cout << ans << endl;
	}
	return 0;
}
