#include<bits/stdc++.h>
using namespace std;

#define FRE(i,a,b)  for(i = a; i <= b; i++)
#define FRL(i,a,b)  for(i = a; i < b; i++)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define all(x)      x.begin(),x.end()
#define un(x)       x.erase(unique(all(x)), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define sl(n)       scanf("%lld", &n)
#define sll(a,b)    scanf("%lld %lld", &a, &b)
#define slll(a,b,c) scanf("%lld %lld %lld", &a, &b, &c)
#define D(x)        cerr << #x " = " << (x) << '\n'
#define DBG         cerr << "Hi" << '\n'
#define pb          push_back
#define PI          acos(-1.00)
#define xx          first
#define yy          second
#define eps         1e-9

typedef unsigned long long int ULL;
typedef long long int LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;


inline int setBit(int N, int pos) { return N=N | (1<<pos); }
inline int resetBit(int N, int pos) { return N= N & ~(1<<pos); }
inline bool checkBit(int N, int pos) { return (bool)(N & (1<<pos)); }

//int fx[] = {+0, +0, +1, -1, -1, +1, -1, +1};
//int fy[] = {-1, +1, +0, +0, +1, +1, -1, -1}; //Four & Eight Direction

int n, p, hashUp[101][101][101][101], dp[26*26*26*26+10][4];
int call(vector<int> v, int leftOver)
{
    int h = hashUp[v[0]][v[1]][v[2]][v[3]];

    if(h == 0)
        return 0;

    if(dp[h][leftOver] != -1)
        return dp[h][leftOver];

    int ret = 0;
    for(int i = 0; i<4; i++)
    {
        if(v[i])
        {
            v[i]--;
            ret = max(ret, call(v, (p-(i-leftOver))%p));
            v[i]++;
        }
    }
    return dp[h][leftOver] = ret+(leftOver==0);
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i, j, cs, t, u;
    sf(t);
    FRE(cs,1,t)
    {
        D(cs);
        mem(dp,-1);
        vector<int>v;
        v.assign(4,0);
        sff(n,p);
        FRE(i,1,n)
        {
            sf(u);
            v[u%p]++;
        }
        int cnt = 0;
        for(int i = 0; i<=v[0]; i++)
        {
            for(int j = 0; j<=v[1]; j++)
            {
                for(int k = 0; k<=v[2]; k++)
                {
                    for(int m = 0; m<=v[3]; m++)
                    {
                        hashUp[i][j][k][m] = cnt++;
                    }
                }
            }
        }

        printf("Case #%d: %d\n",cs,call(v, 0));
    }
    return 0;
}


