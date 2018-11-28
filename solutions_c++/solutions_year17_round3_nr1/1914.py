#include <stdio.h>
#include <assert.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

#define all(a) a.begin(), a.end()
#define FOR(i,N) for(int i=0; i<N; ++i)
#define FORI(it,col) for(auto it = col.being(); it != col.end(); ++it)

using namespace std;

typedef unsigned long long int llu;
typedef map< llu, llu > MII;
typedef vector< llu > VI;
typedef vector<VI> VVI;

typedef pair< llu, llu > PII;
typedef vector< PII > VPII;


//#define DEBUG

#ifdef DEBUG
    #define DE(format, ...) fprintf(stderr,format, ##__VA_ARGS__)
    void DE_MII(MII &m) {
        for (MII::iterator mit = m.begin(); mit != m.end(); ++mit)
            DE(" %llu:%llu", mit->first, mit->second);
        DE("\n");
    }
    void DE_VI(VI &v) {
        for (size_t i=0; i < v.size(); ++i) {
            DE(" %llu", v[i]);
        }
        DE("\n");
    }
    #define DI for(int i=0;i<indent;i++) DE("  ");
#else
    #define DI
    #define DE(format, ...)
    #define DE_MII(m)
    #define DE_VI(v)
#endif

long double PI = 3.1415926535897932384626433832795028841971693993751058209749445923078L;

   
void solve()
{
	llu N, K;
	scanf("%llu %llu", &N, &K);
	fprintf(stderr, "N=%llu K=%llu\n", N, K);

    VPII pancakes(N);
    FOR(i,N)
    {
        llu ri,hi;
        scanf("%llu %llu", &ri, &hi);
        pancakes[i] = PII(ri,hi);
        fprintf(stderr, "ri,hi=%llu,%llu\n", ri, hi);
    }

    sort(all(pancakes));
    DE("Sorted by radi:\n");
    FOR(i,N)
    {
        DE("  ri,hi=%llu,%llu\n", pancakes[i].first, pancakes[i].second);
    }

    
    llu max_result = 0;
    for (int i=K-1; i<N; i++)
    {
        llu rmax = pancakes[i].first;
        llu hmax = pancakes[i].second;
        llu result_curr = rmax * rmax;
        result_curr += hmax * 2 * rmax;
        DE("i=%d: rmax=%llu, hmax=%llu, result=%llu\n", i, rmax, hmax, result_curr);

        VPII rest = pancakes;
        rest.resize(i);

        VI hrs;
        FOR(j,rest.size())
        {
            hrs.push_back(rest[j].first * rest[j].second);
        }

        sort(all(hrs));
        reverse(all(hrs));
        
        assert(hrs.size() >= K-1);
        FOR(j, K-1)
        {
            result_curr += 2 * hrs[j];
            DE("  adding hrs[%i] = %llu\n", j, hrs[j]);
        }
        DE("result_curr i=%d = %llu\n", i, result_curr);

        if (max_result < result_curr) {
            DE("Max with i=%d\n", i);
            max_result = result_curr;
        }
    }
	
	fprintf(stderr, "!!!!result = %.10llf\n\n", max_result*PI);
	printf("%.10llf\n", max_result*PI);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		fprintf(stderr, "Debug Case #%d:\n", i);
		printf ("Case #%d: ", i);
		solve();
	}
	return 0;
}
