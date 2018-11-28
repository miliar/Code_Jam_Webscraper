#include <bits/stdc++.h>

#define INF 1000000000
#define MAXN 102

#define cin fin
#define cout fout

using namespace std;

ifstream fin("C-small-attempt2.in");
ofstream fout("C-small-attempt2.out");

int T;
int Hd, Ad, Hk, Ak, B, D;
int dp[MAXN][2*MAXN][MAXN][MAXN];   /// Hd, Ad, Hk, Ak

int Solve(int HD, int AD, int HK, int AK) {
    if (AD >= 2*MAXN) return INF;

    if (HK <= 0) return 0;
    if (HD <= 0) return INF;
    AK = max(AK, 0);
    if (dp[HD][AD][HK][AK] == -2) return dp[HD][AD][HK][AK] = INF;

    if (dp[HD][AD][HK][AK] != -1) return dp[HD][AD][HK][AK];
    dp[HD][AD][HK][AK] = -2;

    int retval = INF;
    retval = min(retval, Solve(HD-AK, AD, HK-AD, AK));  /// attack
    if (retval > 0)
    retval = min(retval, Solve(HD-AK, AD+B, HK, AK)); /// buff
    if (retval > 0)
    retval = min(retval, Solve(Hd-AK, AD, HK, AK));   /// cure
    if (retval > 0)
    retval = min(retval, Solve(HD-max(AK-D, 0), AD, HK, AK-D));  /// debuff
    if (retval != INF) retval ++;
    dp[HD][AD][HK][AK] = retval;
    return retval;
}

int main()
{
    cin >> T;

    for (int caseno=1; caseno<=T; caseno++) {
        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
        memset(dp, -1, sizeof dp);

        int answer = Solve(Hd, Ad, Hk, Ak);
        cout << "Case #" << caseno << ": ";
        if (answer == INF)  cout << "IMPOSSIBLE\n";
        else cout << answer << endl;
    }

    return 0;
}
