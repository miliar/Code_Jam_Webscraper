#include <stdio.h>
#include <assert.h>
#include <map>

//#define DEBUG

typedef std::map< int, int > MII;

#ifdef DEBUG
#define DE(format, ...) fprintf(stderr,format, ##__VA_ARGS__)
void DE_MII(MII &m) {
    for (MII::iterator mit = m.begin(); mit != m.end(); ++mit)
    {
        DE(" %d:%d", mit->first, mit->second);
    }
    DE("\n");
}
#else
#define DE(format, ...)
#define DE_MII(m)
#endif


void solve()
{
	int N, K;
	scanf("%d %d", &N, &K);
	DE("N=%d K=%d\n", N, K);

    int minrl = -1;
	int maxrl = -1;
	
    MII space2cnt;
    space2cnt[N] = 1;
    
    int remaining = K;
    while (remaining > 0) {
        MII::reverse_iterator itMaxSpace = space2cnt.rbegin();
        assert(itMaxSpace != space2cnt.rend());
        int spaces = itMaxSpace->first;
        int numIntervals = itMaxSpace->second;
        minrl = (spaces - 1)/ 2;
        maxrl = spaces / 2;
        DE("remaining: %d\n", remaining);
        DE("Before: "); DE_MII(space2cnt);
        if (remaining <= numIntervals) {
            break;
        }
        remaining -= numIntervals;
        
        space2cnt.erase((++itMaxSpace).base());
        //space2cnt.erase(itMaxSpace->first);
        
        if (space2cnt.find(minrl) == space2cnt.end()) space2cnt[minrl] = 0;
        if (space2cnt.find(maxrl) == space2cnt.end()) space2cnt[maxrl] = 0;
        space2cnt[minrl] += numIntervals;
        space2cnt[maxrl] += numIntervals;
        DE("After: "); DE_MII(space2cnt);
	}
	
	DE("minrl = %d maxrl = %d\n", maxrl, minrl);
	printf("%d %d\n", maxrl, minrl);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf ("Case #%d: ", i);
		solve();
	}
	return 0;
}
