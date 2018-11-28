#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

char S[1001];

void flip(int s, int e) {
    for (int i = s; i < e; i++)
        S[i] = (S[i] == '+') ? '-' : '+';
}

int solve(int start, int end, int k) {
    //printf("start = %d, end = %d\n", start, end);
    int ans = -1;
    int s, e;
    for (s = start; s <= end; s++)
        if (S[s] == '-')
            break;

    if (s > end)
        return 0;

    for (e = end; ; e--)
        if (S[e] == '-')
            break;

    if (e-s+1 < k)
        return -1;

    flip(s,s+k);
    int a = solve (s,e,k);
    if (a != -1) {
        ans = a+1;
    }

    flip(s,s+k);
    flip(e-k+1,e+1);

    a = solve(s,e,k);
    if (a != -1) {
        if (ans == -1)
            ans = a+1;
        else
            ans = min(ans, a+1);
    }
    
    flip(e-k+1,e+1);
    return ans;
}

int main(int argc, char **argv)
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
   
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        scanf("%s", S);

        int k;
        scanf("%d", &k);

        int ans = solve(0,strlen(S)-1,k);

        if (ans == -1)
            printf("IMPOSSIBLE");
        else 
            printf("%d", ans);

        printf("\n");
    }

	return 0;
}
