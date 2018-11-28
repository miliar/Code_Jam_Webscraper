#include <stdio.h>
#include <assert.h>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

#define all(a) a.begin(), a.end()

using namespace std;

typedef unsigned long long int llu;
typedef long double llf;
typedef map< llu, llu > MII;
typedef vector< llu > VI;
typedef vector<VI> VVI;
typedef set< llu > SI;
typedef vector < pair <llu, llu> > VPI;


#define DEBUG

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


void solve()
{
	llu D, N;
	scanf("%llu %llu", &D, &N);
	fprintf(stderr, "D=%llu N=%llu\n", D, N);
    VPI ks(N);
    for (int i = 0; i < N; i++) {
        scanf("%llu %llu", &(ks[i].first), &(ks[i].second));
    }
    for (int i = 0; i < N; i++) {
        DE("i:%llu K,S = %llu %llu\n", i, (ks[i].first), (ks[i].second));
    }

    //sort(ks.begin(), ks.end());
    llf max_time = 0;
    for (int i = N-1; i>=0; i--)
    {
        llu k = ks[i].first;
        llu s = ks[i].second;
        assert (k < D && k > 0);
        assert(s > 0);
        llf time = ((llf)(D-k))/s;
        DE("i = %llu, time = %llf, k, s = %llu, %llu D-k=%llu\n", i, time, k, s, D-k);
        if (time > max_time) {
            max_time = time;
        }
        DE("max_time, k, s = %llf, %llu, %llu\n", max_time, k, s);
    }
    
    llf result = D/max_time;
	fprintf(stderr, "!!!!result = %llf\n\n", result);
	printf("%llf\n", result);
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
