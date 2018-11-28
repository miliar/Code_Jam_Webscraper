#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cmath>
#include <inttypes.h>

#include <string>
#include <vector>
#include <set>
#include <map>

inline int RANDOM_NUM(int from, int tillExcl) {
    int n;

    do
    {
        n = rand() / (double)RAND_MAX * (tillExcl - from) + from;
    } while(n == tillExcl);
    return n;
}


int main()
{
    srand(time(NULL));

    int numTasks;
    scanf("%d", &numTasks);

    for(int taskNo = 1; taskNo <= numTasks; taskNo++)
    {
    uint64_t D, N;
    double max = 0.0;
        
        {
        scanf("%" SCNu64 " %" SCNu64, &D, &N);
        }
        {
        for(int i = 0; i < N; i++)
        {
            uint64_t pos, speed;
            scanf("%" SCNu64 " %" SCNu64, &pos, &speed);

            double tim = D * speed / (double)(D - pos);
            if(i == 0 || max > tim)
                max = tim;
        }
        }

        printf("Case #%d: ", taskNo);
        {

        printf("%lf\n", max);

        }
    }

    return EXIT_SUCCESS;
}
