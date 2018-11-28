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

const int M = 500;

int h, a;
int kh, ka;
int buff, debuff;

int simulate(int x, int y)
{
    int tt = 0;
    int hh = h, aa = a, khh = kh, kaa = ka;

    while (tt <= M)
    {
        tt++;

        if (x > 0)
        {
            int tempat = max(kaa - debuff, 0);
            if (hh - tempat <= 0) hh = h;
            else kaa -= debuff;
            x--;
        }
        else if (y > 0)
        {
            if (hh - kaa <= 0) hh = h;
            else aa += buff;
            y--;
        }
        else
        {
            if (khh - aa <= 0) return tt;

            if (hh - kaa <= 0) hh = h;
            else khh -= aa;
        }

        hh -= kaa;
        if (hh <= 0) return M;
    }

    return tt;
}

bool ispossible(int turn)
{

    for (int d = 0; d <= turn; d++)
    {
        for (int b = 0; b + d <= turn; b++)
        {
            if (simulate(b, d) <= turn) return true;
        }
    }

    return false;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("C:\\Users\\Dell\\Desktop\\C-small-attempt0.in", "r", stdin);
    freopen("C:\\Users\\Dell\\Desktop\\out.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);

    int t, cs = 0;
    int i, j, k;

    in(t);
    while (t--)
    {
        in2(h, a);
        in2(kh, ka);
        in2(buff, debuff);

        int l = 1, r = M;

        while (l < r)
        {
            int m = (l + r)/2;

            if (ispossible(m)) r = m;
            else l = m + 1;
        }

        printf("Case #%d: ", ++cs);
        r >= M ? printf("IMPOSSIBLE\n") : pr(r);

//        cerr<<r<<endl;
    }


return 0;
}

