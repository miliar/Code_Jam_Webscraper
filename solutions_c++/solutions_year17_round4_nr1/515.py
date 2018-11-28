#include <bits/stdc++.h>
using namespace std;

map<int, int> M;

int main()
{
    freopen("A-large (1).in", "r", stdin);
    freopen("output2.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int test=1; test<=T; test++)
    {
        int N, P;
        scanf("%d %d", &N, &P);

        M.clear();

        for(int i=1; i<=N; i++)
        {
            int x;
            scanf("%d", &x);

            M[x%P]++;
        }

        int ans = 0;

        if(P==2)
            ans = M[0] + (M[1]+1)/2;
        else if(P==3)
        {
            if(M[1]<M[2])
                ans = M[0] + M[1] + (M[2]-M[1]+2)/3;
            else
                ans = M[0] + M[2] + (M[1]-M[2]+2)/3;
        }
        else
        {
            int rem1 = max(M[1], M[3]) - min(M[1], M[3]);
            int rem2 = M[2]%2;

            ans = M[0] + M[2]/2 + min(M[1], M[3]);

            if(rem2)
            {
                if(rem1==0)
                    ans++;
                else if(rem1>1)
                    rem1 -= 2, ans++;
            }

            ans += (rem1+3)/4;
        }

        printf("Case #%d: %d\n", test, ans);
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
