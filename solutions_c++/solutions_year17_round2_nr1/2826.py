#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std;

int main ()
{
	int T , N;
    scanf ("%d", &T);
    for (int t = 0; t < T; t++)
    {
		int D, N;
        scanf ("%d %d", &D, &N);
		float mx = 0;
		for(int i = 0; i < N; i++)
		{
			int k,sp;
			scanf("%d%d", &k,&sp);
			float f = (float)(D-k)/(float)sp;
			mx = max(f, mx);
		}
        printf ("Case #%d: %0.6f\n", t + 1, (float)D/mx);
    }

    return 0;
}