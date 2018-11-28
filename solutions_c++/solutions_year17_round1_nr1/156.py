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

const int M = 30;

char A[M][M];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("C:\\Users\\Dell\\Desktop\\A-large (1).in", "r", stdin);
    freopen("C:\\Users\\Dell\\Desktop\\out.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);

    int t, cs = 0;
    int i, j, k, row, col;

    in(t);
    while (t--)
    {
        in2(row, col);
        for (i = 0; i < row; i++) ins(A[i]);

        for (i = 0; i < row; i++)
        {
            for (j = 0; j < col; j++)
            {
                if (A[i][j] != '?')
                {
                    for (k = j + 1; A[i][k] == '?' && k < col; k++) A[i][k] = A[i][j];
                    for (k = j - 1; A[i][k] == '?' && k >= 0; k--) A[i][k] = A[i][j];
                }
            }
        }

        for (i = 0; i < row; i++)
        {
            for (j = 0; j < col; j++)
            {
                if (A[i][j] != '?')
                {
                    for (k = i + 1; A[k][j] == '?' && k < row; k++) A[k][j] = A[i][j];
                    for (k = i - 1; A[k][j] == '?' && k >= 0; k--) A[k][j] = A[i][j];
                }
            }
        }

        printf("Case #%d:\n", ++cs);
        for (i = 0; i < row; i++) puts(A[i]);
    }


return 0;
}

