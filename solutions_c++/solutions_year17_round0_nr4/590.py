#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair < int, int > PII;

const int N = 1e2 + 7;

int n, m;
bool X1[N], X2[N];
unordered_set < int > P1, P2;
char S[N][N];
bool X[N][N], P[N][N];
vector < pair < char, PII > > ans;

int main()
{
    int te; scanf("%d", &te);
    for(int t = 1; t <= te; t++)
    {
        scanf("%d%d", &n, &m);
        P1.clear(), P2.clear();
        ans.clear();
        for(int i = 1; i <= n; i++)
            X1[i] = X2[i] = 0;
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++)
                S[i][j] = X[i][j] = P[i][j] = 0;
        int res = 0, ile = 0;
        while(m--)
        {
            int a, b; char c; scanf(" %c %d %d", &c, &a, &b);
            S[a][b] = c;
            if(c != '+')
            {
                X[a][b] = 1;
                X1[a] = 1;
                X2[b] = 1;
                res++;
            }
            if(c != 'x')
            {
                P[a][b] = 1;
                P1.insert(a + b);
                P2.insert(a - b);
                res++;
            }
        }
        for(int i = 1; i <= n; i++)
        {
            for(int j = 1; j <= n; j++)
            {
                if(!X1[i] && !X2[j])
                {
                    X[i][j] = 1, X1[i] = 1, X2[j] = 1;
                    res++;
                }
            }
        }
        for(int j = 1; j <= n; j++)
        {
            int i = 1;
            if(P1.find(i + j) == P1.end() && P2.find(i - j) == P2.end())
            {
                P1.insert(i + j);
                P2.insert(i - j);
                P[i][j] = 1;
                res++;
            }
        }
        for(int j = 1; j <= n; j++)
        {
            int i = n;
            if(P1.find(i + j) == P1.end() && P2.find(i - j) == P2.end())
            {
                P1.insert(i + j);
                P2.insert(i - j);
                P[i][j] = 1;
                res++;
            }
        }
        for(int i = 1; i <= n; i++)
        {
            for(int j = 1; j <= n; j++)
            {
                if(S[i][j] == 'o') continue;
                if((S[i][j] == 'x' && P[i][j]) || (S[i][j] == '+' && X[i][j]) || (P[i][j] && X[i][j]))
                {
                    ile++;
                    ans.push_back({'o', {i, j}});
                    continue;
                }
                if(S[i][j] != 'x' && X[i][j])
                {
                    ile++;
                    ans.push_back({'x', {i, j}});
                }
                if(S[i][j] != '+' && P[i][j])
                {
                    ile++;
                    ans.push_back({'+', {i, j}});
                }
            }
        }
        printf("Case #%d: %d %d\n", t, res, ile);
        for(auto x: ans) printf("%c %d %d\n", x.first, x.second.first, x.second.second);
    }
    return 0;
}
