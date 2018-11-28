#include "iostream"
#include "cstdio"
#include "cstdlib"
#include "string.h"
#include "vector"
#include "map"
#include "algorithm"

#define ll long long
#define ull unsigned long long

struct node
{
    int cnt;
    int pos;

    bool operator < (const node& no) const
    {
        return cnt > no.cnt;
    }
};

node a[6];

char GetChar(int x)
{
    switch (x)
    {
    case 0:
        return 'R';
    case 1:
        return 'O';
    case 2:
        return 'Y';
    case 3:
        return 'G';
    case 4:
        return 'B';
    case 5:
        return 'V';
    default:
        return ' ';
    }
}

int main()
{
    freopen("B-small-attempt0 (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while(T--)
	{
        cas++;
        int n;
        scanf("%d", &n);
        for (int i = 0; i < 6; i++)
        {
            a[i].pos = i;
            scanf("%d", &a[i].cnt);
        }
        std::sort(a, a+6);
        if (a[0].cnt > a[1].cnt + a[2].cnt)
        {
            printf("Case #%d: IMPOSSIBLE\n", cas);
            continue;
        }
        std::string s;
        for (int i = 0; i < a[0].cnt; i++)
            s += GetChar(a[0].pos);
        for (int i = 0; i < a[1].cnt; i++)
            s = s.substr(0, 2*i+1) + GetChar(a[1].pos) + s.substr(2*i+1);
        if (a[1].cnt == a[0].cnt)
        {
             for (int i = 0; i < a[2].cnt; i++)
                s = s.substr(0, 2*i+1) + GetChar(a[2].pos) + s.substr(2*i+1);
        }
        else
        {
            for (int i = 0; i < a[0].cnt - a[1].cnt; i++)
                s = s.substr(0, 2*i+1+2*a[1].cnt) + GetChar(a[2].pos) + s.substr(2*i+1+2*a[1].cnt);
            int haha = a[1].cnt + a[2].cnt - a[0].cnt;
            for (int i = 0; i < haha; i++)
                s = s.substr(0, 2*i+1) + GetChar(a[2].pos) + s.substr(2*i+1);
        }
        printf("Case #%d: %s\n", cas, s.c_str());
	}
	return true;
}
