#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <string>
#include <string.h>
#include <math.h>

using namespace std;

// typedefs
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int,int> pii;

// constants
const double PI = 2.0*acos(0.0);
const double EPS = 1e-9;  // too small/big?????

const int INF = 10000000;

int dp[1500][1500][2][2];
int cd[1500];
int jk[1500];

// magic
int solve()
{
    int i,j,k,s,e,C,J;
    // Reset
    for(i=0;i<1500;i++)
    {
        for(j=0;j<1500;j++)
            dp[i][j][0][0] = dp[i][j][0][1] = dp[i][j][1][0] = dp[i][j][1][1] = INF;
        cd[i]=jk[i]=0;
    }
    // Now Solve!
    cin>>C>>J;
    for(i=0;i<C;i++)
    {
        cin>>s>>e;
        s++;e++;
        for(j=s;j<e;j++)
            cd[j] = 1;
    }
    for(i=0;i<J;i++)
    {
        cin>>s>>e;
        s++;e++;
        for(j=s;j<e;j++)
            jk[j] = 1;
    }

    // 0 is Cameron
    // 1 is Jamie
    dp[1][1][0][0] = 0;
    dp[1][1][0][1] = 1;
    dp[1][0][1][1] = 0;
    dp[1][0][1][0] = 1;

    // lallalalalalalala
    for(i=2; i<=1440; i++)
    {
        for(j=max(i-720,0);j<=min(i,720);j++)
        {
            for(k=0; k<2;k++)
            {
                //cerr<<i<<j<<endl;
                if(!j || cd[i])
                    dp[i][j][0][k] = INF;
                else
                    dp[i][j][0][k] = min(dp[i-1][j-1][0][k], dp[i-1][j-1][1][k]+1);

                if(i==j || jk[i])
                    dp[i][j][1][k] = INF;
                else
                    dp[i][j][1][k] = min(dp[i-1][j][1][k], dp[i-1][j][0][k]+1);
            }
        }
    }
    //cerr<<dp[2][2][0]<<" " <<dp[2][0][1]<<" "<<dp[3][3][0]<<" "<<dp[3][0][1]<<endl<<dp[2][1][0]<<" "<<dp[2][1][1]<<endl;
    return min(dp[1440][720][0][0], dp[1440][720][1][1]);
}

int main()
{
    int T;
    cin>>T;
    for(int tc=1; tc<=T; tc++)
    {
        cerr << "Running test #" << tc << "..." << endl;
        printf("Case #%d: %d\n", tc, solve());
    }
    return 0;
}