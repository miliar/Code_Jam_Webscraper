#include <bits/stdc++.h>

#define MAXN 102

#define cin fin
#define cout fout

using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

int T, N, P, G;
int modula[4];
int dp2[2][MAXN][MAXN];
int dp3[3][MAXN][MAXN][MAXN];
int dp4[4][MAXN][MAXN][MAXN][MAXN];

int Solve2(int pack, int mod0, int mod1) {
    if (mod0+mod1 == 0) return 0;

    if (dp2[pack][mod0][mod1] != -1)
        return dp2[pack][mod0][mod1];

    int retval = 0;
    if (mod0 > 0) retval = max(retval, Solve2(pack, mod0-1, mod1));
    if (mod1 > 0) retval = max(retval, Solve2((pack+1)%2, mod0, mod1-1));
    retval += (pack == 0 ? 1 : 0);
    dp2[pack][mod0][mod1] = retval;
    return retval;
}

int Solve3(int pack, int mod0, int mod1, int mod2) {
    if (mod0+mod1+mod2 == 0) return 0;

    if (dp3[pack][mod0][mod1][mod2] != -1)
        return dp3[pack][mod0][mod1][mod2];

    int retval = 0;
    if (mod0 > 0) retval = max(retval, Solve3(pack, mod0-1, mod1, mod2));
    if (mod1 > 0) retval = max(retval, Solve3((pack+2)%3, mod0, mod1-1, mod2));
    if (mod2 > 0) retval = max(retval, Solve3((pack+1)%3, mod0, mod1, mod2-1));
    retval += (pack == 0 ? 1 : 0);
    dp3[pack][mod0][mod1][mod2] = retval;
    return retval;
}

int Solve4(int pack, int mod0, int mod1, int mod2, int mod3) {
    if (mod0+mod1+mod2 == 0) return 0;

    if (dp4[pack][mod0][mod1][mod2][mod3] != -1)
        return dp4[pack][mod0][mod1][mod2][mod3];

    int retval = 0;
    if (mod0 > 0) retval = max(retval, Solve4(pack, mod0-1, mod1, mod2, mod3));
    if (mod1 > 0) retval = max(retval, Solve4((pack+3)%4, mod0, mod1-1, mod2, mod3));
    if (mod2 > 0) retval = max(retval, Solve4((pack+2)%4, mod0, mod1, mod2-1, mod3));
    if (mod3 > 0) retval = max(retval, Solve4((pack+1)%4, mod0, mod1, mod2, mod3-1));
    retval += (pack == 0 ? 1 : 0);
    dp4[pack][mod0][mod1][mod2][mod3] = retval;
    return retval;
}

int main()
{
    memset(dp2, -1, sizeof dp2);
    memset(dp3, -1, sizeof dp3);
    memset(dp4, -1, sizeof dp4);
    cin >> T;

    for (int caseno=1; caseno<=T; caseno++) {
        cin >> N >> P;
        for (int i=0; i<4; i++) modula[i] = 0;
        for (int i=0; i<N; i++) {
            cin >> G;
            modula[G%P] ++;
        }

        cout << "Case #" << caseno << ": ";

        if (P == 2)
            cout << Solve2(0, modula[0], modula[1]);
        else if (P == 3)
            cout << Solve3(0, modula[0], modula[1], modula[2]);
        else
            cout << Solve4(0, modula[0], modula[1], modula[2], modula[3]);
        cout << endl;
    }

    return 0;
}
