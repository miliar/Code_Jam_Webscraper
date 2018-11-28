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

#define TEST_NUM "aa"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG

int arr[100];
int cnt[10];
int mem[101][101][101][4];
int p;

int f(int a, int b, int c, int r)
{
    if(mem[a][b][c][r] == -1)
    {
        mem[a][b][c][r] = 0;
        if(a)
            mem[a][b][c][r] = max(mem[a][b][c][r], f(a-1, b, c, (r+1)%p) + ((r+1)%p == 0));
        if(b)
            mem[a][b][c][r] = max(mem[a][b][c][r], f(a, b-1, c, (r+2)%p) + ((r+2)%p == 0));
        if(c)
            mem[a][b][c][r] = max(mem[a][b][c][r], f(a, b, c-1, (r+3)%p) + ((r+3)%p == 0));
    }
    return mem[a][b][c][r];
}

void process()
{
    memset(cnt, 0, sizeof(cnt));
    int n, r, i;
    scanf("%d%d", &n, &p);
    for(i = 0; i<n; i++)
        scanf("%d", &arr[i]);

    for(i = 0; i<n; i++)
        cnt[arr[i]%p]++;

    if(cnt[1] == 0 && cnt[2] == 0 && cnt[3] == 0)
    {
        printf("%d", cnt[0]);
        return;
    }

    if(p == 2)
    {
        if(cnt[1]%2)
            printf("%d", cnt[0] + cnt[1]/2 + 1);
        else
            printf("%d", cnt[0] + cnt[1]/2);
        return;
    }

    if(p == 3)
    {
        r = cnt[0];
        while(cnt[1] && cnt[2])
        {
            r++;
            cnt[1]--;
            cnt[2]--;
        }

        while(cnt[1] >= 3)
        {
            r++;
            cnt[1] -= 3;
        }

        while(cnt[2] >= 3)
        {
            r++;
            cnt[2] -= 3;
        }

        if(cnt[1] || cnt[2])
            printf("%d", r+1);
        else
            printf("%d", r);

        return;
    }

    r = 0;
    if(cnt[1])
        r = max(r, f(cnt[1]-1, cnt[2], cnt[3], 0));
    if(cnt[2])
        r = max(r, f(cnt[1], cnt[2]-1, cnt[3], 0));
    if(cnt[3])
        r = max(r, f(cnt[1], cnt[2], cnt[3]-1, 0));
    printf("%d", cnt[0] + r + 1);
}

void pre_process()
{
    memset(mem, -1, sizeof(mem));
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