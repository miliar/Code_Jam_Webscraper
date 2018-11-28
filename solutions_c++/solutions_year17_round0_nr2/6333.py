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

int ara[20];
int sz;

int dp[22][12][3][3];

bool func(int pos, int past, bool chole, bool shuru)  {
    if(pos == sz)   {
        return dp[pos][past][chole][shuru] = 1;
    }
    if(dp[pos][past][chole][shuru] != -1)  {
        return dp[pos][past][chole];
    }
    bool ans = 0;
    if(chole == 0)  {///mane ja icha ta boshano jabe
        ROF(i, 9, past)   {
            if((shuru == 0) && (i == 0))    {
                continue;
            }
            ans = ans | func(pos + 1, i, chole, 1);
        }
    }
    else    {
        ROF(i, ara[pos], past)   {
            if((shuru == 0) && (i == 0))    {
                continue;
            }
            if(i == ara[pos])   {
                ans = ans | func(pos + 1, i, chole, 1);
            }
            else    {
                ans = ans | func(pos + 1, i, 0, 1);
            }
        }
    }
    ///eita na niye
    if(shuru == 0)  {
        ans = ans | func(pos + 1, past, 0, 0);
    }
    return dp[pos][past][chole][shuru] = ans;
}

string bt(int pos, int past, bool chole, bool shuru)  {
    if(pos == sz)   {
        return "";
    }

    string ans = "";
    if(chole == 0)  {///mane ja icha ta boshano jabe
        ROF(i, 9, past)   {
            if((shuru == 0) && (i == 0))    {
                continue;
            }
            if(dp[pos + 1][i][chole][1] == 1)   {
                ans += (char)(i + '0');
                ans += bt(pos + 1, i, chole, 1);
                return ans;
            }
        }
    }
    else    {
        ROF(i, ara[pos], past)   {
            if((shuru == 0) && (i == 0))    {
                continue;
            }
            if(i == ara[pos])   {
                if(dp[pos + 1][i][chole][1] == 1)   {
                    ans += (char)(i + '0');
                    ans += bt(pos + 1, i, chole, 1);
                    return ans;
                }
            }
            else    {
                if(dp[pos + 1][i][0][1] == 1)   {
                    ans += (char)(i + '0');
                    ans += bt(pos + 1, i, 0, 1);
                    return ans;
                }
            }
        }
    }
    ///eita na niye
    ///ans += 'H';
    ans += bt(pos + 1, past, 0, 0);
    return ans;
}

int main()  {
    ///INP;OUT;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    ///cout << 999999999999999999LL;
    BOOST;
    int tc;
    cin >> tc;
    FOR(tt, 1, tc)   {
        LL n;
        cin >> n;
        LL tmp = n;
        sz = 0;
        while(tmp) {
            tmp /= 10;
            sz++;
        }
        tmp = n;
        int tmpsz = sz;
        while(tmp) {
            tmpsz--;
            ara[tmpsz] = tmp % 10;
            tmp /= 10;
        }
        /**
        FOR(i, 0, sz - 1)   {
            cout << ara[i];
        }
        cout << "\n";
        */
        ///cout << sz << "\n";
        MEM(dp, -1);
        func(0, 0, 1, 0);
        cout << "Case #" << tt << ": " << bt(0, 0, 1, 0) << "\n";
    }
    return 0;
}
/**
*/
