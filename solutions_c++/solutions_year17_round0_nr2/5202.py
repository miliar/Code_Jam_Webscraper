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
    int n, ans = 0;
    scanf("%d", &n);
	for (int i = 1; i <= n; ++i)
	{
	    int t = 1;
	    string s = tostring(i);
	    //cout << s << endl;
	    for (int j = 1; j < s.size(); ++j)
	    {
            if (s[j - 1] < s[j])
                t = 0;
	    }
	    if (t)
            ans = i;
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

