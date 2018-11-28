#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <tuple>
#include <iterator>

using namespace std;

#define TEST_NUM "b"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG

int arr[1010][2];
int cnt[1010];
int loc[1010][1010];

void process()
{
    memset(cnt, 0, sizeof(cnt));
    memset(loc, 0, sizeof(loc));

    int n, c, m, p, b, x, y, r1, r2, t, i;
    scanf("%d%d%d", &n, &c, &m);
    for(i = 0; i<m; i++)
        scanf("%d%d", &arr[i][0], &arr[i][1]);

    if(c != 2)
        return;

    for(i = 0; i<m; i++)
    {
        loc[arr[i][0]][arr[i][1]]++;
        cnt[arr[i][1]]++;
    }

    x = loc[1][1];
    y = loc[1][2];

    t = max({ 0, cnt[1] - x - y, cnt[2] - y - x });
    r1 = x + y + t;
    r2 = 0;
    for(i = 2; i<=n; i++)
        r2 = max(r2, max(0, max(0, loc[i][1] - y) + max(0, loc[i][2] - x) - t));

    printf("%d %d", r1, r2);
}

void pre_process()
{

}

int main()
{
#ifndef DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
#ifdef _DEBUG
    fprintf(stderr, "\nYou are using DEBUG MODE!!!\n\n");
#endif
    char inname[100];
    char outname[100];
    sprintf(inname, "%s.in", TEST_NUM);
    sprintf(outname, "%s.out", TEST_NUM);
    freopen(inname, "r", stdin);
    freopen(outname, "w", stdout);
#endif
    int tn, ti;
    scanf("%d", &tn);
    pre_process();
    for(ti = 1; ti<=tn; ti++)
    {
        fprintf(stderr, "Case %d/%d\n", ti, tn);
        printf("Case #%d: ", ti);
        process();
        printf("\n");
    }
    return 0;
}