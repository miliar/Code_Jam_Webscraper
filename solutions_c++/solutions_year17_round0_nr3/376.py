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

int main(void) {
    uint32 T;

    scanf("%u", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
    	uint64 N, K;
		uint64 P;
		uint64 max=0, min=0, r;
		uint64 K_max, K_min;

        /* Test Case run once */
        scanf("%llu %llu", &N, &K);

		//printf("{DBG} N=%llu, K=%llu\n", N, K);

		/* caculate P */
		P=1;
		while (pow(2, P) <= K)
		{
//			printf ("ERR: pow(2, P) = %llu, K = %llu", pow(2, P), K);
			P++;
		}
		//printf("{DBG} P = %llu\n", P);

		min = (N - (pow(2, P) - 1)) / pow(2, P);
		//printf("{DBG} N = %llu\n", N);
		if ((N < (pow(2, P) - 1)) || ((N - (pow(2, P) - 1)) < (min * pow(2, P))))
		{
			r = 0;
		}
		else
		{
			r = (N - (pow(2, P) - 1)) - (min * pow(2, P));
		}
		max = (r > 0)? (min + 1) : (min);

		//printf("{DBG} P = %llu, min = %llu, max = %llu, r = %llu\n", P, min, max, r);

		/* K's min */
		if ((r > pow(2, P-1)) && ((r - pow(2, P-1)) > (K - (pow(2, P-1)))))
		{
			K_min = max;
		}
		else
		{
			K_min = min;
		}

		/* K's max */
		if (r > (K - pow(2, P-1)))
		{
			K_max = max;
		}
		else
		{
			K_max = min;
		}

        /* Print */
    	printf("Case #%d: %llu %llu\n", Ti, K_max, K_min);
    }

    return 0;
}

