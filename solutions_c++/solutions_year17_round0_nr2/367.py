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
#define S_MAX   (18 +1)

int main(void) {
    uint32 T;

    scanf("%u", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
    	char cmpChr;
		char S[S_MAX];
		char R[S_MAX];
		char A[S_MAX];
		int32 length;
		int32 dec;
		int32 i, j, k;

		/* clear memory */
		memset(&R, 0x00, sizeof(R));

        /* Test Case run once */
        scanf("%s", &S[0]);
		length = strlen(S);

		//printf("S: %s (length = %d)\n", S, length);
		dec = 0;
		cmpChr = S[(length - 1)];
		for (i=(length - 1); i >= 0; i--)
		{
			/* R's related position */
			j = (length - 1) - i;

			R[j] = S[i];	/* copy */

			//printf("DBG1: j=%d, R[j]=%c, dec = %d\n", j, R[j], dec);

			/* need to decrease */
			if ((dec > 0) || (cmpChr < R[j]))
			{
				if (R[j] > '0')
				{
					R[j] -= 1;
					dec = 0;
				}
				else
				{
					R[j] = '9';
					dec = 1;
				}

				for (k=(j - 1); k>=0; k--)
				{
					R[k] = '9';
				}
			}

			//printf ("DBG2: j=%d, DBG: R = %s, dec = %d\n", j, R, dec);

			cmpChr = R[j];
		}

		R[length] = '\0';	/* end of line */

		/* prepair the answer */
		for (k=(length); k>0; k--)
		{
			if (R[k-1] == '0')
				R[k-1] = '\0';
			else
				break;
		}
		
		memset(&A, 0x00, sizeof(A));
		length = k;
		while (k > 0)
		{
			A[(length - k)] = R[k - 1];
			k--;
		}

        /* Print */
    	printf("Case #%d: %s\n", Ti, A);
    }

    return 0;
}

