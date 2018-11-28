#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>
#define pb push_back
#define mp make_pair
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const double PI = acos(-1.0);
const double eps = 1e-6;
const int INF = 0x3f3f3f3f;
template <typename T>
inline bool scan_d (T &ret) {
    char c;
    int sgn;
    if (c = getchar(), c == EOF) return 0; //EOF
    while (c != '-' && (c < '0' || c > '9') ) c = getchar();
    sgn = (c == '-') ? -1 : 1;
    ret = (c == '-') ? 0 : (c - '0');
    while (c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + (c - '0');
    ret *= sgn;
    return 1;
}

int R,C;

const int maxn = 30;
char board[maxn][maxn];

int main()
{
    //freopen("data.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scan_d<int>(T);
    for(int cas=1; cas<=T; cas++)
    {
        scanf("%d%d",&R,&C);
        for(int i=1; i<=R; i++)
        {
            scanf("%s",board[i]+1);
        }
        for(int i=1; i<=R; i++)
        {
            bool first = true;
            for(int j=1; j<=C; j++)
            {
                if(first)
                {
                    if(board[i][j] == '?')
                        continue;
                    else
                    {
                        for(int k=1; k<j; k++) board[i][k] = board[i][j];
                        char cur = board[i][j];
                        for(++j; j<=C && board[i][j] == '?'; j++)
                        {
                            board[i][j] = cur;
                        }
                        --j;
                        first = false;
                    }
                }
                else
                {
                    char cur = board[i][j];
                    for(++j; j<=C && board[i][j] == '?'; j++)
                    {
                        board[i][j] = cur;
                    }
                    --j;
                }
            }
        }
        queue<int> Q;
        for(int i=1; i<=R; i++)
        {
            if(board[i][1] != '?') Q.push(i);
        }
        while(!Q.empty())
        {
            int cur = Q.front(); Q.pop();
            if(cur > 1 && board[cur-1][1] == '?')
            {
                memcpy(board[cur-1],board[cur],sizeof(board[cur-1]));
                Q.push(cur-1);
            }
            if(cur < R && board[cur+1][1] == '?')
            {
                memcpy(board[cur+1],board[cur],sizeof(board[cur+1]));
                Q.push(cur+1);
            }
        }
        printf("Case #%d: \n",cas);
        for(int i=1; i<=R; i++)
        {
            for(int j=1; j<=C; j++)
            {
                putchar(board[i][j]);
            }
            puts("");
        }
    }
    return 0;
}
