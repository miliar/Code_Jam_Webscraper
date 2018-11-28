#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <string>
using namespace std;

string solve();

int main()
{
//	FILE* fp = fopen("output.txt","w");
	int T;	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		string ans = solve();
		printf("Case #%d: %s\n", tc, ans.c_str());
//		fprintf(fp,"Case #%d: %s\n", tc, ans.c_str());
	}
}

string solve()
{
	char inp[22];	scanf("%s", inp);
	string N(inp);
	bool changed = true;
	while (changed)
	{
		changed = false;
		bool flag = true;
		int start;
		for (start = 1; start < N.size(); ++start)
			if (N[start - 1] != '0') break;
		for (int i = start; i < N.size(); ++i)
		{
			if (N[i - 1] > N[i])
			{
				
				if (flag)
				{
					flag = false;
					--N[i - 1];
					N[i] = '9';
				}
				else
				{
					N[i] = '9';
				}
				changed = true;
			}
		}
	}
	string ret;
	int start;
	for (start = 0; start < N.size(); ++start)	if (N[start] != '0')break;
	for (int i = start; i < N.size(); ++i)
	{
		ret += N[i];
	}
	return ret;
}