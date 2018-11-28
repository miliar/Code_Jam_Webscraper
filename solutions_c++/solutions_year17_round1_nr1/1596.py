#include<bits/stdc++.h>

using namespace std;

#define PF           printf
#define SF(n)        scanf("%d", &n)
#define SFF(a,b)     scanf("%d %d", &a, &b)
#define SFFF(a,b,c)  scanf("%d %d %d", &a, &b, &c)
#define INF_I        2147483647    //max limit
#define INF          1999999999
#define PB           push_back
#define MEM(n, val)  memset((n), val, sizeof(n))
#define F            first
#define S            second
#define FOR(i, a, b) for(int i = a; i <= b; i++)
#define ROF(i, a, b) for(int i = a; i >= b; i--)
#define BOOST        std::ios_base::sync_with_stdio(false);
#define INP          freopen("in.txt", "r", stdin);
#define OUT          freopen("out.txt", "w", stdout);
#define MP           make_pair
#define INIT_RAND    srand(time(NULL))
#define MOD          1000000007
#define MX           (100010)
#define PI           acos(-1.0)
#define eps          .0000000001

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;
typedef pair<long long, long long> PLL;
typedef priority_queue<int> PQ;
typedef queue<int> Q;
typedef stringstream SS;

int r, c;
string str[30];

int main()  {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    ///OUT;
    BOOST;
    ///cout << "hi\n";
    int tc;
    cin >> tc;
    FOR(tt, 1, tc)   {

        cin >> r >> c;
        FOR(i, 0, r - 1)   {
            cin >> str[i];
        }
        FOR(j, 0, c - 1)   {
            bool chk = 0;

            if(str[0][j] != '?')   {
                chk = 1;
            }
            FOR(i, 1, r - 1)   {
                if((str[i][j] == '?') && str[i - 1][j] != '?')    {
                    str[i][j] = str[i - 1][j];
                }
                if(str[i][j] != '?')   {
                    chk = 1;
                }
            }
            if(chk) {
                ROF(i, r - 2, 0)   {
                    if((str[i][j] == '?') && str[i + 1][j] != '?')    {
                        str[i][j] = str[i + 1][j];
                    }
                }
            }
            else if(j > 0)   {
                FOR(i, 0, r - 1)   {
                    if(str[i][j - 1] == '?')    {
                        break;
                    }
                    str[i][j] = str[i][j - 1];
                }
            }
        }
        ROF(j, c - 2, 0)   {
            FOR(i, 0, r - 1)   {
                if(str[i][j] != '?')    {
                    break;
                }
                str[i][j] = str[i][j + 1];
            }
        }
        cout << "Case #" << tt << ":\n";
        FOR(i, 0, r - 1)   {
            cout << str[i] << "\n";
        }
    }
    return 0;
}
/**
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE


2
4 4
????
????
??L?
????
5 5
?????
?Q???
?????
?????
????z
*/
