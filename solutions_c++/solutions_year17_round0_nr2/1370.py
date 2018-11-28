#include<cstdio>
#include<string>
#include<iostream>

using namespace std;
		
int main()
{
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++)
	{
		string s;
		cin >> s;
		printf("Case #%d: ", tt);
		int idx = s.length()-1;
		int lastChange = -1;
		while(idx >= 1)
		{
			if(s[idx] < s[idx-1])
			{
				s[idx-1]--;
				lastChange = idx;
			}
			idx--;
		}
		if(lastChange > 0)
		{
			for(int i = lastChange; i < s.length(); i++)
				s[i] = '9';
		}
		idx = (s[0] == '0') ? 1 : 0;
		while(idx < s.length())
		{
			printf("%c", s[idx]);
			idx++;
		}
		printf("\n");
	}
	return 0;
}

