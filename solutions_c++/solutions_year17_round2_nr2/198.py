#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef double rl;

#define pb push_back
#define popb pop_back
#define mp make_pair
#define mt make_tuple

int N, R, O, Y, G, B, V;
char answ[2009];

bool solveSmall()
{
    int NN = R+Y+B;

    int rem[4] = {R, Y, B, 0};
    int pr = 3;
    answ[ 0 ] = 3;

    for (int i=0; i<NN; i++)
    {
        int larg = 3;
        for (int j=0; j<3; j++)
        {
            if (j == pr || (rem[ j ] < rem[ larg ] || (rem[ j ] == rem[ larg ] && j!=answ[0])))
                continue;
            larg = j;
        }
        if (larg == 3)
            return false;
        rem[larg]--;
        pr = larg;
        answ[ i ] = larg;
    }

    for (int i=0; i<NN; i++)
        if (answ[ i ] == 0)
            answ[ i ] = 'R';
        else if (answ[ i ] == 1)
            answ[ i ] = 'Y';
        else if (answ[ i ] == 2)
            answ[ i ] = 'B';
        else
            answ[ i ] = 'x';
    answ[ NN ] = '\0';

    if (answ[ 0 ] == answ[ NN-1 ])
        return false;

    return true;
}

void Gen(char a, char b)
{
    for (int i=0; i<N; i+=2)
    {
        answ[ i ] = a;
        answ[ i+1 ] = b;
    }
    answ[ N ] = '\0';
}

void repl(string& tmp, char r, char inside, int cnt) // RVRVR
{
    int pos = 0;
    while (tmp[ pos ] != r) pos++;

    string replwith = "";;
    replwith.push_back(r);
    for (int i=0; i<cnt; i++)
        replwith.push_back(inside), replwith.push_back(r);

    tmp.replace(pos, 1, replwith);
}

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen(".out", "w+", stdout);
    //ios_base::sync_with_stdio( false );cin.tie(0); cout.tie(0);

    int T;
    scanf("%d", &T);
    for (int test = 1; test<=T; test++)
    {
        scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
        bool impossible = false;

        if (O == 0 && G == 0 && V == 0)
        {
            impossible = false == solveSmall();
        }
        else if (R + G == N)
        {
            if (R == G)
                Gen('R','G');
            else
                impossible = true;
        }
        else if (Y + V == N)
        {
            if (Y == V)
                Gen('Y','V');
            else
                impossible = true;
        }
        else if (B + O == N)
        {
            if (B == O)
                Gen('B','O');
            else
                impossible = true;
        }
        else
        {
            if (G!=0 && R <= G)
                impossible = true;
            if (O!=0 && B <= O)
                impossible = true;
            if (V!=0 && Y <= V)
                impossible = true;

            if (impossible == false)
            {
                R-=G;
                B-=O;
                Y-=V;

                impossible = false == solveSmall();
            }

            if (impossible == false)
            {
                string tmp = answ;
                if (G!=0)
                    repl(tmp, 'R', 'G', G);
                if (O!=0)
                    repl(tmp, 'B', 'O', O);
                if (V!=0)
                    repl(tmp, 'Y', 'V', V);
                tmp.copy(answ, tmp.size());
            }
        }

        if (impossible)
            sprintf(answ, "IMPOSSIBLE");
        else
            answ[ N ] = '\0';

        printf("Case #%d: %s\n", test, answ);
    }

    return 0;
}


