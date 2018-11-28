#include "stdio.h"
#include "string.h"
#include <iostream>


int main()
{
	using namespace std;
	FILE * finp;
	FILE * foutp;
    char buf[20];
	int t;
	
	finp = fopen("B-large.in", "r");
	foutp = fopen("1.out", "w");
	fscanf(finp, "%d", &t);
	
	for (int i = 0; i<t; ++i)
	{
		int n;
        char * rs = buf;
        fscanf(finp, "%s", buf);
        int len = strlen(buf);

        for (int i = 0;i != len - 1;++i)
        {
            if (buf[i] > buf[i + 1])
            {
                for (int j = i + 1;j != len;++j)
                {
                    buf[j] = '9';
                }
                --buf[i];
                for (int j = i;j != 0;--j)
                {
                    if (buf[j] < buf[j - 1])
                    {
                        buf[j] = '9';
                        --buf[j - 1];
                    }
                }
            }
        }

        while (*rs == '0')
            ++rs;
        fprintf(foutp, "Case #%d: %s\n", i + 1, rs);

	}

	fclose(finp);
	fclose(foutp);

	return 0;
}
