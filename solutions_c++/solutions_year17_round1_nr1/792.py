#include <bits/stdc++.h>

#define pii pair<int, int>
#define pll pair<LL, LL>
#define F first
#define S second
#define B begin()
#define E end()
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

#define PI (4 * atan(1))

using namespace std;

int t, r, c;
char s[30][30];
bool ch[30], ok[30], sc;

void fill(int x, int y, char z)
{
	if(y > 0)
	{
		if(s[x][y - 1] == '?')
		{
			s[x][y - 1] = z;
			fill(x, y - 1, z);
		}
	}
	if(y < c - 1)
	{
		if(s[x][y + 1] == '?')
		{
			s[x][y + 1] = z;
			fill(x, y + 1, z);
		}
	}
}

int main()
{
	// freopen("D:\\Computer\\TestingArea\\test.in", "r", stdin);
	// freopen("D:\\Computer\\TestingArea\\test.out", "w", stdout);

	// freopen("A-large.in", "r", stdin);
	// freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    for(int z = 1; z <= t; ++z)
    {
    	scanf("%d %d", &r, &c);
    	for(int i = 0; i < r; ++i)
    		scanf("%s", s[i]);

    	for(int i = 0; i < r; ++i)
    	{
    		ok[i] = false;
    		ch[i] = false;
    		for(int j = 0; j < c; ++j)
    		{
    			if(s[i][j] != '?')
    			{
    				sc = true;
    				ch[i] = true;
    				continue;
    			}
    		}
    	}

    	for(int i = 0; i < r; ++i)
    	{
    		for(int j = 0; j < c; ++j)
    		{
    			if(ch[i] && s[i][j] != '?')
    			{
    				fill(i, j, s[i][j]);
    				ok[i] = true;
    			}
    			if(!ch[i] && ok[i - 1])
    			{
    				s[i][j] = s[i - 1][j];
    				ok[i] = true;
    			}
    		}
    	}

    	for(int i = r - 1; i >= 0; --i)
    	{
    		for(int j = 0; j < c; ++j)
    		{
    			if(!ok[i])
    				s[i][j] = s[i + 1][j];
    		}
    	}

    	printf("Case #%d:\n", z);
    	for(int i = 0; i < r; ++i)
    	{
    		for(int j = 0; j < c; ++j)
    			printf("%c", sc? s[i][j]: 'A');
    		printf("\n");
    	}
    }
    return 0;
}