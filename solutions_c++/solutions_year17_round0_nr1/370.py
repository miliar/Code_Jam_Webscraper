#include "cstring"
#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"

using namespace std;

typedef signed long long    int64;
typedef unsigned long long  uint64;
typedef signed int          int32;
typedef unsigned int        uint32;
typedef signed short        int16;
typedef unsigned short      uint16;
typedef signed char         int8;
typedef unsigned char       uint8;

#define T_MAX   (100)
#define K_MAX   (1000 + 1)
#define S_MAX   (1000 + 1)

int main(void) {
    uint32 T;

    scanf("%u", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
    	uint32 P[S_MAX];
		char S[S_MAX];
		uint32 K;
		uint32 length;
		uint32 i, j;
		int32 result;

		/* clear memory */
		memset(P, 0x00, sizeof(P));

        /* Test Case run once */
        scanf("%s %d", &S[0], &K);
		length = strlen(S);

		//printf("S: %s (length = %d)\n", S, length);
		//printf("K: %d\n", K);

		result = 0;
		for (i=0; (i + K) <= length; i++)
		{
			if (S[i] == '-')
			{
				P[i] += 1;
			}

			if (P[i] & 0x1)
			{
				/* flip */
				result += 1;
				//printf ("DBG: i=%d, result=%d\n", i, result);
				
				for (j=0; j<K; j++)
				{
					P[i+j] += 1;
				}
			}
		}

		/* check */
		while (i < length)
		{
			if (S[i] == '-')
			{
				P[i] += 1;
			}

			if (P[i] & 0x1)
			{
				result = -1;
				break;
			}

			i++;
		}

        /* Print */
		if (result == -1)
		{
			printf("Case #%d: IMPOSSIBLE\n", Ti);
		}
		else
		{
        	printf("Case #%d: %u\n", Ti, result);
		}
    }

    return 0;
}

