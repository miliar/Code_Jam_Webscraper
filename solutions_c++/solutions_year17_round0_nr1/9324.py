#include <iostream>
#include <string.h>
using namespace std;

char S[1000];
int T, K;
char c;

bool check_remain(int r)
{
    for (int i = 1; i < K; i++)
    {
        if (S[r+i]!=S[r+i-1])
            return false;
    }
    return true;
}

void flip(int p)
{
    for (int i = 0; i < K; i++)
    {
        int l = p+i;
        if (S[l]=='+')
            S[l]='-';
        else
            S[l]='+';
    }
    return;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &T);
    T++;
    for (int k = 1; k < T; k++)
    {
        scanf("%s%d", S, &K);
        int i = strlen(S);
        int f =0; //number of flips
        int r = i - K;
        for (int j = 0; j < r; j++)
        {
            if (S[j]=='-')
            {
                flip(j);
                f++;
            }
            //cout << "r=" << r << "\n";
            //cout << S << "\n";
        }
        printf ("Case #%d: ", k);
        if (check_remain(r))
        {
            if (S[r]=='-')
                printf("%d\n", f+1);
            else
                printf("%d\n", f);
        }
        else
            printf("IMPOSSIBLE\n");

    }
    return 0;
}
