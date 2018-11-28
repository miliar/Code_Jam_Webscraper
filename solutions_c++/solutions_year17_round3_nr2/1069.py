#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <vector>
#include <math.h>
#include <algorithm>

int main()
{
int N;
scanf("%d", &N);
char ch[10000];
int k;
gets(ch);
//cake c[1005];

for(int I=1; I<=N; ++I)
{
	int ac, aj;
	scanf("%d%d",&ac,&aj);
	gets(ch);
	int ac1s, ac1e;
	int ac2s, ac2e;
	int aj1s, aj1e;
	int aj2s, aj2e;
	if(ac == 1)
		scanf("%d%d", &ac1s, &ac1e);
	else if(ac == 2)
	{
		scanf("%d%d%d%d", &ac1s, &ac1e, &ac2s, &ac2e);
		if( ac2s < ac1s )
		{
			int temp = ac2s; ac2s = ac1s; ac1s = temp;
			temp = ac2e; ac2e = ac1e; ac1e = temp;
		}
	}
	else
		assert(ac == 0);
	if(aj == 1)
		scanf("%d%d", &aj1s, &aj1e);
	else if(aj == 2)
	{
		scanf("%d%d%d%d", &aj1s, &aj1e, &aj2s, &aj2e);
		if( aj2s < aj1s )
		{
			int temp = aj2s; aj2s = aj1s; aj1s = temp;
			temp = aj2e; aj2e = aj1e; aj1e = temp;
		}
	}
	else
		assert(aj == 0);
	
	int swap = 2;
	if(ac == 0)
	{
		if(aj == 2)
		{
			assert(aj2e > aj2s && aj2s > aj1s);
			if( aj2e - aj1s > 720 && aj1e+1440-aj2s>720 )
			{
				swap = 4;
			}
		}
	}
	else if(aj == 0)
	{
		if(ac == 2)
		{
			assert(ac2e > ac2s && ac2s > ac1s);
			if( ac2e - ac1s > 720 && ac1e+1440-ac2s>720 )
			{
				swap = 4;
			}
		}
	}
	else
	{
		assert(ac == 1 && aj == 1);
		int minc = ac1e-ac1s;
		int minj = aj1e-aj1s;
		if( ac1s > aj1e )
		{
		}
	}
	
printf("Case #%d: %d\n", I, swap);
// for(int i=0; i<r; ++i)
	// puts(cake[i]);


}

return 0;
}