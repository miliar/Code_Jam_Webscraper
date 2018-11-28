#include "stdio.h"
#include "string.h"
#include <iostream>

struct pair
{
	int d;
}p[10000];

int main()
{
	using namespace std;
	FILE * finp;
	FILE * foutp;
    char buf[1001];
	int t;
	
	finp = fopen("A-large.in", "r");
	foutp = fopen("1.out", "w");
	fscanf(finp, "%d", &t);
	
	for (int i = 0; i<t; ++i)
	{
		int n;
        int rs = 0;
        fscanf(finp, "%s %d", buf, &n);
        int len = strlen(buf);

        for (int j = 0;j <= len - n;++j)
        {
            if (buf[j] == '-')
            {
                ++rs;
                for (int k = 0;k != n;++k)
                {
                    buf[j + k] = (buf[j + k] == '+' ? '-' : '+');
                }
            }
        }
        for (int j = len - 1;j >= 0;--j)
        {
            if (buf[j] == '-')
            {
                rs = -1;
                break;
            }
        }
        if (rs >= 0)
            fprintf(foutp, "Case #%d: %d\n", i + 1, rs);
        else
            fprintf(foutp, "Case #%d: IMPOSSIBLE\n", i + 1);
	}

	fclose(finp);
	fclose(foutp);

	return 0;
}
