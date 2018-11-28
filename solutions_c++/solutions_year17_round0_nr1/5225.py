// ConsoleApplication3.cpp : Defines the entry point for the console application.
//

#include <time.h>
#include <stdio.h>
#include <cstdio>
#include <algorithm>
#include <map>
#include <string>
#include <iostream>

using namespace std;

string tostring(int n)
{
    string s = "";
    while (n)
    {
        s += (char)(n % 10 + '0');
        n /= 10;
    }
    return s;
}

void work()
{
    int m, ans = 0;
    string s;
    cin >> s;
    scanf("%d", &m);
	for (int i = 0; i < s.size(); ++i)
	{
	    if (i + m - 1 >= s.size()) break;
	    if (s[i] == '-')
	    {
	        ++ans;
	        for (int j = i; j <= i + m - 1; ++j)
	        {
	            if (s[j] == '-') s[j] = '+';
	            else s[j] = '-';
	        }
	    }
	}
	for (int i = 0; i < s.size(); ++i)
	{
	    if (s[i] == '-')
	    {
	        puts("IMPOSSIBLE");
	        return;
	    }
	}
	printf("%d\n", ans);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		work();
	}
    return 0;
}

