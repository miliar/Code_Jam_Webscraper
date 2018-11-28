#include <bits/stdc++.h>
using namespace std;
#define pii             pair<int , int >
#define inf             1111111111
#define in(a)           scanf("%d", &a)
#define ins(a)          scanf("%s", a)
#define in2(a, b)       scanf("%d%d", &a, &b)
#define in3(a, b, c)    scanf("%d%d%d", &a, &b, &c)
#define pn              printf("\n")
#define pr(a)           printf("%d\n", a)
#define prs(a)          printf("%d ", a)
#define pr2(a, b)       printf("%d %d\n", a, b)
#define pr3(a, b, c)    printf("%d %d %d\n", a, b, c)
#define pcs(a)          printf("Case %d: ", a)
#define mp              make_pair
#define vi              vector<int >
#define _ceil(n, a)     ((n)%(a)==0?((n)/(a)):((n)/(a)+1))
#define cl              clear()
#define sz              size()
#define pb              push_back
#define mem(a, b)       memset((a), (b), sizeof(a))
#define all(X)          (X).begin(), (X).end ()
#define iter(it, X)     for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define ext(a)          {printf("%s\n", a); return 0;}
#define oka(x, y)       ((x)>=0&&(x)<row&&(y)>=0&&(y)<col)
#define x               first
#define y               second
#define lc              (2*i)
#define rc              (2*i+1)

typedef long long LL;
//int  dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int  dx[]={1,1,0,-1,-1,-1,0,1,0};int dy[]={0,1,1,1,0,-1,-1,-1,0};//8 direction
//int  dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//bool check(int n, int pos) {return (n & (1<<pos))>>pos;} //typecast 1 in case of int
//int  on(int n, int pos) {return n | (1<<pos);} //typecast 1 in case of int
//int  off(int n, int pos) {return n & ~(1<<pos);} //typecast 1 in case of int
//bool operator < (const data &d) const{return cost<d.cost;} //reverse in priority queue

const int M = 55;

struct data {
    int l, r;
    data(int a = 0, int b = 0) {l = a; r = b;}
    bool operator < (const data &d) const{return l == d.l ? r > d.r : l > d.l;}
};

priority_queue<data>q[M];
int A[M][M];
int req[M];

bool isempty(int n)
{
    for (int i = 0; i < n; i++) if (q[i].empty()) return true;
    return false;
}

bool hascommon(int n)
{
    int i, j, k, l = 0, r = inf;
    for (i = 0; i < n; i++)
    {
        data a = q[i].top();
        if (a.l > l) l = a.l;
        if (a.r < r) r = a.r;
        if (l > r) return false;
    }
    return true;
}

int solve(int n)
{
    int i, j, k, sum = 0;

    while (true)
    {
        if (isempty(n)) return sum;

        if (hascommon(n))
        {
            sum++;
            for (int i = 0; i < n; i++) q[i].pop();
        }
        else
        {
            int minn = inf, id;
            for (int i = 0; i < n; i++) if (q[i].top().r < minn) minn = q[i].top().r, id = i;
            q[id].pop();
        }
    }
    return sum;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("C:\\Users\\Dell\\Desktop\\B-large.in", "r", stdin);
    freopen("C:\\Users\\Dell\\Desktop\\out.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);

    int t, cs = 0;
    int i, j, k;
    int n, p, am;

    in(t);
    while (t--)
    {
        for (i = 0; i < M; i++) while (!q[i].empty()) q[i].pop();

        in2(n, p);
        for (i = 0; i < n; i++) in(req[i]);

        for (i = 0; i < n; i++)
        {
            for (j = 0; j < p; j++)
            {
                in(am);
                double low = (double)am/((double)req[i] * 1.1);
                double high = (double)am/((double)req[i] * .9);

                q[i].push(data((int)ceil(low), (int)floor(high)));
            }
        }

        printf("Case #%d: ", ++cs);
        pr(solve(n));
    }

return 0;
}

