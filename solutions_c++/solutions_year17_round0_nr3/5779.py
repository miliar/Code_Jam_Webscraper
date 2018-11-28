#include <cmath>
#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

bool empty[1000000] = {false};
int64_t L[1000000];
int64_t R[1000000];
int64_t potential[1000000];

void docase(int casenum)
{
    int64_t N, K;
    cin >> N >> K;

    int64_t y, z, best;

    for(int s = 0; s < N; s++)
        empty[s] = true;
    
    for(int k = 0; k < K; k++)
    {
        for(int s = 0; s < N; s++)
        {
            if(empty[s])
            {
                L[s] = 0; R[s] = 0;
                for(int sl = s-1; sl >= 0 && empty[sl]; sl--, ++L[s]);
                for(int sr = s+1; sr <  N && empty[sr]; sr++, ++R[s]);

                //printf("e=%d L[%d]=%lld R[%d]=%lld\n", int(empty[s]), s, L[s], s, R[s]);
            }
        }

        int64_t best_min = -1, best_count = 0, best_s = 0;
        for(int s = 0; s < N; s++)
            if(empty[s])
                best_min = max(min(L[s], R[s]), best_min);

        for(int s = 0; s < N; s++)
        {
            if(empty[s] && min(L[s], R[s]) == best_min)
            {
                best_s = s;
                ++best_count;
            }
        }

        if(best_count > 1)
        {
            int64_t best_max = -1;
            for(int s = 0; s < N; s++)
            {
                if(empty[s] && min(L[s], R[s]) == best_min && max(L[s], R[s]) > best_max)
                {
                    best_max = max(L[s], R[s]);
                    best_s = s;
                }
            }
        }

        //printf("best_s = %lld\n", best_s);
        empty[best_s] = false;
        y = max(L[best_s], R[best_s]);
        z = min(L[best_s], R[best_s]);
    }

    printf("Case #%d: %lld %lld\n", casenum+1, y, z);
}

int main()
{
    int T;
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        docase(i);
    }
	return 0;
}
