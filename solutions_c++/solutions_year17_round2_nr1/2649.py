#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <unistd.h>
#include <vector>
#include <set>

using namespace std;

int main(int argc, char** argv) {

    unsigned int T = 0;

    fscanf (stdin, "%u", &T);

    fprintf (stderr, "Doing %d testcases\n", T);

    for (size_t t = 0; t < T; ++t)
    {
    	long long int D;
    	long long int N;
        fscanf (stdin, "%lld", &D);
        fscanf (stdin, "%lld", &N);

        double maxTime = 0;
        for (int n = 0; n < N; ++n)
        {
        	unsigned long long int K;
        	unsigned long long int S;
            fscanf (stdin, "%lld", &K);
            fscanf (stdin, "%lld", &S);

            double time = (double)(D-K)/(double)S;

            if (time > maxTime)
            {
            	maxTime = time;
            }
        }
        fprintf (stdout, "Case #%d: %f\n", (int)(t+1), (double)D/maxTime);
    }
}
