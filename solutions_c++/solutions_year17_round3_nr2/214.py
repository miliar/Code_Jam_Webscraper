
#include<bits/stdc++.h>
using namespace std;
#define D(x)        cout << #x " = " << (x) << endl
#define MAX         1440
typedef long long int LL;

#define CAMERON         0
#define JAMIE           1


int clr[MAX+5];
const int inf = 100000000;
int dp[MAX+5][MAX+5][3];
int mustLast;

int F(int pos, int wJAMIE, int prv)
{
    if(pos == MAX){
        if(wJAMIE != MAX/2) return inf;
        return 0;
    }

    if(dp[pos][wJAMIE][prv] != -1) return dp[pos][wJAMIE][prv];

    if(clr[pos] != -1){

        if(clr[pos] == JAMIE)
        {
            if(prv == JAMIE) return dp[pos][wJAMIE][prv] = F(pos + 1, wJAMIE + 1, JAMIE);
            return dp[pos][wJAMIE][prv] = 1 + F(pos+1, wJAMIE + 1, JAMIE);
        }
        else
        {
            if(prv == CAMERON) return dp[pos][wJAMIE][prv] = F(pos + 1, wJAMIE, CAMERON);
            return dp[pos][wJAMIE][prv] = 1 + F(pos+1, wJAMIE, CAMERON);
        }
    }

    ///Let JAMIE do it
    int ret = inf, current;
    if(prv == JAMIE)
    {
        current = F(pos + 1, wJAMIE + 1, JAMIE);
        ret = min(ret, current);
    }
    else
    {
        current = 1 + F(pos + 1, wJAMIE + 1, JAMIE);
        ret = min(ret, current);
    }

    ///Let CAMERON do it
    if(prv == CAMERON)
    {
        current = F(pos + 1, wJAMIE, CAMERON);
        ret = min(ret, current);
    }
    else
    {
        current = 1 + F(pos + 1, wJAMIE, CAMERON);
        ret = min(ret, current);
    }

    return dp[pos][wJAMIE][prv] = ret;
}


int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int i, j, k, t, cs;
    int ac, aj, st, ed;

    scanf("%d", &t);
    for(cs = 1; cs <= t; cs++)
    {
        memset(clr, -1, sizeof(clr));
        memset(dp, -1, sizeof(dp));

        scanf("%d %d", &ac, &aj);

        for(i = 1; i <= ac; i++)
        {
            scanf("%d %d", &st, &ed);
            for(j = st; j < ed; j++) clr[j] = CAMERON;
        }

        for(i = 1; i <= aj; i++)
        {
            scanf("%d %d", &st, &ed);
            for(j = st; j < ed; j++) clr[j] = JAMIE;
        }

        int answer = inf, current;
        int ind0 = (clr[0] == -1);
        int indM = (clr[MAX-1] == -1);

        for(i = 0; i < 2; i++)
            for(j = 0; j < 2; j++)
            {
                memset(dp, -1, sizeof(dp));

                if(clr[0] != -1){
                    if(i != clr[0]) continue;
                }

                if(clr[MAX-1] != -1){
                    if(j != clr[MAX-1]) continue;
                }

                clr[0] = i;
                clr[MAX-1] = j;
                answer = min(answer, current + F(0, 0, j));

                if(ind0) clr[0] = -1;
                if(indM) clr[MAX-1] = -1;
            }
        printf("Case #%d: %d\n", cs, answer);
    }

    return 0;

}
