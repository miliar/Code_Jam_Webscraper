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

typedef long long int LL;
typedef double db;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;

int n, m;
char S[30][30];

void go(int r, int c)
{
    if(S[r][c] == '?')
        return;
    char cur = S[r][c];
    for(; c>=0; c--)
    {
        if(S[r][c] != '?')
            return;
        S[r][c] = cur;
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i, j, cs, t;
    sf(t);
    FRE(cs,1,t)
    {
        sff(n,m);
        FRL(i,0,n)
            scanf("%s",S[i]);
        FRL(i,0,n)
        {
            FRL(j,1,m)
            {
                if(S[i][j] == '?')
                    S[i][j] = S[i][j-1];
            }
        }
        FRL(i,0,n)
        {
            for(j = m-2; j>=0; j--)
            {
                if(S[i][j] == '?')
                    S[i][j] = S[i][j+1];
            }
        }
        FRL(i,1,n)
        {
            FRL(j,0,m)
            {
                if(S[i][j] == '?')
                    S[i][j] = S[i-1][j];
            }
        }
        for(i = n-2; i>=0; i--)
        {
            FRL(j,0,m)
            {
                if(S[i][j] == '?')
                    S[i][j] = S[i+1][j];
            }
        }
        printf("Case #%d:\n",cs);
        FRL(i,0,n)
            printf("%s\n",S[i]);
    }
    return 0;
}


